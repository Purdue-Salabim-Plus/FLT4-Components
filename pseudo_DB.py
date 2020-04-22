import sqlite3
import pandas as pd
from sqlalchemy import create_engine
from random import randint


def dbCall(testName):
    
    file = r"ProdDatabase.xlsx" # File path to excel file

    engine = create_engine('sqlite://', echo=False) # Jack mentioned saving the DB in RAM? This is where it would happen 

    df = pd.read_excel(file, sheet_name='Sheet1')      # Sheet name in excel file goes here
    df.to_sql('data', engine, if_exists='replace', index=False) 

    # SQL Query goes here:
    result = engine.execute('Select * from data where MethodOfTest="' + testName + '"') 

    final = pd.DataFrame(result, columns=df.columns) # pandas dataframe
    
    if len(final.index) == 0:
        print("No results found when searching for: " + testName)
        sys.exit()
    
    value = randint(0, len(final.index) - 1) # random row number
    return final.loc[value][1]   # Print out/return the time of randomly selected row

