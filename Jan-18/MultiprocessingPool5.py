import time
import multiprocessing
import os
def SumCube(No):
    print("Process is running with :",os.getpid())
    sum=0

    for i in range(1,No+1):
        sum=sum + (i**3)
    return sum


def main(): 
    Data =[1000000,2000000,3000000,4000000,5000000,6000000,7000000,8000000,90000000,10000000]
    Result=[]
    start_time=time.time()

    pobj= multiprocessing.Pool()
    Result = pobj.map(SumCube,Data)
    pobj.close()
    pobj.join()

    End_time =time.time()

    print(Result)

    print("Total execution time :",End_time-start_time) 

if __name__=="__main__":
    main()
