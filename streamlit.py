import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from config import DB_USER, DB_PASS, DB_ENDPOINT

# SQL Alchemy
from sqlalchemy import create_engine

 # Create Engine
engine = create_engine(f"postgresql://{DB_USER}:{DB_PASS}@{DB_ENDPOINT}")
conn = engine.connect()

# Query All Records in the the Database
data = pd.read_sql("SELECT * FROM historical", conn)

@st.cache
def load_data():
    # read data
    data = pd.read_sql("SELECT * FROM historical", conn)
    return data

df = load_data()
# ethereum_data = df[df["crypto"] == "ethereum_gbp"]

