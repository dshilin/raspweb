#!/bin/bash
cd webOs
sudo chown pi:pi /home/pi/webOs/
sudo chown pi:pi /home/pi/webOs/*
sudo chmod a+x add_current_value.sh add_data_to_database.py get_aer_start_par.py get_aer_stop_par.py get_hum_par.py get_temp_par.py is_enabled.py processon.py processoff.py relay.py select_current_temp.py select_current_hum.py set_params.py 

