import xnat
import sys
import os

#Download
subject_min = int( sys.argv[ 1 ] )
folder_min = int( sys.argv[ 2 ] )

session = xnat.connect( "http://18.188.8.197", user="admin", password="admin" )

project_name = "Train"

project = session.projects[ project_name ]

def download( project, subject_min, subject_max, dir_loc ):
    subject_n = subject_min
    i = subject_min
    while i < subject_max:
    #for i in range( subject_min, subject_max, 1 ):
        subject_name = f"train_{subject_n}"
        subject = project.subjects[ subject_name ]
        subject_n += 1
        for session in subject.experiments:
            print( f"train_{subject_n}_{session}" )
            if not "CTCLIP" in subject.experiments[ session ].resources:
                print( f"Downloading {subject_name}" )
                subject.experiments[ session ].download_dir( dir_loc )
                i += 1

#Prep

import preprocess
import pandas as pd
from multiprocessing import Pool
import shutil
from tqdm import tqdm

def prep( dir_loc ):
    split_to_preprocess = dir_loc #select the validation or test split
    nii_files = preprocess.read_nii_files(split_to_preprocess)


    num_workers = 1  # Number of worker processes

    for i in tqdm( range( len( nii_files ) ) ):
        preprocess.process_file( nii_files[ i ], dir_loc.replace( "input", "batch" ) )

n = folder_min
batch = 18
for i in range( subject_min, 20000, batch ):
    print( "Downloading..." )
    os.mkdir( f"./input/{n}/" )
    download( project, i, i + batch, f"./input/{n}/" )
    prep( f"./input/{n}/" )
    n += 1
