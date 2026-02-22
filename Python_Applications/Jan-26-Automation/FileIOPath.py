import os


def main():
    file_name = input("Enter the Name of File : ")

    Ret = os.path.isabs(file_name)

    if(Ret == True):
        print("It is absolute path")
    else:
        print("It is Relative path")


if __name__ == "__main__":
    
    main()

    #Input =  C:\Users\prash\Desktop\Python\Jan-26-Automation\Hello.txt