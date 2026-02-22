#Procedural Approach- def Keyword (CheckEven)

def CheckEven(No):
    if(No % 2 == 0):
        return True
    else:
        return False

def Main():
    Value = 0
    Ret = False

    print("Enter the Number :")
    Value = int(input())

    Ret = CheckEven(Value)

    print(Ret)
    
    
if __name__ == "__main__":
     Main()