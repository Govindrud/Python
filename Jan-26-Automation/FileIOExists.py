import os


def main():
    file_name = input("Enter the Name of File : ")

    Ret = os.path.exists(file_name)
    

    if Ret == True :
        fobj = open(file_name ,"r")
        print("File gets Successfully Opened")

    else :
        print("There is no such file")


if __name__ == "__main__":
    
    main()

    