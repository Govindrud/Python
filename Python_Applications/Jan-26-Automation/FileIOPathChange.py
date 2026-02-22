import os


def main():
    file_name = input("Enter the Name of File : ")

    Ret = os.path.isabs(file_name)

    if(Ret == True):
        print("It is absolute path")
    else:
        print("It is Relative path")

        NewPath = os.path.abspath(file_name)                  # Absolute Path 

        print("Updated Path :", NewPath)


if __name__ == "__main__":
    
    main()

   # Input = Hello.txt