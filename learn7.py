#functions
def fun(a,b):
    print(f"I am {a} \n You are {b}")
fun('Ram','Fool') #direct arguements that works on order
fun(b='fool',a='Ram') #using variable names to store values, order dont matter
def emp(): pass #empty function
def yld():
    a=7
    yield 1
    yield 'one'
    yield a
print(next(yld()),next(yld())) #next func can be used
print(next(yld()))
print(*yld()) # yld is generator acts as iterator so *yld unpacks all values and displays all values
#As u can see, since its a function, so the pointer keeps refreshing its position back to its initial position
for x in yld(): #only by this method, we can print all values
    print(x)

#default arguments
#1st method
def multiply(a:int,b:int,c:int=1)->int: #default argument
    return a*b*c
print(multiply(5,7))
#2nd method
from functools import partial
def mult(a:int,b:int,c:int)->int:
    return a*b*c
m=partial(mult,1) #partial(func name,default arguement value as many as no of arguements). it fills arguments from right to left
print(m(5,7)) #c=1 by default
m1=partial(m,5,7) #partial fun of partial fun
print(m1()) #all arguments got default values
#2nd method advantage is can reuse fun with same values 
#but disadvantage is cant change values, m1(5,6,7) will show error
#but multiply(5,6,7) wont show error
def a(u,v):
    return u(v)
def s(x):
    return x**2
print(a(s,4))

#coroutine is func with yield used as input method for data entering
#it pauses func execution at yield and resumes after getting data
def print_name(prefix): 
	print("Searching prefix:{}".format(prefix)) 
	i=1
	while True: 
		name = (yield) 
		if prefix in name: 
			print(name) 
		else: print('no prefix')
corou = print_name("Dear") # need to create object for coroutine function
corou.__next__() #__next__ starts execution of func upto yield then waits for data to be fed
corou.send("Atul") #sends data to yield and starts execution until next yield is reached
#As in func, while is run infinetly with yield inside, so keeps asking for data to be entered
corou.send("Dear Atul") #for 2nd run of while, next yield data
corou = print_name("Sir") #updating the object with new start data
corou.__next__()
corou.send("Sir bl")
coro = print_name("Sir") #creating a new 2nd object
coro.__next__()
coro.send("Sir sam")
corou.close() #closes the func that is running infinite unless loop/no. of yield are finite

#function as classes, function objects
#func objs can take funcs as parameters, and can be returned from func
print("\nFunction objects\n".center(30,'-'))
def sum(a,b):
    return a+b
print(sum(5,7)) #normal func call
s=sum #func object
print(s(5,6))
#func as parameters
def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def dis(f):
    print(f)
dis(sum(9,6))
s=sub(9,2)
dis(s)
#func as return
def add(a):
    def sum(b):
        return a+b
    return sum
x=add(6) #creates obj with a=6 then add returns sum
print(x(21)) #now 21 is put in sum which is returned above,b=21, hence returns a+b
print(x(1)) #here 1 is put to sum instead to 21

#classs and object
print("\nClass and objects\n".center(30,'-'))
class Fun:
    a=10 #class variables
    b='name'
    __c=14 #private variable
Fun.a=19; #changing class element value
f=Fun #creating object
f.b='Ramu' #again changing value affects class value
f2=Fun
f2.a=21; f2.b='Sonu'
print(Fun.a,Fun.b,'\n',f.a,f.b)
#As can see above, the values are changed since we can directly changing the class original variable values

class tap:
    w=1 #static variable, can be accessed directly by Class name
    def __init__(self,x,y): #init is used for constructor, constructor used for variable initializtion mainly
        self.a=x #self is default attribute for all class functions
        self.b=y #self is replaced by object name, when object calling
        #self var are unique to all objects created
    def __str__(self):
        return "string-a=%d,b=%s"%(self.a,self.b)
    def __repr__(self):
        return 'This is repr'
    def __del__(self): #its destructor, which can be called by, del obj name or its auto called
        print("obj is destroyed")
t=tap(19,'Sam') #calling class tap is function calling since its constructor
t2=tap(24,'Anil')
#del t #destructor called
print(t.a,t.b,'\n',t2.a,t2.b)
print(t) #calls str method/func
print([t])
t.w=5
tap.w=7 #static var value change affects all objects who didnt changed its value previously
print(t.w,tap.w,t2.w)
#static variables are shared all by objects of class
# private variable access
class hid: 
	__hiddenVariable = 10
scrt = hid	 
print(scrt._hid__hiddenVariable) 

#inheritance
class Person(): # parent class or base class
	def __init__(self, name, idnumber):
		self.name = name
		self.idnumber = idnumber
	def display(self):
		print(self.name)
		print(self.idnumber)
	def details(self):
		print("My name is {}".format(self.name))
		print("IdNumber: {}".format(self.idnumber))
#derived class can access class variables and its functions and can also change its functions and variables but that change dont affect base class
class Employee(Person): # child class or Derived class of Person class
	def __init__(self, name, idnumber, salary, post):
		self.salary = salary
		self.post = post
		Person.__init__(self, name, idnumber) #calling init func of base class Person to initialize name and idnumber
        #instead of calling constructor
        #can directly call variable name with base class name :-
        #Person.name=name
        #Person.idnumber=idnumber
        #but this method wont allow usage of self.name and self.idnumber like below, can only access variable with class name
	def details(self):
		print("My name is {}".format(self.name))
		print("IdNumber: {}".format(self.idnumber))
		print("Post: {}".format(self.post))
a = Employee('Rahul', 886012, 200000, "Intern") #obj of derived class
a.display() #derived cls obj calling base class func
a.details() #calling changed base class func
p=Person('Ram',1101)
p.details() #unchanged func of base class

#inheritance can be multi level and multiple and heirchical-one parent class has multiple base classes like below
#polymorphism example
class Bird:
    def intro(self):
        print("There are many types of birds")
    def fly(self):
        print("Most birds can fly but some cant")
class parrot(Bird): #inheriting Bird class
    def fly(self): #changing func behaviour of subclass
        print("Parrots can fly")
class cock(Bird):
    def fly(self):
        print("cock cant fly")
b=Bird()
b.intro()
p=parrot()
p.fly()
cock().intro()
cock().fly()

#inheritance and polymorphism example with super function usage isntead of accessing base class elements with its name 
class Person(object): # Base or Super class
	def __init__(self, name): 
		self.name = name 
	def getName(self): 
		return self.name 
	def isEmployee(self): 
		return False
class Employee(Person): # Inherited or Subclass (Note Person in bracket) 
	def __init__(self, name, id): 
        #super(derived class name,self).func name(variable name excluded self)
		super(Employee, self).__init__(name) #accessing base class using super and func name
		self.empID = id 
	def isEmployee(self): 
		return True
	def getID(self): 
		return self.empID 
emp = Employee("Geek1", "E101") 
p=Person("Ramu")
print(emp.getName(), emp.isEmployee(), emp.getID()) 
print(p.getName(),p.isEmployee())
