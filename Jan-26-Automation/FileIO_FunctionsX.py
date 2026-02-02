import os

def main():
    file_name = input("Enter the Name of File : ")      #Demo.txt

    if(os.path.exists(file_name)):
        fobj = open(file_name ,  "w")
       
        print(fobj.readable())
        print(fobj.writable())
        print(fobj.seekable())
       
    else:
        print("there is no such file")
    

if __name__ == "__main__":
    
    main()

  