import pandas as pd

import matplotlib.pylab as plt

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier , plot_tree

from sklearn.metrics import (accuracy_score ,confusion_matrix , classification_report ,ConfusionMatrixDisplay)
#######################################################
#                Step 1 :Load the DataSet
#######################################################

Border = "-"*40
print(Border)
print("Step 1: Load the DataSet")
print(Border)


Datasetpath = "iris.csv"
df = pd.read_csv(Datasetpath)

print("DataSet Gets Loaded Successfully")
print("Initial entries from DataSet")
print(df.head())

#######################################################
#   Step 2 :Data Analysis EDA(Exploretry Data AnAlysis)
#######################################################

Border = "-"*40
print(Border)
print("Step 2: Data Analysis")
print(Border)

print("Shape od DataSet:",df.shape)
print("Column Name :",list(df.columns))

print("Missing Values(Per Column)")
print(df.isnull().sum())

print("Class Distribution (Species Count)")
print(df["variety"].value_counts())
