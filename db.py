# Import Flask
from os import replace
from flask import Flask, jsonify, render_template, redirect
# Import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import Session
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.ext.automap import automap_base
# Import data collection needs
import sqlite3 as sql
import pandas as pd
from historical_api import historical_api_call
from historical_hist_api import historical_hist_api_call
#from historical_api import shortinterval_api_call
# binance
from binance.client import Client
import config
# Other libraries
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
# pip install APScheduler 
import time
import atexit
from apscheduler.schedulers.background import BackgroundScheduler
import websocket, json
# from live_update import dict_cryptoinfon


# Set binance connection
client = Client(config.API_KEY, config.API_SECRET)

## Database
engine = create_engine(config.DB_PATH)

# Collect kline data
historical_df = historical_api_call()
historical_df.to_sql('historical', con=engine, if_exists='replace')
