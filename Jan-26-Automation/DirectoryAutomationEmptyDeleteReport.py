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
    

    FileCount = 0
    EmptyFileCount = 0


    for FolderName , SubfolderName , FileName in os.walk(DirName):

        for fname in FileName:
            FileCount = FileCount + 1

            fname = os.path.join(FolderName,fname)
            print("File name :",fname)
            print("File Size :", os.path.getsize(fname))  # EmptyFile 
                
            if(os.path.getsize(fname) == 0):  
                EmptyFileCount = EmptyFileCount + 1                
                os.remove(fname)

    border =("-" * 50)
    print(border)
    print("--------------------Automation Report ------------------------")
    print("Total Files Scanned : ",FileCount)
    print("Total Empty File count :",EmptyFileCount)



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


    border =("-" * 50)
    print(border)
    print("--------------------Marvellous Automation------------------------")
    print(border)

if __name__ == "__main__":
    main()