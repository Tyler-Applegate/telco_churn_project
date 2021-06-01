# Tyler's Super Successful Telco Churn Project

## Project Summary

### Project Objectives:
> - Deliver a Jupyter Notebook walkthrough (no more than 5 minutes) that gives a high level overview tof my project.
> - Document my planning, process (data aquisition, data preparation, data exploration, data visualizations, statistical testing, modeling, and model evaluation,) as well as all relevent findings and key takeaways from each step.
> - Develop modules (acquire.py, prepare.py, explore.py) to make this process repeatable.
> - Be prepared to answer follow-up questions about my methods, code, findings, model

### Business Goals:
> - Identify at least one key driver of churn in the Telco data set.
> - Build a Machine Learning classification model that outperforms the baseline model to accuractely predict customer churn.
> - Document my process so that it can be presented live, as well as read later like a report.

### Audience:
> - Codeup Data Science (Instructors, Support Staff, and Peers.)

### Deliverables:
> - Final Jupyter Notebook of my report.
> - Live presenation of Jupyter Notebook.
> - All modules required to replicate my project
> - .csv file that documents my predications along side actual values for Telco Churn.
> - All necessary Jupyter Notebooks to document each stage of the DS Pipeline.

### Project Context:
> - The Telco Churn data set came from the Codeup database.

### Data Dictionary:
|Target|Datatype|Definition|
|:-------|:-------|:----------|
|churn|7032 non-null: int64|0:no churn, 1:churn|

### Initial Hypothoses:
> - Hypothosis 1 - We reject the Null Hypothesis
> - $H_0$: There is no difference in churn rate between month-to-month and contracted users
> - $H_a$: There is a statistically significant difference in churn rate between month-to-month and contracted users
> - Hypothosis 2 - We reject the Null Hypothesis
> - $H_0$: Monthly charges have no impact on churn rate (they are independent variables)
> - $H_a$: There is a statistically significant relationship between monthly charges and churn rate

## Executive Summary
> - I found that my Decision Tree and Random Forest models each outperformed my baseline accuracy of 73%
> - The features I chose to focus on were:
>    - m2m
>    - auto-pay
>    - fiber
>    - has internet
>    - monthly charges
> - I chose my Random Forest Classifier because it performed the best on my validate dataset. It also slightly improved accuracy, and greatly improved recall.
> - More time is needed to study why fiber internet users are churning at such a high rate, and how our incentive program(s) is/are working

## Stages of DS Pipeline
Plan -> Data Acquisition -> Data Prep -> Exploratory Analysis -> ML Models -> Delivery

### Planning
- [x] Create README.md with data dictionary, project and business goals, come up with initial hypotheses.
- [x] Acquire data from the Codeup Database and create a series of functions to automate this process. Save the functions in an acquire.py file to import into the Final Report Notebook.
- [x] Clean and prepare data for the first iteration through the pipeline, MVP preparation. Create a series of functions to automate the process, store the functions in a prepare.py module, and prepare data in Final Report Notebook by importing and using the funtions.
- [x]  Clearly define two hypotheses, set an alpha, run the statistical tests needed, reject or fail to reject the Null Hypothesis, and document findings and takeaways.
- [x] Establish a baseline accuracy and document well.
- [x] Train three different classification models.
- [x] Evaluate models on train and validate datasets.
- [x] Choose the model with that performs the best and evaluate that single model on the test dataset.
- [x] Create csv file with the customer id, the probability of the churn, and the model's prediction for churn in my test dataset.
- [x] Document conclusions, takeaways, and next steps in the Final Report Notebook.

### Data Acquistion
- [x] Store functions that are needed to acquire data from the telco_churn database on the Codeup data science database server; make sure the acquire.py module contains the necessary imports to run my code.
- [x] The final function will return a pandas DataFrame.
- [x] Import the acquire function from the acquire.py module and use it to acquire the data in the Final Report Notebook.
- [x] Complete some initial data summarization (`.info()`, `.describe()`, `.value_counts()`, `.nunique()`, ...).

### Data Prep
- [x]  Store functions needed to prepare the telco_churn data; make sure the module contains the necessary imports to run the code. The final function should do the following:
    - Split the data into train/validate/test.
    - Handle any missing values.
    - Handle erroneous data and/or outliers that need addressing.
    - Encode variables as needed.
    - Create any new features, if made for this project.
- [x]  Import the prepare function from the prepare.py module and use it to prepare the data in the Final Report Notebook.

### Exploratory Analysis
- [x] Answer key questions, my hypotheses, and figure out the features that can be used in a classification model to best predict the target variable, churn. 
- [x] Run at least 2 statistical tests in data exploration. Document my hypotheses, set an alpha before running the tests, and document the findings well.
- [x] Create visualizations and run statistical tests that work toward discovering variable relationships (independent with independent and independent with dependent). The goal is to identify features that are related to churn (the target), identify any data integrity issues, and understand 'how the data works'. If there appears to be some sort of interaction or correlation, assume there is no causal relationship and brainstorm (and document) ideas on reasons there could be correlation.
- [x] Summarize my conclusions, provide clear answers to my specific questions, and summarize any takeaways/action plan from the work above.

### ML Models
- [x] Establish a baseline accuracy to determine if having a model is better than no model and train and compare at least 3 different models. Document these steps well.
- [x] Train (fit, transform, evaluate) multiple models, varying the algorithm and/or hyperparameters you use.
- [x] Compare evaluation metrics across all the models you train and select the ones you want to evaluate using your validate dataframe.
- [x] Feature Selection (after initial iteration through pipeline): Are there any variables that seem to provide limited to no additional information? If so, remove them.
- [x] Based on the evaluation of the models using the train and validate datasets, choose the best model to try with the test data, once.
- [x] Test the final model on the out-of-sample data (the testing dataset), summarize the performance, interpret and document the results.

### Delivery
> - Introduce myself and my project goals at the very beginning of my notebook walkthrough.
> - Summarize my findings at the beginning like I would for an Executive Summary. 
> - Walk Codeup Data Science Team through the analysis I did to answer my questions and that lead to my findings. (Visualize relationships and Document takeaways.) 
> - Clearly call out the questions and answers I am analyzing as well as offer insights and recommendations based on my findings.

## How to Reproduce this Project
> - You will need your own env file with credentials for the database, along with these files to recreate my project:
    > - README.md
    > - acquire.py
    > - prepare.py
    > - explore.py
    > - run the final_report.ipynb notebook
