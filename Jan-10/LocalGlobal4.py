No = 11    # Global

def Fun():   #Local
    global No 
    print("Value of No from Fun is :", No) #11
    No = No +1 
    print("Value of No From Fun is  :", No) #12

print("Value of No is : ", No)   #11
Fun()
print("The value of no is :" , No)  #12

