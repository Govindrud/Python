#Command Line Input

import psutil
import sys
import os


def CreateLog(Foldername):

    Ret = os.path.exists(Foldername)

    if(Ret == True):
        Ret = os.path.isdir(Foldername)
        if (Ret == False):
            print("Unable to create folder")
            return
        
    else:
        os.mkdir(Foldername)
        print("Directory for log files gets created successfully")


def main():
    Border = " - " *50
    print(Border)
    print("______________________Marvellous Platform Survellance System_________________________")
    print(Border)
    
    
    if(len(sys.argv) == 2):
        if(sys.argv[1]== "--h" or sys.argv[1] =="--H"):
            print("This script is used to :")
            print("1 : Create the automatic logs ")
            print("2: Execute perodically")
            print("3: Sends mail witht the logs")
            print("4: Stores information about process")
            print("5: Stores information about CPU")
            print("6: Stores information about RAM usage")
            print("7: Stores information about Secondary Storage")
        
        
        
        elif(sys.argv[1]== "--u" or sys.argv[1] =="--U"):
            print("Use the aurtomation script as")
            print("ScriptName.py Timeintervel DirectoryName")
            print("TimeIntervel : The time in minutes for perodic scheduling")
            print("DirectoryNAme: Name of the directory to create auto logs")


        else:
            print("Unable to process as there is non such option")
            print("Please use --h or --u to get more details")


    # Python Demo.py 5 Marvellous
    elif(len(sys.argv) == 3):
        print("Inside Projects Logic")
        print("Time Intervel :",sys.argv[1])
        print("DirectoryName  :",sys.argv[2])
        CreateLog(sys.argv[2])

    else:
        print("Invalid Number of CommandLine Arguments")
        print("Unable to process as there is non such option")
        print("Please use --h or --u to get more details")


    print(Border)
    print("_________________________ThankYou for Using our Script__________________________________")
    print(Border)
    
if __name__=="__main__":
    main()