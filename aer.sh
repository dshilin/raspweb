#!/bin/bash
#This script run every 30 seconds
while (sleep 30 &&  sudo python /home/pi/webOs/aeration.py)  &
do
  wait $!
done
