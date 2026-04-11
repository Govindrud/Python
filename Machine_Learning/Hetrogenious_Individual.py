from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier

from sklearn.metrics import accuracy_score , confusion_matrix ,classification_report

# Step 1 : Load Dataset 
data = load_breast_cancer()
X = data.data
Y = data.target
print("shape of X :",X.shape)
print("shape of Y :",Y.shape)

# Step 2: Split the Dataset
X_train,X_test,Y_train,Y_test =train_test_split(X,Y,test_size=0.2,random_state=42)

# Step 3 : Create Base Models
model_LR = LogisticRegression(max_iter=5000)
model_DT = DecisionTreeClassifier(random_state=42)
model_KNN =KNeighborsClassifier(n_neighbors=5)

# Step 4 : Train Base Models
model_LR.fit(X_train,Y_train)

model_DT.fit(X_train,Y_train)

model_KNN.fit(X_train,Y_train)

# Step 5: Calculate the Individual Accuracy
Pred_LR = model_LR.predict(X_test)
Pred_DT = model_DT.predict(X_test)
Pred_KNN = model_KNN.predict(X_test)

Accuracy_LR = accuracy_score(Pred_LR,Y_test)

Accuracy_DT = accuracy_score(Pred_DT,Y_test)

Accuracy_KNN = accuracy_score(Pred_KNN,Y_test)

print("Individual Model Accuracy :")
print("Logistic Regression :",Accuracy_LR)
print("Decision Tree :",Accuracy_DT)

print("KNN :",Accuracy_KNN)



# Step 6 : 




