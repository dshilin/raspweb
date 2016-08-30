BEGIN;
CREATE TABLE IF NOT EXISTS CURR_TEMP (tdate DATE, ttime TIME, temperature NUMERIC, humidity NUMERIC);
CREATE TABLE IF NOT EXISTS CAMERA_PARAMS (tdate DATE, ttime TIME, temp_par NUMERIC, hum_par NUMERIC, is_enabled BOOL, aer_start NUMERIC, aer_stop NUMERIC);
INSERT INTO CURR_TEMP values(date('now'), time('now'), 25, 42);
INSERT INTO CAMERA_PARAMS values(date('now'), time('now'), 12, 80,0,30,30);
COMMIT;
