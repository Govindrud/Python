import sys
import os
import time
import schedule
import shutil
import hashlib

def calculate_hash(path):
    hobj = hashlib.md5()

    fobj = open(path , "rb")

    while True :
        data = fobj.read(1024)
        if not data:
            break
        else:
            hobj.update(data)
    fobj.close()
    return hobj.hexdigest()


def BackupFiles(Source,Destination):
    Copied_Files = []

    print("Creating the Backup folder for Backup process")

    os.makedirs(Destination,exist_ok=True)   # If Folder exists then No error 
     
    for root,dirs,files in os.walk(Source):
        for file in files :
            src_path = os.path.join(root,file)

            relative = os.path.relpath(src_path,Source)
            dest_path = os.path.join(Destination , relative)

            os.makedirs(os.path.dirname(dest_path),exist_ok=True)

            # Copy the files if its new 

            print(calculate_hash(src_path))
            shutil.copy2(src_path , dest_path)
            Copied_Files.append(relative)

    return Copied_Files

def MarvellousDataShieldStart(Source="Data"):
    BackupName = "MarvellousBackup"

    print("Back Up process started Successfully at:",time.ctime()) 

    files = BackupFiles(Source , BackupName)
    print("Report of the backup")

    for name in files:
        print(name)

def main():

    Border = "-" *50
    print(Border)
    print("______________________Marvellous Data Shield  System_________________________")
    print(Border)
    
    
    if(len(sys.argv) == 2):
        if(sys.argv[1]== "--h" or sys.argv[1] =="--H"):
            print("This script is used to :")
            print("1: Takes auto backup at given time  ")
            print("2: Backup only New and Updated Files")
            print("3: Create an archieve of the backup perodically")
            

        elif(sys.argv[1]== "--u" or sys.argv[1] =="--U"):
            print("Use the aurtomation script as")
            print("ScriptName.py Timeintervel SourceDirectory")
            print("TimeIntervel : The time in minutes for perodic scheduling")
            print("SourceDirectory : Name of the directory to create backed up files")


        else:
            print("Unable to process as there is non such option")
            print("Please use --h or --u to get more details")


    # Python Demo.py 5 Data

    elif(len(sys.argv) == 3):
        print("Inside Projects Logic")
        print("Time Intervel :",sys.argv[1])
        print("SourceDirectory  :",sys.argv[2])
        
        # Apply the Scheduler
        schedule.every(int(sys.argv[1])).minutes.do(MarvellousDataShieldStart,sys.argv[2])

        print("Data Shield System started Successfully")
        print("Time interval in minutes :",sys.argv[1])
        print("Press Ctrl + C to stop the execution")

        # Wait till abort
        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid Number of CommandLine Arguments")
        print("Unable to process as there is non such option")
        print("Please use --h or --u to get more details")


    print(Border)
    print("_________________________ThankYou for Using our Script__________________________________")
    print(Border)
    
if __name__=="__main__":
    main()
