# This is my acquire.py file for Telco Churn Project

########################### General Imports ####################################
import pandas as pd
import numpy as np
import os

############### Connection #####################################################

# Enables access to my env.py file in order to use sensitive info to access Codeup DB
from env import host, user, password

# sets up a secure connection to the Codeup db using my login infor
def get_db_url(db, user=user, host=host, password=password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

# assigns the telco_churn url to the variable name 'url' so it can be used in additional functions
url = get_db_url('telco_churn')

def get_connection(db, user=user, host=host, password=password):
    '''
    This function uses my env file to create a connection url to access
    the Codeup database.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def new_telco_data():
    '''
    This function joins the 'customers', 'contract_types', 'internet_service_types', and 'payment_types' tables from the telco_churn db
    and return a pandas DataFrame with all columns/values from all tables.
    '''
    sql_query = '''SELECT * 
                    FROM customers
                    JOIN contract_types USING(contract_type_id)
                    JOIN internet_service_types USING(internet_service_type_id)
                    JOIN payment_types USING(payment_type_id)'''
    return pd.read_sql(sql_query, get_connection('telco_churn'))

def get_telco_data():
    '''
    This function reads in Telco data from Codeup database, writes data to
    a csv file if a local file does not exist, and returns a df.
    '''
    if os.path.isfile('telco_df.csv'):
        
        # If csv file exists read in data from csv file.
        df = pd.read_csv('telco_df.csv', index_col=0)
        
    else:
        
        # Read fresh data from db into a DataFrame
        df = new_telco_data()
        
        # Cache data
        df.to_csv('telco_df.csv')
        
    return df