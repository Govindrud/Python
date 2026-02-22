import os 

def main():

    DirectoryName = input("Enter the name of Directory : ")

    print("Containts of the Directory are : ")

    for FolderName , SubFolderName , FileName in os.walk(DirectoryName ):
        print("Folder Name :", FolderName)

        for subf in SubFolderName : 
            print("Subfolder name :", subf)

        for fname in FileName :
            print("File name :", fname)


if __name__ == "__main__":
    main()