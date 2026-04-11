#   [A,B,C,D]
# X [1,2,3,5]
# Y [2,3,1,6]
#[Red,Red,Blue,Blue]
#Predict =(3,3)
import numpy as np
import math

def EuclidienDistance(P1,P2):
    Ans = math.sqrt((P1["X"] -P2["X"]) **2 + (P1["Y"] -P2["Y"]) **2)
    return Ans

def MarvellousKNeighbourClassifier():
    border = "-"*40
 
    data =[
        {'point':'A','X' :1 ,'Y':2,'label':'Red'},
        {'point':'B','X' :2 ,'Y':3,'label':'Red'},
        {'point':'C','X' :3 ,'Y':1,'label':'Blue'},
        {'point':'D','X' :5 ,'Y':6,'label':'Blue'}
        ]

    print(border)
    print("Marvellous Userdefined KNN")
    print(border)

    print(border)
    print("Training Data Set")
    print(border)

    for i in data :
        print(i)
    print(border)
    new_point = { 'X':3 , 'Y':3}
    print(new_point)

    Result = EuclidienDistance(data[0],new_point)
    print(Result)

    # calculate all distance 
    for d in data :
        d['distance']= EuclidienDistance(d,new_point)
    print(border)    
    print("Calculated distances are :")
    print(border)
    for d in data :
        print(d)

    sorted_data = sorted(data , key= lambda item : item['distance'])

    for d in sorted_data:
        print(d)

def main():

    MarvellousKNeighbourClassifier()

if __name__ == "__main__":
    main()