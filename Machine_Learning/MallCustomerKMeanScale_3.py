import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def main():
    #_------------------------------------------------------
    # Step 1 : Load the Dataset
    #-------------------------------------------------------
    print("Step 1 : Load the Dataset")
    df=pd.read_csv("Mall_Customers.csv")

    print("First few records:")
    print(df.head())

    print("Shape of Dataset:")
    print(df.shape)

    print("Missing values :")
    print(df.isnull().sum())
    #_------------------------------------------------------
    # Step 2 : Select Features
    #-------------------------------------------------------
    print("Step 2 : Select Features")

    X =df[["AnnualIncome","SpendingScore"]]
    print("Selected Features :")
    print(X.head())
    print("Shape of Selected features:")
    print(X.shape)

    #_------------------------------------------------------
    # Step 3: Scale the Data
    #-------------------------------------------------------
    scalar = StandardScaler()
    X_scaled =scalar.fit_transform(X)




if __name__ == "__main__":
    main()