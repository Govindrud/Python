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
    print("Step 3: Scale the Data")
    scalar = StandardScaler()
    X_scaled =scalar.fit_transform(X)


    #_------------------------------------------------------
    # Step 4: Elbow Method
    #-------------------------------------------------------
    print("Step 4: Elbow Method")
    # With in Cluster sum of squares = WCSS
    WCSS =[]
    for i in range(1,11):
        model = KMeans(n_clusters=i,random_state=42,n_init=10)
        model.fit(X_scaled)
        WCSS.append(model.inertia_)
    
    plt.figure(figsize=(8,5))
    plt.plot(range(1,11),WCSS ,marker ='o')
    plt.xlabel("Number of clusters")
    plt.ylabel("WCSS")
    plt.title("Elbow method")
    plt.grid(True)
    plt.show()


    #_------------------------------------------------------
    # Step 5: Train the Model
    #-------------------------------------------------------
    model = KMeans(n_clusters=4 ,random_state=42,n_init=10)
    clusters = model.fit_predict(X_scaled)
    df["Cluster"] = clusters
    print("Dataset with clusters")
    print(df.head(30))

if __name__ == "__main__":
    main()