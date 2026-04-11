import pandas as pd
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score ,confusion_matrix , classification_report
from sklearn.preprocessing import StandardScaler


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

    
    #Step 4 : Split the Dataset for Training and Testing 
    print(border)
    print("Step 4 : Split the Dataset for Training and Testing ")
    print(border)
    X_train ,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42 ,stratify=Y)

    print(border)
    print("Information on  Training and Testing Data")
    print("X_train shape:",X_train.shape)
    print("X_test shape:",X_test.shape)
    print("Y_train shape:",Y_train.shape)
    print("Y_test shape:",Y_test.shape)
    print(border)

    # Step 5 : Feature Scaling
    print(border)
    print("Step 5 : Feature Scaling ")
    print(border) 

    scalar = StandardScaler()
    # Independent Variable Scaling
    X_train_Scaled = scalar.fit_transform(X_train)
    X_test_Scaled = scalar.fit_transform(X_test)

    print("Fearure Scaling is Done")

    # Step 6: Explore the Multiple values of K
    print(border)
    print("Step 6: Explore the Multiple values of K")
    print(border) 
    # Hyper Parameter Tunning (K)

    accuracy_scores = []
    K_values = range(1,21)

    for K in K_values:
        model = KNeighborsClassifier(n_neighbors=K)
        model.fit(X_train_Scaled,Y_train)
        Y_pred= model.predict(X_test_Scaled)
        accuracy = accuracy_score(Y_test,Y_pred)
        accuracy_scores.append(accuracy)

    print(border)
    print("Accuracy report of all K values from 1 to 20")
    for values in accuracy_scores:
        print(values)
    
    print(border)
    
    # Step 7: Plot graph of K Vs Accuracy
    print(border)
    print("Step 7: Plot graph of K Vs Accuracy")
    print(border) 
    plt.figure(figsize=(8,5))
    plt.plot(K_values,accuracy_scores,marker ='o')
    plt.title("K values Vs Accuracy")
    plt.xlabel("Values of K")
    plt.ylabel("Accuracy")
    plt.grid(True)
    plt.xticks(list(K_values))
    plt.show()

def main():
    border = "-"*40
    print(border)
    print("Wine Classifier using KNN")
    print(border)
    MarvellouClassifier(DataPath="WinePredictor.csv")

if __name__ == "__main__":
    main()