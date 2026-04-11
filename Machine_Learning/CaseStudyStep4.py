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

print("Satsticial report  of the Dataset")
print(df.describe())

#######################################################
#   Step 3 : Decide Independent and Dependent Variable
#######################################################

Border = "-"*40
print(Border)
print("Step 3 : Decide Independent and Dependent Variable")
print(Border)

# X : Independent Variable / Features
# Y : Dependent Variables / Labels

feature_cols = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)"
]
X = df[feature_cols]
Y = df ["variety"]

print("X shape:",X.shape)
print("Y shape :",Y.shape)

#######################################################
#   Step 4 : Visualization of DataSet
#######################################################

Border = "-"*40
print(Border)
print("Step 4 : Visualization of DataSet")
print(Border)

plt.figure(figsize=(7,5))

for sp in df["variety"].unique():
    temp = df[df["variety"] == sp]
    plt.scatter(temp["petal length (cm)"],temp["petal width (cm)"],label =sp)

plt.title("Iris : Petal length(cm) vs Petal width(cm)")

plt.xlabel("petal length (cm)")
plt.xlabel("petal width (cm)")
plt.legend()
plt.grid(True)
plt.show()
