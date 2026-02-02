Value1 =[10,20,30,40,10]
Value1[1] = 200   #List is Mutable
print(Value1)
print(type(Value1))

Value2 =(10,20,30,40,10)
#Value2[1] = 200  # Tupple is Immutable
print(Value2)
print(type(Value2))


Value3 ={10,20,30,40,10}
print(Value3)
print(type(Value3))


x =50
def Demo():
    global x
    x = x + 10
    print(x)

Demo()   
    