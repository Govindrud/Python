import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error , r2_score



def MarvellousAdvetise(Datapath):
    border = "=" * 60
    print(border)
    #------------------------------------------------------------
    # Step 1 : Load Dataset
    #------------------------------------------------------------
    print(border)
    print('Step 1 : Load Dataset')
    print(border)

    df = pd.read_csv(Datapath)
    print("few records from the dataset :")
    print(df.head())
    #------------------------------------------------------------
    # Step 2 : Remove Unwanted Columns
    #------------------------------------------------------------
    print(border)
    print('Step 2 :Remove Unwanted Columns')
    print(border)
    print("Shape of dataset before removal:",df.shape)

    if 'Unnamed: 0' in df.columns:
        df.drop(columns = ['Unnamed: 0'] , inplace = True)
    print("Shape of dataset before removal:",df.shape)


    #------------------------------------------------------------
    # Step 3 :Check missing Values
    #------------------------------------------------------------
    print(border)
    print('Step 3 :Check missing Values')
    print(border)

    print("Missing values colun:", df.isnull().sum())


    #------------------------------------------------------------
    # Step 4 :Display Statistical Summary
    #------------------------------------------------------------
    print(border)
    print('Step  4 :Display Statistical Summary')
    print(border)

    print(df.describe())

    
    #------------------------------------------------------------
    # Step 5: Correlation Between Columns 
    #------------------------------------------------------------
    print(border)
    print('Step  5: Correlation Between Columns')
    print(border)

    print("Correleation Matrix:")
    print(df.corr())
   



def main():
    MarvellousAdvetise(Datapath="Advertising.csv")
    
    
if __name__ == "__main__":
    main()