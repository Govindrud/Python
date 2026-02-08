
import psutil
import sys
import os
import time
import schedule


def CreateLog(Foldername):
    Border = "-" *50
    print(Border)

    Ret = os.path.exists(Foldername)

    if(Ret == True):
        Ret = os.path.isdir(Foldername)
        if (Ret == False):
            print("Unable to create folder")
            return
        
    else:
        os.mkdir(Foldername)
        print("Directory for log files gets created successfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    Filename = os.path.join(Foldername,"Marvellous_%s.log"%timestamp)

    print("Log files get created with name :",Filename)

    fobj = open(Filename , "w")
    fobj.write(Border+"\n")
    fobj.write("----Marvellous Platform survelliance System -------\n")
    fobj.write("Log created at :"+time.ctime()+"\n")
    fobj.write(Border+"\n\n")

    fobj.write("---------------------System Report------------------------\n")

    #print("CPU Usage :",psutil.cpu_percent())
    fobj.write("CPU Usage : %s %%\n" %psutil.cpu_percent())

    fobj.write(Border+"\n")

    Mem = psutil.virtual_memory()
    #print("Ram Usage :",Mem.percent)
    fobj.write("RAM Usage : %s %%\n" %Mem.percent)

    fobj.write(Border+"\n")

    fobj.write("\nDisk Usage Report\n")
    fobj.write(Border+"\n")
    for part in psutil.disk_partitions():
        try:
            useage = psutil.disk_usage(part.mountpoint)
            #print(f"{part.mountpoint} used {useage.percent}%%")
            fobj.write("%s -> %s %% used \n" %(part.mountpoint , useage.percent))
        
        except:
            pass

    net = psutil.net_io_counters()
    fobj.write("\nNetwork Usage Report\n")
    fobj.write("sent : %.2f MB\n" %(net.bytes_sent / (1024 * 1024)))
    fobj.write("Recive : %.2f MB\n" %(net.bytes_recv / (1024 * 1024)))
    fobj.write(Border+"\n")

    # Process LOG
    

    fobj.write(Border+"\n")
    fobj.write("---------------End of the Log File----------------------------\n")
    fobj.write(Border+"\n")

   
        
def main():
    Border = "-" *50
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
        
        # Apply the Scheduler
        schedule.every(int(sys.argv[1])).minutes.do(CreateLog,sys.argv[2])

        print("Platform Survellance System started Successfully")
        print("Directory created with name :",sys.argv[2])
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