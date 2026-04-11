import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
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
    
if __name__ == "__main__":
    main()