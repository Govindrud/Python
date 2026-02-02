import threading

def Display():
    print("Inside Display function:",threading.get_ident())   #Call Back Function
    for i in range(100):
        print("inside Display")
        

def main():
    print("Inside main:",threading.get_ident())
    t = threading.Thread(target=Display)
    t.start()
    t.join()        # its to join the main and end 
    print("End of main")
  

if __name__ =="__main__":
    main()
