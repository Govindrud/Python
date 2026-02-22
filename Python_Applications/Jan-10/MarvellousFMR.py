

def filterX(Task,Elements):   #Calling (CheckEven , Data)
    Result = list()

    for no in Elements:
        Ret =Task(no)
        
        if (Ret == True):
            Result.append(no)
    
    return Result

def mapX(Task,Elements):    #Calling (Increment , FData)
    Result = list()

    for no in Elements:
        # Ret = Task(no)
        Result.append(no)
    return Result

def reduceX(Task ,Elements):    #calling (Add,MData)
    Sum = 0
    #[11,21,23,31]

    for no in Elements :
        Sum = Task(Sum,no)
    return Sum
