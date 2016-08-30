#!/bin/bash
#This script run every 1 seconds
while (sleep 1 &&  sudo python3 /home/baas/webOs/add_data_to_database.py) &
do
  wait $!
done
