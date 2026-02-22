import pandas as pd

def main():
    Data = [11,21,51,101,111]
 
    sobj = pd.Series([11.0,21.0,51.0,101.0,111.0],index=[5,6,7,8,9])

    print(sobj)
    print(sobj[7])


if __name__ == "__main__":
    main()