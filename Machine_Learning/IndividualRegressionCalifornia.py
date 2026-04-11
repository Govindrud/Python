import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import BaggingRegressor
from sklearn.metrics import mean_squared_error ,r2_score

#-------------------------------------------------------------
# Step 1 : Load the dataset
#-------------------------------------------------------------

df = pd.read_csv("california_housing.csv")
print("Shape of the dataset :")
print(df.shape)
print("First 5 of the Dataset: ")
print(df.head())

#-------------------------------------------------------------
# Step 2 : Sepearte the Features and Labels
#-------------------------------------------------------------
X= df.drop("target",axis=1)
Y= df["target"]


#-------------------------------------------------------------
# Step 3 :Split dataset for Training and Testing
#-------------------------------------------------------------

X_train , X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)


#-------------------------------------------------------------
# Step 4 :Create Model
#-------------------------------------------------------------

model = DecisionTreeRegressor(random_state=42)




#-------------------------------------------------------------
# Step 5 :Train  Model
#-------------------------------------------------------------

model.fit(X_train,Y_train)


#-------------------------------------------------------------
# Step 6 :Test Model
#-------------------------------------------------------------

Y_pred = model.predict(X_test)


#-------------------------------------------------------------
# Step 7 :Evaluate  Model
#-------------------------------------------------------------

print("Mean_Squared Error :",mean_squared_error(Y_test,Y_pred))
print("R square :",r2_score(Y_test,Y_pred))