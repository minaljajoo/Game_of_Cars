# Use this script isntead of table_maker.py
# This script will create the series table in the database
# and append the data directly to the table. 

import json
import pandas as pd
import datetime as dt

from dateutil import parser #pip install python-dateutil
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import Session
import os
import sys
import datetime


# set environment var
password = os.environ['AWS_CAR_PW']

# AWS connection setup. Declare username and endpoint piece. 
user = 'minalCarData'
endpoint = 'cardb.ci3ptaygzvuw.us-east-2.rds.amazonaws.com'
args = "ssl_ca=../database/config/rds-ca-2015-us-east-2-root.pem"

# AWS username and password. 
rds_connection_string = f"{user}:{password}@{endpoint}/fuel_economy_db?{args}"
engine = create_engine(f'mysql://{rds_connection_string}')

# Connection attachment. 
conn = engine.connect()
Base = declarative_base()



session = Session(engine)


# Create Fuel Class for SQL Database Table
# Object relational mapping for our table
# ----------------------------------
class Fuel(Base):
    __tablename__ = 'fuel'
    id = Column(Integer, primary_key=True)
    year = Column(Integer)
    model = Column(String(255))
    vehicle_class = Column(String(255))
    fuel_type = Column(String(255))
    smog_rating = Column(Integer)
    city_mpg  = Column(Float)
    hwy_mpg  = Column(Float)
    cmb_mpg = Column(Float)
    Greenhouse_gas_score = Column(Integer)
    smartway = Column(String(255))


Base.metadata.create_all(conn)
print("Read the final data from final_mpg")
file_path = '../Resources/final_mpg.csv'
final_mpg_df = pd.read_csv(file_path, index_col=0)
print(final_mpg_df)

c = 0
maxRows = 10000
start_time = datetime.datetime.now()
print(f"Start time: {start_time}")
for index, row in final_mpg_df.iterrows():
    record = Fuel()
   
    record.year = row['year']
    record.model = row['model']
    record.fuel_type = row['fuel_type']
    record.vehicle_class = row['vehicle_class']
    record.smog_rating = row['smog_rating']
    record.city_mpg = row['city_mpg']
    record.hwy_mpg = row['hwy_mpg']
    record.cmb_mpg = row['cmb_mpg']
    record.Greenhouse_gas_score = row['Greenhouse_gas_score']
    record.smartway = row['smartway']
    
    session.add(record)
    session.commit()
    print(c)
    print("Commit to Database!!!!!!!")
    c = c + 1
    if c >= maxRows: break

end_time = datetime.datetime.now()
print(end_time - start_time)


# CREATE DATABASE connection
def create_connection(make_tables=False, folder_helper='../'):
    # set environment var
    password = os.environ['AWS_CAR_PW']
  
   # AWS connection setup. Declare username and endpoint piece. 
    user = 'minalCarData'
    endpoint = 'cardb.ci3ptaygzvuw.us-east-2.rds.amazonaws.com'
    args = f'ssl_ca={folder_helper}database/config/rds-ca-2015-us-east-2-root.pem'

    # AWS username and password. 
    rds_connection_string = f"{user}:{password}@{endpoint}/fuel_economy_db?{args}"
    engine = create_engine(f'mysql://{rds_connection_string}')

    conn = engine.connect()
    if make_tables:
        Base.metadata.create_all(conn)
    
    return conn, Session(engine)






