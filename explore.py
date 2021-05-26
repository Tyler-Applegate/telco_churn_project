# This is my explore.py file for Telco Churn Project

# general imports (from big libraries)
import pandas as pd
import numpy as np
import os

# my specific imports
# this brings in my login credentials to the Codeup database
from env import host, user, password
# this gives me access to my acquire functions
import acquire
# this gives me access to my prepare functions
import prepare

########################### fancy function time #########################################

def telco_cat_chi(df):
    '''
    This function is specific to the telco churn project. It takes in either the train, validate, or test df
    and returns chi2 and p values for all categorical variables measures against 'has_churn'.
    '''
    cat_vars = ['senior_citizen', 'auto_pay', 'dsl', 'fiber', 'has_internet', 'm2m', 'one_year',
       'two_year', 'has_contract', 'is_male', 'has_partner', 'has_dep', 'has_phone', 'multi_phone', 'has_security',
       'has_backup', 'has_protection', 'has_support', 'stream_tv',
       'stream_movies', 'has_paperless']
    for cat in cat_vars:
        print(cat)
        observed = pd.crosstab(train['has_churn'], train[cat])
        chi2, p, degf, expected = stats.chi2_contingency(observed)
        print(f'chi^2 = {chi2:.4f}')
        print(f'p     = {p:.4f}')
        print('--------------------------------')



def telco_quant_ttest(df):
    '''
    This function is specific to the telco churn project. It takes in either the train, validate, or test df
    and returns tscore and p/2 values for all continuous variables measures against 'has_churn'.
    '''
    quant_vars = ['monthly_charges', 'total_charges', 'tenure_months']
    for quant in quant_vars:
        churn_rate = df['has_churn'].mean()
        alpha = 0.01
        t, p = stats.ttest_1samp(df[quant], churn_rate)
        print(quant)
        print('tscore:', t.round(2))
        print('p/2:   ', p/2)
        print('alpha: ', alpha)
        print('-------------------------------------')