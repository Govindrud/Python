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


def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()