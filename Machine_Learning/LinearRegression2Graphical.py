import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def MarvellousPredictor():
    #load the data 
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print("Values of Independent Variables : X -", X)
    print("Values of Independent Variables : Y -", Y)

    mean_X = np.mean(X)
    mean_Y = np.mean(Y)

    print("X_mean is :",mean_X)  #3.0
    print("Y_mean is :",mean_Y)  #3.6

    n = len(X) #5

    # Y = mX + C

    # m = (Sum (X-X_bar) * (Y-Y_bar) ) / (Sum (X - X_bar) **2)

    numerator = 0
    denominator = 0

    for i in range(n):
        numerator = numerator + ((X[i]-mean_X) * (Y[i]-mean_Y))
        denominator = denominator + ((X[i]-mean_X)**2)

    m = numerator / denominator
    print("Slope of line i.e is m :",m)  # 0.4

    C = mean_Y - (m * mean_X)
    print("Y intercept if line i.e C :",C)

    x = np.linspace(1,6,n)
    
    y = C + m*x

    print(y)

    plt.plot(x,y,color='g',label="Regression Line")

    plt.scatter(X,Y,color='r',label="Scanner plot")
    plt.xlabel("X : Independent Variable")
    plt.ylabel("Y: Dependent Variable")


    plt.legend()
    plt.show()

    # Finding the Y_predicted values

    Y_predicted = []
    for i in range(n):
        Values = float(m * X[i] + C)
        Y_predicted.append(Values)
    print("Predicted values in Y are :",Y_predicted)


def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()