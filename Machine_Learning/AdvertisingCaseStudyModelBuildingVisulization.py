import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error , r2_score



def MarvellousAdvertise(Datapath):
    border = "=" * 60
    print(border)
    #------------------------------------------------------------
    # Step 1 : Load Dataset
    #------------------------------------------------------------
    print(border)
    print('Step 1 : Load Dataset')
    print(border)

    df = pd.read_csv(Datapath)
    print("few records from the dataset :")
    print(df.head())
    #------------------------------------------------------------
    # Step 2 : Remove Unwanted Columns
    #------------------------------------------------------------
    print(border)
    print('Step 2 :Remove Unwanted Columns')
    print(border)
    print("Shape of dataset before removal:",df.shape)

    if 'Unnamed: 0' in df.columns:
        df.drop(columns = ['Unnamed: 0'] , inplace = True)
    print("Shape of dataset before removal:",df.shape)
    print(border)
    print('clean dataset is: ')
    print(border)
    print(df.head())

    #------------------------------------------------------------
    # Step 3 :Check missing Values
    #------------------------------------------------------------
    print(border)
    print('Step 3 :Check missing Values')
    print(border)

    print("Missing values colun:", df.isnull().sum())


    #------------------------------------------------------------
    # Step 4 :Display Statistical Summary
    #------------------------------------------------------------
    print(border)
    print('Step  4 :Display Statistical Summary')
    print(border)

    print(df.describe())

    
    #------------------------------------------------------------
    # Step 5: Correlation Between Columns 
    #------------------------------------------------------------
    print(border)
    print('Step  5: Correlation Between Columns')
    print(border)

    print("Correleation Matrix:")
    print(df.corr())
    
    #-------------------------------------------------------------------
    # Step 6: Split the Dataset into Independent and Dependent Variables
    #--------------------------------------------------------------------
    print(border)
    print('Step 6: Split the Dataset into Independent and Dependent Variables')
    print(border)  

    X = df[['TV','radio','newspaper']]
    Y = df[['sales']]
    print("Shape of Independent Variables:",X.shape)
    print("Shape of Dependent Variables:",Y.shape)
    
    #-------------------------------------------------------------------
    # Step 7: Split the Dataset for Training and Testing
    #--------------------------------------------------------------------
    print(border)
    print('Step 7: Split the Dataset for Training and Testing')
    print(border) 

    X_train, X_test , Y_train,Y_test = train_test_split(X,Y, test_size=0.2, random_state=42)

    print("X_train shape :",X_train.shape)
    print("Y_train shape :",Y_train.shape)
    print("X_test shape :",X_test.shape)
    print("Y_test shape :",Y_test.shape)

    
    #-------------------------------------------------------------------
    # Step 8 : Create and Train the Model
    #--------------------------------------------------------------------
    print(border)
    print('Step 8 : Create and Train the Model')
    print(border) 

    model = LinearRegression()
    model.fit(X_train,Y_train)

    
    #-------------------------------------------------------------------
    # Step 9: Test the Model
    #--------------------------------------------------------------------
    print(border)
    print('Step 9: Test the Model')
    print(border) 

    Y_pred = model.predict(X_test)

    
    #-------------------------------------------------------------------
    # Step 10: Evaluate the Model
    #--------------------------------------------------------------------
    print(border)
    print('Step 10: Evaluate the Model')
    print(border) 

    #Accuracy = Accuracy()  

    MSE = mean_squared_error(Y_test ,Y_pred)
    RMSE = np.sqrt(MSE)
    R2 = r2_score(Y_test,Y_pred)

    print("Mean Squared Error :",MSE)
    print("Root Mean Squared Error :",RMSE)
    print("R Squared Value :",R2)

    
    #-------------------------------------------------------------------
    # Step 11: Calculate the Model Coefficient 
    #--------------------------------------------------------------------
    print(border)
    print('Step 11: Calculate the Model Coefficient ')
    print(border) 

    for column ,value in zip(X.columns , model.coef_):
        print(f"{column} : {value}")

    print("Intercept :",model.intercept_)

    
    #-------------------------------------------------------------------
    # Step 12: Compare the Actual and Predicted values
    #--------------------------------------------------------------------
    print(border)
    print('Step 12: Compare the Actual and Predicted values')
    print(border) 

   # Result = pd.DataFrame({"Actual sale": Y_test.values, "Predicted sale": Y_pred})
    
    #print(Result.head())

    
    #-------------------------------------------------------------------
    # Step 13: Plot  Actual and Predicted
    #--------------------------------------------------------------------
    print(border)
    print('Step Plot  Actual and Predicted')
    print(border) 

    plt.figure(figsize= (8,5))
    plt.scatter(Y_test,Y_pred)
    plt.xlabel("Actual Sales ")
    plt.ylabel("Predicted Sales")
    plt.title("Actual Sales Vs Predicted Sales")
    plt.grid(True)
    plt.show()

def main():
    MarvellousAdvertise(Datapath="Advertising.csv")
    
    
if __name__ == "__main__":
    main()