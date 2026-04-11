import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score , confusion_matrix 



#-------------------------------------------------------------------------------
# Function name : DisplayInfo
# Description : It displays the title of the pag
# Parameters : None
# Return : None
# Date : 14/03/2026
# Author : Govind Anil Rudrawar
#---------------------------------------------------------------------------------
def DisplayInfo(title):
    print("/n" + "=" *70)
    print(title)
    print("=" * 70)
#-------------------------------------------------------------------------------
# Function name : Display Info
# Description : This is Main pipeline Controller 
#                It loads the dataset ,show the raw data
#                It preprocess the dataset and train the model    
# Parameters : Datapath of Dataset File
# Return : None
# Date : 14/03/2026
# Author : Govind Anil Rudrawar
#---------------------------------------------------------------------------------
def ShowData(df,message):
    DisplayInfo(message)
    print("\nFirst Five rows of Dataset")
    print(df.head())
    print("\nShape of Dataset")
    print(df.shape)
    print("\nColumn Names :")
    print(df.columns.tolist())

    print("/nMissing Values in each Columns")
    print(df.columns.isnull().sum())

#-------------------------------------------------------------------------------
# Function name : ShowData
# Description : It shows basic information about dataset
# Parameters : Dataset (df)
#              df -> Pandas Dataframe Object
#              message -> message heading display
# Return : None
# Date : 14/03/2026
# Author : Govind Anil Rudrawar
#---------------------------------------------------------------------------------
def MarvellousTitanicLogistic(Datapath):
    DisplayInfo("Step 1: Loading the Dataset")
    df = pd.read_csv(Datapath)
    ShowData(df,"Initial Dataset")

#-------------------------------------------------------------------------------
# Function name : main
# Description : Starting point of the application
# Parameters : None
# Return : None
# Date : 14/03/2026
# Author : Govind Anil Rudrawar
#---------------------------------------------------------------------------------

def main():
    MarvellousTitanicLogistic("MarvellousTitanicDataset.csv")

if __name__=="__main__":
    main()