#! /bin/bash


N=0

while [ $N == 0 ];
do
	echo "Restarting text script"
	python scripts/run_text_zero_shot.py
	N=$?
done

