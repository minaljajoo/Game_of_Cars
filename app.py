# Importing Dependencies
import pandas as pd
from flask import Flask, render_template, redirect, make_response,request, jsonify
import os
import json

from sqlalchemy.pool import StaticPool
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import pickle

import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
######################
# Database Setup
# Web sites use threads, but sqlite is not thread-safe.
# These parameters will let us get around it.
# However, it is recommended you create a new Engine, Base, and Session
#   for each thread (each route call gets its own thread)
engine = create_engine("sqlite:///static/Resources/fuel_economy.sqlite",
    connect_args={'check_same_thread':False},
    poolclass=StaticPool)
#################################################
conn = engine.connect()

# Relect the existing database into a new model.

Base = automap_base()

# Reflect the table.

Base.prepare(engine, reflect=True)

# Save a reference to the car table as "Car".

Car = Base.classes.car
CarValidate = Base.classes.carvalidate
Train = Base.classes.train
Test = Base.classes.test




# Create our session link from Python to the database.

session = Session(engine)
######################
# Create an instance of Flask
app = Flask(__name__)



######################
# Route to render index.html
@app.route("/")
def home():

   return render_template("index.html")
#-------------------

# Route to render magic.html: Display the techinical report
@app.route("/magic")
def magic():


    return render_template("magic.html")
#--------------------
# Route to render featured.html: display all the plots
@app.route("/prediction")
def prediction():

    prediction_smartway = smartway_model()
    prediction_mpg = pd.read_csv('Model/pred_mpg_tf.csv')
    print(prediction_mpg)
    return(jsonify({'smartway prediction': prediction_smartway
    }))

#--------------------

# Route to render about.html template using csv data
@app.route("/about")
def about():

    return render_template("about.html")
#--------------------
@app.route("/smartway")
def smartway():
    return render_template("smartway.html")
#--------------------s
@app.route("/loan")
def loan():
    return render_template("loan.html")
#--------------------
@app.route("/resale")
def resale():
    return render_template("resale.html")

#--------------------
@app.route("/mpg")
def mpg():
    return render_template("mpg.html")
#--------------------
@app.route("/loan_amir")
def loan_amir():
   return render_template("loan_amir.html")

#--------------------
@app.route("/loan_sarah")
def loan_sarah():
   return render_template("loan_sarah.html")
#--------------------
@app.route("/loan_nadia")
def loan_nadia():
   return render_template("loan_nadia.html")

#--------------------
@app.route("/loan_dan")
def loan_dan():
   return render_template("loan_dan.html")


#--------------------
def smartway_model():
    filename_smartway = 'Model/finalized_smartway_model_KN.sav'
    # load the model from disk
    loaded_model_smartway  = pickle.load(open(filename_smartway , 'rb'))
    smartway_new_df = pd.read_sql_query("SELECT * FROM test",conn)
    newX_smartway  =  smartway_new_df.drop(['id','smartway'], axis=1)
    newy_smartway  =  smartway_new_df['smartway']
    print(newy_smartway )
    result_smartway  = loaded_model_smartway.score(newX_smartway, newy_smartway)
    ynew_smartway  = loaded_model_smartway.predict(newX_smartway).tolist()
    return ynew_smartway 
    

###################### End #########################
if __name__ == "__main__":
    app.run(debug=True)
