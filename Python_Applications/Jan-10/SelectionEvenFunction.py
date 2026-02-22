def CheckEven(No):
    if(No % 2 == 0):
        print("It is Even")
    else:
        print("It is odd")

def Main():
    CheckEven(21)   # Positional Argument
    CheckEven(No=22)  #Keyword Argument

if __name__ == "__main__":
     Main()

    

