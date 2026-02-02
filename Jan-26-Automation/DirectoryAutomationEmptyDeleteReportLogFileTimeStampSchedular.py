import sys
import os
import time
import schedule

def DirectoryScanner(DirName ="Marvellous"):
    border =("-" * 50)
    timestamp = time.ctime()

    LogfileName = "Marvellous%s.log"%(timestamp)
    LogfileName = LogfileName.replace(" ","_")
    LogfileName = LogfileName.replace(":","_")
    fobj = open(LogfileName,"w")

    fobj.write(border +"\n")
    fobj.write("This is a log file create by Marvellous Automation \n")
    fobj.write("This is a Directory cleaner script \n")
    fobj.write(border +"\n")

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
            
                
            if(os.path.getsize(fname) == 0):  
                EmptyFileCount = EmptyFileCount + 1                
                os.remove(fname)
    fobj.write(border+"\n") 
    fobj.write("Total Files scanned : "+str(FileCount)+"\n")
    fobj.write("Total Empty Files found : "+str(EmptyFileCount)+"\n") 
    fobj.write("This Log file is created at : "+timestamp+"\n")          
    
    print(border+"\n")
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
    
    #DirectoryScanner (sys.argv[1])
    schedule.every(1).minutes.do(DirectoryScanner)
    while True:
        schedule.run_pending()
        time.sleep(1)

    border =("-" * 50)
    print(border)
    print("--------------------Marvellous Automation------------------------")
    print(border)

if __name__ == "__main__":
    main()


    ## Input = & C:/Users/prash/Desktop/Python/Jan-26-Automation/.venv/Scripts/python.exe c:/Users/prash/Desktop/Python/Jan-26-Automation/DirectoryAutomationEmptyDeleteReportLogFileTimeStampSchedular.py Marvellous