import threading

def SumEven(No):
    sum =0 
    for i in range(2,No+1,2):
        sum=sum+i
    print("Even Sum is : ",sum) 

def SumOdd(No):
    sum =0 
    for i in range(1,No+1,2):
        sum=sum+i
    print("odd Sum is : ",sum)    

def main():
    SumEven(6)
    SumOdd(6)
    


  

if __name__ =="__main__":
    main()
