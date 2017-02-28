
import os
import sys
import datetime
from tabulate import tabulate

import pandas as pd
import numpy as np

import config

def main():
    #     default project directory path
    project_directory_path = os.path.dirname(sys.argv[0])  

#     test missing data file path
    missing_data_path = os.path.join(project_directory_path, config.TEST_MISSING_DATA)  
    
#     test data no missing file path
    no_missing_data_path = os.path.join(project_directory_path, config.TEST_NO_MISSING_DATA)  
    
#     1. IMPORT TITANIC DATA FILE
    df_missing_data = pd.read_csv(missing_data_path, sep=",")    
    print(df_missing_data)    
#     print(tabulate(df_missing_data, headers='keys', tablefmt='rst'))
    
#     2. GET NUMBER OF ROWS AND COLUMNS
    result = df_missing_data.shape
    print(result)
    
#     3. GET INDEX, DATATYPE AND MEMORY INFORMATION
    result = df_missing_data.info()
    print(result)
    
#     4. REMOVE DUPLICATES ROWS
#     identify which observations are duplicates
    result = df_missing_data.duplicated()
    print(result)   
    
#     drop duplicates for all columns and keep first
#     inplace : boolean, default False. Modify the DataFrame in place (do not create a new object)
    result = df_missing_data.drop_duplicates(keep = "first", inplace = True)
    print(result)
    
#     drop duplicates for column "one" and keep first
#     result = df_missing_data.drop_duplicates(["one"], keep = "first")
#     print(result)
    
#     drop duplicates for all columns and keep nothing
#     result = df_missing_data.drop_duplicates(keep=False)    
#     print(result)
    
#     5. FILL NAN VALUES (MEAN, MEDIAN, DEFAULTS, ETC)
    result = df_missing_data.fillna(df_missing_data.mean()["one":"two"], inplace = True)
    print(result)
    
    result = df_missing_data.fillna(df_missing_data.median()[:"three"], inplace = True)
    print(result)
   
    df_missing_data["four"] = df_missing_data["four"].fillna("club")
    print(df_missing_data)        
    
    df_missing_data["five"] = df_missing_data["five"].fillna(True)
    print(df_missing_data)     
        
    now = datetime.datetime.now().strftime('%m/%d/%Y')
    df_missing_data["timestamp"] = df_missing_data["timestamp"].fillna(str(now))
    print(df_missing_data)     
    
#     6. REMOVE ROWS BY COLUMNS CONDITIONS
    df_missing_data = df_missing_data[(df_missing_data["four"] == "bar") | (df_missing_data["four"] == "club")]
    print(df_missing_data)
    
    df_missing_data.set_index("one", inplace=True)
    df_missing_data.to_csv(no_missing_data_path)
        
if __name__ == '__main__':
    main()