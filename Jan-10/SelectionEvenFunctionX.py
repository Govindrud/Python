#Procedural Approach- def Keyword (CheckEven)
def CheckEven(No):
    if(No % 2 == 0):
        print("It is Even")
    else:
        print("It is odd")

def Main():
    Value = 0

    print("Enter the Number :")
    Value = int(input())

    CheckEven(Value)
    
if __name__ == "__main__":
     Main()