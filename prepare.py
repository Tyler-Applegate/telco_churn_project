# This is my prepare.py file for my Telco Churn Project

# necessary imports for my functions to run properly
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from env import host, user, password

def prep_1_telco(df):
    '''
    This function will take in my freshly acquired telco_df and generate new columns with numerical values
    of all object columns, as well as any column that has multiple variables (like 0, 1, or multiple.)
    This function intentionally keeps all old columns so that I can compare to ensure data integrity.
    It will also reset the index to 'customer_id' and drop the 11 values that have a missing 'total_charge'
    since they are brand new customers who are yet to receive a bill.

    '''
    # create reusable dictionary for replacing 'No', 'Yes', 'No internet service', 'No phone service'
    rep_dict = {'No': 0, 'Yes': 1, 'No internet service': 0, 'No phone service': 0}
    # reset the customer_id to be the index
    df = df.set_index('customer_id')
    # This replaces empty cells with nan (null values)
    df = df.replace(' ', np.nan)
    # drop the nulls...
    df = df.dropna(axis=0)
    # convert payment types to 1:auto-pay, 0:not auto-pay
    df['auto_pay'] = df['payment_type_id'].replace({1:0, 2:0, 3:1, 4:1})
    # create DSL column where 1:has DSL, 0:No DSL
    df['dsl'] = df['internet_service_type_id'].replace({1:1, 2:0, 3:0})
    # create Fiber column where 1:has Fiber service, 0:No Fiber
    df['fiber'] = df['internet_service_type_id'].replace({1:0, 2:1, 3:0})
    # create Has Internet column where 1:Has Internet 0:No internet service
    df['has_internet'] = df['internet_service_type_id'].replace({1:1, 2:1, 3:0})
    # separte contract_type_id into three columns...
    # create m2m column where 1:Month-to-Month service, 2:contract
    df['m2m'] = df['contract_type_id'].replace({1:1, 2:0, 3:0})
    # create one_year column where 1:One year contract, 0:no contract, or m2m
    df['one_year'] = df['contract_type_id'].replace({1:0, 2:1, 3:0})
    # create teo_year column where 1:two year contract, 0:less than 2 year contract
    df['two_year'] = df['contract_type_id'].replace({1:0, 2:0, 3:1})
    # create has contract column where 1:has contract, 0:no contract
    df['has_contract'] = df['contract_type_id'].replace({1:0, 2:1, 3:1})
    # create column to convert gender to int 1:male, 0:female
    df['is_male'] = df['gender'].replace({'Male':1, 'Female':0})
    # create has_partner column where 1:has partner, 0:no partner
    df['has_partner'] = df['partner'].replace(rep_dict)
    # create has_dep column where 1:has dependents, 0:no dependents
    df['has_dep'] = df['dependents'].replace(rep_dict)
    # better identify tenure in months by renaming column...
    df['tenure_months'] = df['tenure']
    # create has_phone column where 1:has phone, 0:no phone
    df['has_phone'] = df['phone_service'].replace(rep_dict)
    # create multi_phone column where 1:multiple phone lines, 0:One or fewer phone lines
    df['multi_phone'] = df['multiple_lines'].replace(rep_dict)
    # create security column where 1:has online security, 2:no security
    df['has_security'] = df['online_security'].replace(rep_dict)
    # create has_backup column where 1:has online backup, 0:no backup
    df['has_backup'] = df['online_backup'].replace(rep_dict)
    # create has_protection column where 1:has device protection, 0:no device protection
    df['has_protection'] = df['device_protection'].replace(rep_dict)
    # create has_support column where 1:has tech support, 0:no tech support
    df['has_support'] = df['tech_support'].replace(rep_dict)
    # create stream_tv column where 1:streams tv, 0:no streaming tv
    df['stream_tv'] = df['streaming_tv'].replace(rep_dict)
    # create stream_movies column where 1:streams movies, 0:no streaming movies
    df['stream_movies'] = df['streaming_movies'].replace(rep_dict)
    # create has_paperless column where 1:has paperless billing, 0:no paperless billing
    df['has_paperless'] = df['paperless_billing'].replace(rep_dict)
    # convert total_charges to float
    df['total_charges'] = df['total_charges'].astype(float)
    # create has_churn column where 1:has churn, 0:no churn
    df['has_churn'] = df['churn'].replace(rep_dict)

    return df

def prep_2_telco(df):
    '''
    This function will take in my wide telco DataFrame, and drop all object
    columns, as well as all integer columns that had more than 2 responses,
    and were converted into multiple columns in prep_1_telco.
    A list of those colums will be 
    '''

    # all object columns in a variable to drop
    obj_cols = list(df.select_dtypes('object').columns)
    # other columns to drop...
    other_drops = ['payment_type_id', 'internet_service_type_id', 'contract_type_id', 'tenure']
    # combine all drops into 1 list
    all_drops = obj_cols + other_drops
    # create new dataframe that has been cleaned up
    df_1 = df.drop(columns=all_drops)

    return df_1


def split_data(df):
    '''
    take in a DataFrame and return train, validate, and test DataFrames; stratify on has_churn.
    return train, validate, test DataFrames.
    '''
    train_validate, test = train_test_split(df, test_size=.2, random_state=1221, stratify=df.has_churn)
    train, validate = train_test_split(train_validate, 
                                       test_size=.3, 
                                       random_state=1221, 
                                       stratify=train_validate.has_churn)
    return train, validate, test