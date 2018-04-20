#!/bin/bash 

COUNT=0

for f in $(ls --sort=time /media/backup/); do
	((COUNT = COUNT + 1))
	if [ $COUNT -gt 3 ]; then
		rm /media/backup/$f
	fi
done
		

