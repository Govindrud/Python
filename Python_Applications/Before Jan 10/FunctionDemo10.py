#One Function can call another Function

def fun():
    print("Inside Fun")

def gun():
    print("Inside Gun")
    fun()

def main():     # One function can call Another function
    gun()    
    

    
if __name__== "__main__": 
    main()



   
