import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score , confusion_matrix 



#-------------------------------------------------------------------------------
# Function name : DisplayInfo
# Description : It displays the title of the page
# Parameters : None
# Return : None
# Date : 14/03/2026
# Author : Govind Anil Rudrawar
#---------------------------------------------------------------------------------
def DisplayInfo(title):
    print("\n" + "=" *70)
    print(title)
    print("=" * 70)

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

def ShowData(df,message):
    DisplayInfo(message)
    print("\nFirst Five rows of Dataset")
    print(df.head())
    print("\nShape of Dataset")
    print(df.shape)
    print("\nColumn Names :")
    print(df.columns.tolist())

    print("\nMissing Values in each Columns")
    print(df.columns.isnull().sum())


#-------------------------------------------------------------------------------
# Function name : CleanTitanicData
# Description :   It does preprocessing
#                 It removes unnecessary columns
#                 It converts text data to numeric format
#                 It does encoding to categorical columns
# Parameters : df -> Pandas dataframe
# Return : df -> Clean pandas dataframe
# Date : 14/03/2026
# Author : Govind Anil Rudrawar
#---------------------------------------------------------------------------------
def CleanTitanicData(df):
    DisplayInfo("step 2: Original Data ")
    print(df.head())
    print(df.shape)

    # remove unnecessary Columns
    drop_columns = ["Passengerid","zero","name","Cabin"]
    existing_Columns = [col for col in drop_columns if col in df.columns]

    print("\n Columns to be droped : ")
    print(existing_Columns)

    # drop the unwanted Columns
    df = df.drop(columns=existing_Columns)

    DisplayInfo("step 2: Data after Column Removal")
    print(df.head())
    print(df.shape)

    # Handle Age Column
    if "Age" in df.columns:
        print("Age Column before filling missing values")
        print(df["Age"].head(10))

     # Coerce -->> Invalid Values get coverted as NAN = None
        df["Age"] = pd.to_numeric(df["Age"],errors="coerce")

        age_median = df["Age"].median()

        # Replace the missing values with median
        df["Age"] = df['Age'].fillna(age_median)
        print("\nAge Column after preprocessing")

        print(df["Age"].head(10))

     # Handle Fare column

        if "Fare" in df.columns:
            print("\nFare Column Before Preprocessing")
            print(df["Fare"].head(10))
            df["Fare"] = pd.to_numeric(df["Fare"],errors="coerce")

            Fare_median = df["Fare"].median()

            # Replace the missing values with median
            df["Fare"] = df["Fare"].fillna(Fare_median)
            print("\nFare Column after preprocessing")
            print("\n Median of fare column is :",Fare_median)

            print(df["Fare"].head(10))

         # Handle Embardked Column
        if "Embarked" in df.columns:
            print("\nEmbarked Column Before Preprocessing")
            print(df["Embarked"].head(10))

            # Convert data into string
            df["Embarked"] = df["Embarked"].astype(str).str.strip()

            # remove missing values
            df["Embarked"] = df["Embarked"].replace(['nan','None',''],np.nan)

            # Get most frequent value
            embarked_mode = df["Embarked"].mode([10])
            print("Mode of Embarked Column : ",embarked_mode)

            df["Embarked"] = df["Embarked"].fillna(embarked_mode)
            print("\nEmbarked column after preprocessing :")
            print(df["Embarked"].head(10))

        # Encode Embarked columns into integer
            df = pd.get_dummies(df,columns=["Embarked"],drop_first=True)

            print("\n Data after Encoding")
            print(df.head())


         #Convert boolean columns into integer
            for col in df.columns:
                if df[col].dtype == bool:
                    df[col] =df[col].astype(int)

            print("\n Data after encoding")
            print(df.head())

         # Handle Sex Column
        if "Sex" in df.columns:
            print("\n Sex column Before Preprocessing")
            print(df["Sex"].head(10))
            df["Sex"]= pd.to_numeric(df["Sex"],errors="coerce")

            print("\n Sex column after preprocessing\n",df["Sex"].head(10))

            

    return df


#-------------------------------------------------------------------------------
# Function name : MarvellousTitanicLogistic
# Description : This is Main pipeline Controller 
#                It loads the dataset ,show the raw data
#                It preprocess the dataset and train the model    
# Parameters : Datapath of Dataset File
# Return : None
# Date : 14/03/2026
# Author : Govind Anil Rudrawar
#---------------------------------------------------------------------------------

def MarvellousTitanicLogistic(Datapath):
    DisplayInfo("Step 1: Loading the Dataset")
    df = pd.read_csv(Datapath)
    ShowData(df,"Initial Dataset")
    df = CleanTitanicData(df)

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