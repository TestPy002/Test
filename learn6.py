#type conversion
d=10.8 #float
print(int(d)) #int conversion
d=123 #int
print(float(d)) #float conversion
o='67' #string
i=int(o,8) #int(variable,base), here string o is treated as octal no, so base is 8
print(i)
b='10010'
print(int(b,2)) #b is binary no with base 2, converted into integer with decimal base 10
c='a' #character
ci=ord(c) #converts character to ASCII value
print(ci)
x=65
print(chr(x)) #converts ASCII code to character
print(hex(37)) #converts 56 into hex code
print(oct(129)) #converts 129 into octal code

#Encoding and decoding
s="Hello World"
e = s.encode('ASCII') #converts text into ASCII code by encode
print(f"Encoded Text: {e}")
c=b'Hello World' # b is encoded text for Hello world
if(e==c): print("Encoding correct")
d=e.decode('ASCII') #converts ASCII code into text by decode
print(d)
if(d==s): print("Decoding correct")

#operators
a=10; b=10; a=c # a and c variable is same
print(a is b, a is c) #is checks if variable is same, doesnt matter if values are same
print(a is not c) #not is used so prints opposite
print(a==b) #checks if both have same value
a=10
l=[10,20,30]
print(a in l, a not in l) #checks if element is present in it or not
x=5; y=9;
minimum=x if x<y else y #one line if-else
print(minimum)
a= True
print(not a,~17)
print('\a')
# match is switch statement of C
ch=1
match ch:
	case 0:
		print( "zero")
	case 1:
		print( "one")
	case 2:
		print( "two")
	case default:
		print( "something")
# Accessing items and indexes enumerate()
cars = ["Aston" , "Audi", "McLaren"]
for x in enumerate(cars): #enumerate gives index then value at index
	print (x[0], x[1],end=',')
print()
# using 2 variable for enum
cars = ["Aston" , "Audi", "McLaren"]
for x,y in enumerate(cars):
	print (x,y,end=',')
print()
# Printing return value of enumerate() 
cars = ["Aston" , "Audi", "McLaren"]
print(enumerate(cars))
print (*enumerate(cars)) # * will unpack the tuple which is returned by enumerate function
# Python code to illustrate
# chaining comparison operators
x = 5
print(1 < x < 10)
print(10 < x < 20 )
print(x < 10 < x*10 < 100)
print(10 > x <= 9)
print(5 == x > 4)

#iter and next
l=[1,2,3,4,6,7]
a=iter(l) #creates a iterator of iterable that is l
print(next(a),next(a),next(a)) #next is used to access the elements of iterator
print(*a) #*a unpacks the itertor entity into its elements
#As above, iterator is like pointer pointing to index
#next func is used 3 times, so pointer points to index 3 so *a unpacks all elements from index 3 to last

#alternate is generator expression
a=(x for x in range(5)) #generator expression, need ()
print(next(a),next(a)) #next can be used on generator too
for n in a:
	print(n,end=' ') 
print()
#iter on range
d=iter(range(7))
print(next(d),next(d))
for x in d:
	print(x,end=' ')
print()
f=range(2,12,2)
print(f.start,f.step,f.index(10))
#read module itertools for few more functions