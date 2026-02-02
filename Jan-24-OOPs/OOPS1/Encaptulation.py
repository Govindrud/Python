class Arithmatic :
    def __init__(self,A,B):
        self.No1 =A
        self.No2 =B
        print("Objects get created successfully")

    def Addition(self):
        Ans=0
        Ans=self.No1 + self.No2
        return Ans
    
    def Substraction(self):
        Ans=0
        Ans=self.No1 - self.No2
        return Ans
    
    #Arithmatic(id(obj1),10,100)
obj1 = Arithmatic(10,100)
obj2 = Arithmatic(11,10)

ret = obj1.Addition()
print(ret)

ret = obj2.Substraction()
print(ret)