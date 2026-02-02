
def EmployeeInfo(Name ="Rahul",Age =21, Salary =1000 , City ="Mumbai"):
    print("Name :", Name )
    print("Age :", Age )
    print("Salary :", Salary)
    print("City :", City )

def main():
    #EmployeeInfo(Age=26,Name="Rahul",City="Pune", Salary=None) # Correct
    EmployeeInfo()
    

if __name__ == "__main__":
    main()