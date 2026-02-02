#Procedural Approach- def Keyword (CheckEven)
def CheckEven(No):
    if(No % 2 == 0):
        print("It is Even")
    else:
        print("It is odd")


Value = 0

print("Enter the Number :")
Value = int(input())

CheckEven(Value)

