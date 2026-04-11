import pandas as pd
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score ,confusion_matrix , classification_report


def MarvellouClassifier(DataPath):
    border = "-"*66
    print(border)
    print("Step 1 : Load the dataset from CSV file")
    print(border)
    df = pd.read_csv(DataPath)
    print(border)
    print("some entries from the dataset:",df.head())
    print(border)


    #Step 2 : Clean teh dataset by removing the empty rows
    print(border)
    print("Step 2 : Clean teh dataset by removing the empty rows")
    print(border)
    #if 'Unnamed: 0' in columns:
       # df.drop(columns=['Unnamed : 0', inplace= True])
    df.dropna(inplace=True)
    print("Total records :",df.shape[0])
    print("Total columns :",df.shape[1])

    #Step 3 : Seperate the Independent and Dependent Variables 
    print(border)
    print("Step 3 : Seperate the Independent and Dependent Variables")
    print(border)

    X = df.drop(columns=['Class'])
    Y = df['Class']
    
    print('shape of X:',X.shape)
    print('shape of Y:',Y.shape)

    print(border)
    print("Input Columns :",X.columns.to_list())
    print("Output Columns : Class")
    print(border)

def main():
    border = "-"*40
    print(border)
    print("Wine Classifier using KNN")
    print(border)
    MarvellouClassifier(DataPath="WinePredictor.csv")

if __name__ == "__main__":
    main()