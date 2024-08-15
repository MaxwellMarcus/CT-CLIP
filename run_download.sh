#! /bin/bash


N=0

while [ $N == 0 ];
do
	folder=`ls input -v | tail -1`
	echo ${folder}
	IN=`ls input/${folder} | head -1`
	echo ${IN}
	arrIN=(${IN//_/ })
	subject=${arrIN[1]}
	rm -rf input/$folder
	echo "Starting with folder $folder and subject $subject"

	python scripts/download_files.py 3000 $folder
	N=$?
done

