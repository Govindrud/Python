import os

def main():
    file_name = input("Enter the Name of File : ")

    if(os.path.exists(file_name)):
        os.remove(file_name)
        print("the file gets deleted")
  
    else:
        print("there is no such file")
    

if __name__ == "__main__":
    
    main()

  