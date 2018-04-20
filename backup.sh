#!/bin/bash 
sudo rsync -aprv --backup --suffix="-bkp-$(date +%s)" /home/ /media/backup/
