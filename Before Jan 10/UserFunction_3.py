def multiplication(Value1 , Value2):
    Ans=0  #Local Variable
    Ans=Value1*Value2
    return Ans


#Global Variable
No1 = 0
No2 = 0
Result = 0

No1 = int(input("Enter the first number: "))
No2 = int(input("Enyer the Second number: "))


Result =multiplication(No1,No2)
print("Multipliaction is :" , Result)

####################################

No1 = int(input("Enter the first number: "))
No2 = int(input("Enyer the Second number: "))


Result = multiplication(No1,No2)
print("Multipliaction is :" , Result)