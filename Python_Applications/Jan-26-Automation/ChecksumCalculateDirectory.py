import hashlib
import os

def CalculateCheckSum(FileName):
    fobj= open(FileName ,"rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()
    return hobj.hexdigest()


def DirectoryWatcher(DirectoryName ="Marvellous"):
    Ret = False
    Ret = os.path.exists(DirectoryName)

    if  (Ret == False):
        print("There is no Such Directory")
        return
    
    Ret = os.path.isdir(DirectoryName)

    if (Ret == False ):
        print("It is not a Directory")
        return

    for Foldername ,subFoldername , FileName in os.walk(DirectoryName):
        for fname in FileName:
            fname = os.path.join(Foldername,fname)
            Checksum = CalculateCheckSum(fname)

            print(f"File name :{fname} Checksum :{Checksum}")

def main():

    DirectoryWatcher()

if __name__=="__main__":
    main()
