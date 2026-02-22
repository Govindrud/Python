import os

def main():
    file_name = input("Enter the Name of File : ")      #Demo.txt

    if(os.path.exists(file_name)):
        fobj = open(file_name , "r")
        print(fobj.name)
        print(fobj.mode)
        print(fobj.closed)

        fobj.close()
        print("After fobj.close ",fobj.closed)

       
    else:
        print("there is no such file")
    

if __name__ == "__main__":
    
    main()

  