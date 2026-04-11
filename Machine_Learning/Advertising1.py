import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def main():
    df = pd.read_csv("Advertising.csv")
    print(df.shape)

    if 'Unnamed: 0'in df.columns:
        df.drop(columns=['Unnamed: 0'], inplace = True)

    print(df.shape)



if __name__ == "__main__":
    main()