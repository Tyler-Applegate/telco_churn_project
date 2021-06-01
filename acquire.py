# This is my acquire.py file for Telco Churn Project

########################### General Imports ####################################
import pandas as pd
import numpy as np
import os

############### Connection #####################################################

# Enables access to my env.py file in order to use sensitive info to access Codeup DB
from env import host, user, password

# sets up a secure connection to the Codeup db using my login infor
def get_connection(db, user=user, host=host, password=password):
    '''
    This function uses my env file to create a connection url to access
    the Codeup database.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

# This function will connect with the Codeup database to join all tables in the telco db
# to return a pandas DataFrame
def new_telco_data():
    '''
    This function joins the 'customers', 'contract_types', 'internet_service_types', 
    and 'payment_types' tables from the telco_churn db
    and return a pandas DataFrame with all columns/values from all tables.
    '''
    sql_query = '''SELECT * 
                    FROM customers
                    JOIN contract_types USING(contract_type_id)
                    JOIN internet_service_types USING(internet_service_type_id)
                    JOIN payment_types USING(payment_type_id)'''
    return pd.read_sql(sql_query, get_connection('telco_churn'))

# This function plays on top of new_telco_data by 1st looking to see if there is a .csv of the telco Dataframe, and
# creating one if there is not. This optomizes performance/runtime, by only needing to connect to the server 1 time
# and then using a local .csv thereafter
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

def overview(df):
    '''
    This function returns the shape and info of the df. It also includes a breakdown of the number of unique values
    in each column to determine which are categorical/discrete, and which are numerical/continuous. Finally, it returns
    a breakdown of the statistics on all numerica columns.
    '''
    print(f'This dataframe has {df.shape[0]} rows and {df.shape[1]} columns.')
    print('----------------------------------')
    print('')
    print(df.info())
    print('----------------------------------')
    print('')
    print('Unique value counts of each column')
    print('')
    print(df.nunique())
    print('----------------------------------')
    print('')
    print('Stats on Numeric Columns')
    print('')
    print(df.describe())