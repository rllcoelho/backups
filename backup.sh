#!/bin/bash 
sudo rsync -aprv --backup --suffix="-bkp-$(date +%s)" /home/rafael/Documents/Desafio_STI/ /media/backup/
