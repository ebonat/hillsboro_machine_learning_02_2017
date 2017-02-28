
# Cleaning data in Python 
# http://data.library.utoronto.ca/cleaning-data-python

# http://www.dataquest.io/blog/pandas-python-tutorial/
# Pandas Tutorial: Data analysis with Python: Part 1

# Pandas Tutorial: Data analysis with Python: Part 2
# https://www.dataquest.io/blog/pandas-tutorial-python-2/

# Working with DataFrames
# http://www.gregreda.com/2013/10/26/working-with-pandas-dataframes/

# 10 Minutes to pandas
# http://pandas.pydata.org/pandas-docs/stable/10min.html

# cleaning big data using python - LOOK AT IT - VERY IMPORTANT!
# http://stackoverflow.com/questions/13867294/cleaning-big-data-using-python

# A Complete Tutorial to Learn Data Science with Python from Scratch
# https://www.analyticsvidhya.com/blog/2016/01/complete-tutorial-learn-data-science-python-scratch-2/

# Introduction to Pandas with Practical Examples
# http://pythonforengineers.com/introduction-to-pandas/

# Dropping Rows And Columns In pandas Dataframe 
# http://chrisalbon.com/python/pandas_dropping_column_and_rows.html

# An Introduction to Pandas
# http://synesthesiam.com/posts/an-introduction-to-pandas.html
# VARIABLE DESCRIPTIONS FOR TITANIC CSV FILE
# survival        Survival
#                 (0 = No; 1 = Yes)
# pclass          Passenger Class
#                 (1 = 1st; 2 = 2nd; 3 = 3rd)
# name            Name
# sex             Sex
# age             Age
# sibsp           Number of Siblings/Spouses Aboard
# parch           Number of Parents/Children Aboard
# ticket          Ticket Number
# fare            Passenger Fare
# cabin           Cabin
# embarked        Port of Embarkation
#                 (C = Cherbourg; Q = Queenstown; S = Southampton)

# http://pandas.pydata.org/pandas-docs/stable/dsintro.html
# http://pandas.pydata.org/pandas-docs/stable/missing_data.html#missing-data

import os
import sys
from tabulate import tabulate

import pandas as pd
import numpy as np

import config

def main():
    
#     default project directory path
    project_directory_path = os.path.dirname(sys.argv[0])  

#     titanic data file path
    titanic_data_path = os.path.join(project_directory_path, config.TITANIC_DATA_FILE)  
    
#     import titanic data file
    df_titanic = pd.read_csv(titanic_data_path, sep=",")    
    
#     set a new index to PassengerId column
    df_titanic.set_index("PassengerId", inplace=True)
    print(df_titanic)

if __name__ == '__main__':
    main()