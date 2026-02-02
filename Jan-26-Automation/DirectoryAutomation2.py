import sys
import os

def DirectoryScanner(DirName ="Marvellous"):
    Ret = False

    Ret = os.path.exists(DirName)

    if (Ret == False):
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(DirName)
    if (Ret == False):
        print("it is not a Directory")
        return

    for FolderName , SubfolderName , FileName in os.walk(DirName):
        for fname in FileName:
            print("File name :",fname)
            print("File Size :", os.path.getsize(fname))      #Path Issue 

    

def main():
    border =("-" * 50)
    print(border)
    print("--------------------Marvellous Automation------------------------")
    print(border)

    if (len(sys.argv) != 2):
        print("Invalid Number of Argument ")
        print("Please specify the correct name of Directory")
        return
    
    DirectoryScanner (sys.argv[1])
    


if __name__ == "__main__":
    main()