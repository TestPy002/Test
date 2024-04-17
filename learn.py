#to run in command prompt -> python ./folder name/file name , here python ./Programs/learn.py
import keyword #import is used to attach module to our code, module is like a function, means we can use a new function by importing, and that function can have sub functions
from test import Main as here #importing Main function from test.py but since name is same so it is renamed as here
#help(format) # help func gives info about python functions whether built in or user created
def Main(): #Main func, tho unnecessary creation,
    p=print #changing name of print, since its just keyword but used as function
# p("he")
    a=[] #list-stores any data type
    a.append(60)
    a.append("Abc")
    a.append(56.89)
    p(a)
    i=input
    sum = lambda x,y : x+y # small functions can created with lamba keyword, fun name = lambda arguments : return value
    b=int(i("Enter num1-")) #input fun is scanf , get renamed to i, as well can write
    c=int(i("Enter num2-"))
    def mul(a:int,b:int)->int : #function declaration and defintion with argument and return value
        d=a*b
        return d
    p(b,"*",c,"=",mul(b,c)) # function calling
    print("5+6=",sum(5,6))
    def many():
        for i in range(0,5,1):
            yield i #it returns multiple values one by one, like a generator generating values one by one
    for i in many(): #now many function act as generater, gives lot of values, so with for loop, we can get all values
        print(i)
    x=int(input("Enter marks-"))
    grade= lambda x : f"{x} is too good, Grade A" if x>90 else "Grade B" if x<=90 & x>80 else f'Grade C' if x>60 else f'{x} is not good'
    print(grade(x))
    def chk(): #function-> def function name () : then spaces in beginning until function code is done
        g=int(input("Enter number for condition-"))
        if(g%2==0): 
            p("Even")  #here for if/elif,spaces needed in beginning or can write on same line like below for elif
        elif (g%2!=0): p("Odd")
    chk()
    count=1
    while(count<5): #while(condition): statement
        print(count,end=' ')
        count+=1
if __name__=="__main__":    
    Main() #calling main func, tho unnecessary if, can just direct write - Main() but tho it is used to check main function is this file and not imported
here() #from test.py file
for i in range (0,5,1): #i is variable whose value starts from 0, gets incremented by 1 ,s.t, i<5; range(initial,end,increment/decrement)
    print(i,end=",") 
    print(i)
x=[3,"jl",'l',4] #list  stores any datatype and can be edited
y= 2,'r',"df",4.7 #tuple is like list , just cant be edited and is declared with() instead of [] or without anything
print(x,y)
print(x[0],y[3]) #index
print(x[1:4],y[2:4],x[0:3:2]) #its slicing, [a:b:c]->prints values from a to b-1 position, means excluding and c is step that is next element will be printed is a+2, if no start then default 0, end - last , step - 1
list1=[1,2,3]; list2=[3,4,5]
list1= list1+list2; list3=list1[2]+list2[0]
print(list1,",",list1[1:2]+list2[2:3],",",list3) #anything is possible
tuple1=1,2,3; tuple2=(2,4,'r')
tuple3=tuple1+tuple2 #same as list, just cant do, tuple1=tuple1+tuple2, since tuple cant be changed
print(tuple3)
print(f'Hi {tuple3}') #print fun usage with f'___', prints anything in blank and for variable, put variable in curly braces
d={'Name':'Ram','Age':15,tuple1:3,tuple3[5]:'r'} #dictionary datatype, curly braces used, can take any basic datatype as input and tuples as well
print(d,type(d)) #type() function used to get type of variable
print(d['Name'],d[tuple3[5]],d[1,2,3]) #dict is like {x,f(x)} in maths,here d[x] is same as f(x), so d[x]= prints the output/image of x under d
var=tuple(d.keys()) # dictionary name.keys() function is used to gets x values then creates a list using list function tho can create tuple or set too, list isnt only option
print(var[0]) #it prints the x values as you can see at their index
set1={3,5,7,'rt','5'} #set same as list but dont have indices, so its unsorted
print(3 in list1) #3 in list is condition statement, which gives true/false as can see, works on all datatypes
print(list1 * 2) #doubles list, can multiply list with whole no
print("The keywords are :")
print(keyword.kwlist)
string1 = "Very Dangerous kill"
print(string1,string1[5]) 
print("Slicing characters from 6-16: ") 
print(string1[3:12]) 
print("\nSlicing characters between 3rd and 2nd last character: ") 
print(string1[3:-2]) 

#read math module and few more modules