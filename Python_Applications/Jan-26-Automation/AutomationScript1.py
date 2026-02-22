import sys

def main():

    Border = "-" * 40
    print(Border) 
    print("_____________Marvellous Automation______________")
    print(Border)

    if (len(sys.argv) ==2):
        if((sys.argv[1] == "--h")  or (sys.argv[1]  == "--H")):
            print("This application is use to perform _____")
            print("This is Automation script")

        elif ((sys.argv[1] =="--u") or (sys.argv[1] == "-- U")):
            print("Use the keyword script as ")
            print("scriptName.py Argument1 Argument2 ")
            print("Argument1: ______________ ")
            print("Argument2: ______________ ")

        else:
            print("Use the given flags as:")
            print("--u: Usedto display usage")
            print("--h: Used to display Help")
    else:
        print("Invalid no of command line Arguments ")
        print("Use the given flags as:")
        print("--u: Usedto display usage")
        print("--h: Used to display Help")
        print(Border)
    print(Border)
    print("_______Thank You for using our script______")
    print("_____________Marvellous Automation______________")
    print(Border)
    
        
            
if __name__ == "__main__":
    main()