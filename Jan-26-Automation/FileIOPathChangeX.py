import os

def main():
    file_name = input("Enter the Name of File : ")

    if (os.path.exists(file_name)):

        Ret = os.path.isabs(file_name)

        if(Ret == True):
            print("It is absolute path")

        else:
            print("It is Relative path")

            NewPath = os.path.abspath(file_name)                  # Absolute Path 

            print("Updated Path :", NewPath)
    else:
        print("There is no such file")


if __name__ == "__main__":
    
    main()

   #1. Input = Hello.txt
   #1. Input = Python.txt