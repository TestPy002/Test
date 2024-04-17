#input--
#x,y=input().split()
#print(x,y)
user_input = "1,2,3"
numbers = user_input.split(",", 2)
print(numbers)
#array=input("Enter numbers-").split(" ",4)
#print(array)
#l=list(map(int,input().split()))
#print(l)
string = "Hello, World!"
uppercase_string = map(str.upper, string)
print("".join(list(uppercase_string)))
string='**Hello**'
print(string.strip('*'))
#x = [ int(x)  for x in input("Enter-").split()]
#print(type(x),x)

#print--
x=7; y=9.06; z='a'; c='hell'
print(x,y,z,c,sep=' ~ ',end='=}->')
print("\nx=%d\ny=%.2f\tz=%c\nc=%s"%(x,y,z,c))
#just like in C lang
print("%10d"%(6))
print("1234567890")
print("%10s"%("Hello"))
print("%.2s"%("Hello"))
print("%10.2f"%(1.9325))
#format-> syntax- str.format
print("x={}  y={}  z={}  c={}".format(x,8.04,z,'heaven'))
print('I am {1} years old and week has {0} days. Month has {m:d} and I have{days: .2f} rupees'.format(x,y,m=31,days=325.699))
string="you are {3}, live there for {1} days"
print(string.format(x,y,z,c))
#unformatted and formatted data
for i in range(1,7):
    print(i,i**2,i**3,i**4)
for i in range(1,7):
    print("{:6d} {:6d} {:6d} {:6d}".format(i,i**2,i**3,i**4))
#using dictionary to format, very efficient since it auto finds the values to be inserted in print statement
data={'name':'Ram','age':17,'job':'student', 'a1':2}
intro='My name is {name} I am {age} years old\nI am a {job}\nI study {a1} hours'
print("My name is {name}\nI am {age} years old\nI am a {job} I study {a1} hours".format(**data))
print(intro.format(**data))
#formatting list means changing datatype or adjusting
l=[23,56]
l2=['{:10d}'.format(x) for x in l]
f=[68.7896,6.5667,444.66677]
f2=['{:.2f}'.format(x) for x in f]
print(l2,f2,sep='\n')
#alignment-> str.centre, str,ljust , str.rjust
string1='This is center'
str2='This is left'
print("This is right".rjust(30,','))
print(string1.center(30,'_'))
print(str2.ljust(30,'.'))

#example of format
t='geek'
for i in range(6):
    t='',t,''
    print(str(t).center(100))
