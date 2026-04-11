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

#######################################################
#   Step 5 : Split the Dataset for training and Testing
#######################################################

Border = "-"*40
print(Border)
print("Step 5 : Split the Dataset for training and Testing")
print(Border)

#Total dataset sixe = 150,5
# X =150,4
# Y = 150,1

# Test size = 20%
# Train size = 80%

X_train ,X_test ,Y_train ,Y_test = train_test_split(
   X,
   Y,
   test_size=0.5,
   random_state=42
)
print("Data Splitting Activity Done")

print("X _ Independent: ",X.shape) #(150,4)
print("Y_Dependent: ",Y.shape) #(150,1)

print("X_train :",X_train.shape) #(120,4)
print("X_test :",X_test.shape) #(30,4)

print("Y_train :",Y_train.shape) #(120,)
print("Y_test :",Y_test.shape) #(30,)

#######################################################
#   Step 6 : Build the Model
#######################################################

Border = "-"*40
print(Border)
print("Step 6: Build the Model")
print(Border)

print("We are going to use the decision tree classifer")

model = DecisionTreeClassifier(
    criterion = "gini",
    max_depth= 4,
    random_state=42,

)
print("Model successfully created :",model)

#######################################################
#   Step 7: Training the Model
#######################################################

Border = "-"*40
print(Border)
print("Step 7: Training the Model")
print(Border)


model.fit(X_train,Y_train)
print("Model training completed")

#######################################################
#   Step 8: Test (Evaluate) the Model
#######################################################

Border = "-"*40
print(Border)
print("Step 7: Test (Evaluate) the Model")
print(Border)

Y_pred = model.predict(X_test)
print("Model Evaluation (testing) complete")

print(Y_pred.shape)

print("Expected answers :")
print(Y_test)

print("Expected answers :")
print(Y_pred)

#######################################################
#   Step 9: Evaluate the Model performance
#######################################################

Border = "-"*40
print(Border)
print("Step 9: Evaluate the Model performance")
print(Border)

Accuracy = accuracy_score(Y_test,Y_pred)
print("Accuracy of the Model is :",Accuracy * 100)

cm = confusion_matrix(Y_test,Y_pred)
print("Confussion matrix :")
print(cm)

print("Classification report ")
print(classification_report(Y_test,Y_pred))

#######################################################
#   Step 10: Plot Confussion Matrix
#######################################################

Border = "-"*40
print(Border)
print("Step 10: Plot Confussion Matrix")
print(Border)

data =ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=model.classes_)
data.plot()
plt.title("Confussion matrix of Iris Dataset")
plt.show()

# Artifical intelligence of modern approch