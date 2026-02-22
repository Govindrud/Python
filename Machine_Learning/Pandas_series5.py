import pandas as pd

def main():
    Data = [11,21,51,101,111]
 
    sobj = pd.Series([25000,27000,29000,30000],index=["PPA","LB","Python","React"])

    print(sobj)
    print(sobj["Python"])


if __name__ == "__main__":
    main()