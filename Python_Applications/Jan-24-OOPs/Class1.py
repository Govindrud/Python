class Demo():
    def __init__(self):    #Instance Method
        print("Inside Constructor")
    
    def __del__(self):     #Instance Method
        print("Inside destructor")

obj = Demo()

print("End of Application")
