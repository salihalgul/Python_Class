
class Calc(object):
    def __init__(self, a, b):
        self.value1 = a
        self.value2 = b
    def add(self):
        return self.value1 + self.value2
        
    def multiply(self):
        return self.value1 * self.value2
    def divide(self):
        return self.value1 / self.value2
    def subs(self):
        return self.value1 - self.value2
    
print("Choose add(1), multiply(2), divide(3), subs(4)")
selection = input("select 1,2,3 or 4")
    
v1 = float(input("first value : "))
v2 = float(input("second value : "))
c1 = Calc(v1,v2)

if selection == "1":
    add_result = c1.add()
    print("Add : {}".format(add_result))
elif selection == "2":
    multiply_result = c1.multiply()
    print("Multiply : {}".format(multiply_result))
elif selection == "3":
    divide_result = c1.divide()
    print("Divide : {}".format(divide_result))    
elif selection == "4":
    subs_result = c1.subs()
    print("Subs : {}".format(subs_result))
else:
    print("Wrong entry")