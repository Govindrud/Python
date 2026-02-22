import gc

class Demo():
    def __init__(self):    # Instance Method
        print("Inside Constructor")
    
    def __del__(self):     # Instance Method
        print("Inside destructor")

# Allocate
obj1 = Demo()
obj2 = Demo()


# Use

# Deallocate
del obj1
del obj2

gc.collect

print("End of Application")
