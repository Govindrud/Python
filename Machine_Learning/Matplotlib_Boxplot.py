import matplotlib.pyplot as plt
import seaborn as sns


def main():
    #Detecting Outlier  # 110 =  Outlier 
    sns.boxplot(x = [10,20,30,110])       

    plt.show()


if __name__ =="__main__":
    main()