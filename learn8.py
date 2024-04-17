#static variable
class My:
    @staticmethod #static method only works on outside variables and returns values which are not connected to cls
    def smd(x, y): #static methods dont need self/cls parameters but still they works
        return x + y
print(My.smd(5,5))# Calling static method directly on class
r = My
print(r.smd(5,8))  #calling static on object

#class variable
class fun:
    v = 10
    @classmethod
    def cmd(cls, x):
        return cls.v * x #changes class variable
print(fun.cmd(5)) #calling directly
o=fun
print(o.cmd(7)) #calling cls method on object
#class method with constructor
class two:
    def __init__(self, x):
        self.x = x
    @classmethod
    def cmd(cls, x):
        # This class method creates an instance of MyClass with the value of x doubled.
        return cls(x * 2) #since two is constructor so returns constructor func by returning cls
t=two(5) #one object
print(t.cmd(7).x) #cmd func creates another object with x=7,then doubles to 14, then creates object of x=14

#Another example of class method and constructor but diff arguments passed
class MyClass:
    def __init__(self, x):
        self.x = x
    @classmethod
    def create_with_additional_value(cls, x, additional_value):
        # This class method creates an instance of MyClass with the value of x plus additional_value.
        return cls(x + additional_value) #calls constructor and creates a object
# Create an instance of MyClass using the class method
instance1 = MyClass.create_with_additional_value(5, 3)
# Print the value of instance1's attribute x
print(instance1.x)  # Output: 8

#class variables and static variables
class MyClass:
	static_var = 0

	def __init__(self):
		self.static_var += 1
		self.instance_var = self.static_var

obj1 = MyClass()
print(obj1.instance_var) # Output: 1

obj2 = MyClass()
print(obj2.instance_var) # Output: 2

print(MyClass.static_var) # Output: 2

class MyClass:
	static_var = 0

	def __init__(self):
		MyClass.static_var += 1
		self.instance_var = MyClass.static_var

obj1 = MyClass()
print(obj1.instance_var) # Output: 1

obj2 = MyClass()
print(obj2.instance_var) # Output: 2

print(MyClass.static_var) # Output: 2
