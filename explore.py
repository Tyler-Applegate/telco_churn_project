# This is my explore.py file for Telco Churn Project

# general imports (from big libraries)
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from IPython.display import display, display_html 

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
        observed = pd.crosstab(df['has_churn'], df[cat])
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

def telco_melt(df):
    '''
    This function will take in the cleaned/prepped/split telco_train and return a melted
    dataframe of all numerical/continuous variables (except for total_charges)
    '''
#     melts the data into 3 cols (has_churn, measurement, value)
# has_churn=[1,0]
# measurement=['monthly_charges', 'tenure_months']
# value = specific numerical value of each measurement
    df = df[['has_churn', 'monthly_charges', 'tenure_months']].melt(id_vars = ['has_churn'],
                         var_name = 'measurement',
                         value_name = 'value')
    return df

def telco_strip(df):
    '''
    takes in my melted telco_train df and returns a swarm plot of all numerical/
    continuous variables on the x-axis, with the value on the y-axis, and
    includes a color hue to distinguish between churn vs no churn
    '''
    plt.figure(figsize=(8,6))
    plt.title('Stripplot of monthly_charges and tenure_months w/ has_churn hue')
    p = sns.stripplot(
    x='measurement',
    y='value',
    hue='has_churn',
    data=df,
    jitter=1,
    )
    p.set(xlabel='variable')
    return plt.show()

def model_performs (X_df, y_df, model):
    '''
    Take in a X_df, y_df and model  and fit the model , make a prediction, calculate score (accuracy), 
    confusion matrix, rates, clasification report.
    X_df: train, validate or  test. Select one
    y_df: it has to be the same as X_df.
    model: name of your model that you prevously created 
    
    Example:
    mmodel_performs (X_train, y_train, model1)
    '''
    # create the model
    #model = DecisionTreeClassifier(max_depth=None, max_features=None, random_state=None )

    # fit the model
    #model.fit(X_df, y_df)

    #prediction
    pred = model.predict(X_df)

    #score = accuracy
    acc = model.score(X_df, y_df)

    #conf Matrix
    conf = confusion_matrix(y_df, pred)
    mat =  pd.DataFrame ((confusion_matrix(y_df, pred )),index = ['actual_no_churn','actual_churn'], columns =['pred_no_churn','pred_churn'])
    rubric_df = pd.DataFrame([['TN', 'FP'], ['FN', 'TP']], columns=mat.columns, index=mat.index)
    cf = rubric_df + ': ' + mat.values.astype(str)

    #assign the values
    tp = conf[1,1]
    fp =conf[0,1] 
    fn= conf[1,0]
    tn =conf[0,0]

    #calculate the rate
    tpr = tp/(tp+fn)
    fpr = fp/(fp+tn)
    tnr = tn/(tn+fp)
    fnr = fn/(fn+tp)

    #classification report
    clas_rep =pd.DataFrame(classification_report(y_df, pred, output_dict=True)).T
    clas_rep.rename(index={'0': "no_churn", '1': "churn"}, inplace = True)
    print(f'''
    Overall Accuracy:  {acc:.2%}

    True Positive Rate:  {tpr:.2%}  
    True Negative Rate:  {tnr:.2%}   
    False Positive Rate:  {fpr:.2%}
    False Negative Rate:  {fnr:.2%}

    ---------------------------------------------------
    ''')
    print('''
    Positive =  'Churn'

    Confusion Matrix:
    ''')
    display(cf)
    print('''

    
    ---------------------------------------------------
    Classification Report:
    ''')
    display(clas_rep)

def compare (model1, model2, X_df,y_df):
    '''
    Take in a X_df, y_df and model  and fit the model , make a prediction, calculate score (accuracy), 
    confusion matrix, rates, clasification report.
    X_df: train, validate or  test. Select one
    y_df: it has to be the same as X_df.
    model: name of your model that you prevously created 
    
    Example:
    mmodel_performs (X_train, y_train, model1)
    '''
    

    #prediction
    pred1 = model1.predict(X_df)
    pred2 = model2.predict(X_df)

    #score = accuracy
    acc1 = model1.score(X_df, y_df)
    acc2 = model2.score(X_df, y_df)


    #conf Matrix
    #model 1
    conf1 = confusion_matrix(y_df, pred1)
    mat1 =  pd.DataFrame ((confusion_matrix(y_df, pred1 )),index = ['actual_no_churn','actual_churn'], columns =['pred_no_churn','pred_churn'])
    rubric_df = pd.DataFrame([['TN', 'FP'], ['FN', 'TP']], columns=mat1.columns, index=mat1.index)
    cf1 = rubric_df + ': ' + mat1.values.astype(str)
    
    #model2
    conf2 = confusion_matrix(y_df, pred2)
    mat2 =  pd.DataFrame ((confusion_matrix(y_df, pred2 )),index = ['actual_no_churn','actual_churn'], columns =['pred_no_churn','pred_churn'])
    cf2 = rubric_df + ': ' + mat2.values.astype(str)
    #model 1
    #assign the values
    tp = conf1[1,1]
    fp =conf1[0,1] 
    fn= conf1[1,0]
    tn =conf1[0,0]

    #calculate the rate
    tpr1 = tp/(tp+fn)
    fpr1 = fp/(fp+tn)
    tnr1 = tn/(tn+fp)
    fnr1 = fn/(fn+tp)

    #model 2
    #assign the values
    tp = conf2[1,1]
    fp =conf2[0,1] 
    fn= conf2[1,0]
    tn =conf2[0,0]

    #calculate the rate
    tpr2 = tp/(tp+fn)
    fpr2 = fp/(fp+tn)
    tnr2 = tn/(tn+fp)
    fnr2 = fn/(fn+tp)

    #classification report
    #model1
    clas_rep1 =pd.DataFrame(classification_report(y_df, pred1, output_dict=True)).T
    clas_rep1.rename(index={'0': "no_churn", '1': "churn"}, inplace = True)

    #model2
    clas_rep2 =pd.DataFrame(classification_report(y_df, pred2, output_dict=True)).T
    clas_rep2.rename(index={'0': "no_churn", '1': "churn"}, inplace = True)
    print(f'''
    ******       Model 1  ******                                ******     Model 2  ****** 
       Overall Accuracy:  {acc1:.2%}              |                Overall Accuracy:  {acc2:.2%}  
                                                
     True Positive Rate:  {tpr1:.2%}              |          The True Positive Rate:  {tpr2:.2%}  
    False Positive Rate:  {fpr1:.2%}              |         The False Positive Rate:  {fpr2:.2%} 
     True Negative Rate:  {tnr1:.2%}              |          The True Negative Rate:  {tnr2:.2%} 
    False Negative Rate:  {fnr1:.2%}              |         The False Negative Rate:  {fnr2:.2%}

    _____________________________________________________________________________________________________________
    ''')
    print('''
    Positive =  'Churn'

    Confusion Matrix
    ''')
    conf_1_styler = cf1.style.set_table_attributes("style='display:inline'").set_caption('Model 1 Confusion Matrix')
    conf_2_styler = cf2.style.set_table_attributes("style='display:inline'").set_caption('Model 2 Confusion Matrix')
    space = "\xa0" * 20
    display_html(conf_1_styler._repr_html_()+ space  + conf_2_styler._repr_html_(), raw=True)
    print('''

    ________________________________________________________________________________
    
    Classification Report:
    ''')
    clas_rep1_styler = clas_rep1.style.set_table_attributes("style='display:inline'").set_caption('Model 1 Classification Report')
    clas_rep2_styler = clas_rep2.style.set_table_attributes("style='display:inline'").set_caption('Model 2 Classification Report')
    space = "\xa0" * 20
    display_html(clas_rep1_styler._repr_html_()+ space  + clas_rep2_styler._repr_html_(), raw=True)