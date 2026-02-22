import gc

class Demo():
    def __init__(self):    # Instance Method
        print("Inside Constructor")
    
    def __del__(self):     # Instance Method
        print("Inside destructor")

# Allocate
obj = Demo()

# Use

# Deallocate
del obj

gc.collect

print("End of Application")
