import requests
import time
import logging
import sqlalchemy
# start an engine
engine = sqlalchemy.create_engine('postgresql://postgres:1234@pgdb:5432/postgres')

# create a table
create_query = '''
CREATE TABLE IF NOT EXISTS luftdaten (
    timestamp TIMESTAMP,
    pm25 REAL,
    pm10 REAL,
    lon TEXT,
    lat VARCHAR(50)
);
'''
engine.execute(create_query)
# if new table comes in, insert into the table.



SENSOR_URL = "http://api.luftdaten.info/static/v1/sensor/{}/"


def pick_luftdaten_values(sensor_id):
    result = requests.get(SENSOR_URL.format(sensor_id))
    data = result.json()
    time_stamp = data[0]['timestamp']
    PM25 = data[0]['sensordatavalues'][1]['value']
    PM10 = data[0]['sensordatavalues'][0]['value']
    lat = data[0]['location']['latitude']
    lon = data[0]['location']['longitude']
    return time_stamp, PM25, PM10, lat, lon 


if __name__ == '__main__':
    sensor_id = 37927
    while True: 
        time_stamp, PM25, PM10, lat, lon = pick_luftdaten_values(sensor_id)
        logging.critical('INCOMING NEW DATA!')
        logging.critical(f'Air quality data at {time_stamp}: PM2.5 = {PM25}, PM10 = {PM10}')
        engine.execute(f'''INSERT INTO luftdaten VALUES('{time_stamp}'
        ,'{PM25}',
        '{lat}',
        '{lon}',
        '{lat}')''')
        time.sleep(10)