# Importing Dependencies
import pandas as pd
from flask import Flask, render_template, redirect, make_response,request, jsonify
import os
import json
from flask_pymongo import PyMongo
#import scrape_four

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
######################
# Database Setup

#engine = create_engine("sqlite:///static/Resources/ncaa_Rank_Seed2018.sqlite")

# Relect the existing database into a new model.

#Base = automap_base()

# Reflect the table.

#Base.prepare(engine, reflect=True)

# Save a reference to the ranks table as "Ranks".



# Save a reference to the seeds table as "Seed".



# Create our session link from Python to the database.

#session = Session(engine)
######################
# Create an instance of Flask
app = Flask(__name__, static_url_path='/static')



######################
# Route to render index.html
@app.route("/")
def home():

   return render_template("index.html")
#-------------------

# Route to render magic.html: Display the techinical report
@app.route("/magic")
def data():

   return render_template("magic.html")
#--------------------
# Route to render featured.html: display all the plots
@app.route("/featured")
def featured():

   return render_template("featured.html")

#--------------------

# Route to render about.html template using csv data
@app.route("/about")
def about():

   return render_template("about.html")
#--------------------


#--------------------
@app.route("/loan")
def loan():
   return render_template("loan.html")

#--------------------
@app.route("/mpg")
def mpg():
   return render_template("mpg.html")

#--------------------
@app.route("/resale")
def resale():
   return render_template("resale.html")

#--------------------
@app.route("/smartway")
def smartway():
   return render_template("smartway.html")

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



#error handler
@app.errorhandler(404)
def not_found(error):
   return make_response(jsonify({'error': 'Not found'}), 404)

###################### End #########################
if __name__ == "__main__":
    app.run(debug=True)
