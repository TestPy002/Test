c= None # null/void datatype
d='j'
z=c,d #list,tuple,set,dict can store variables as well
print(z)
x={1,2}
y={4,5,6}
tup=zip(x,y) # combines 2 any datatype to form tuple of form ( (a,b) , (c,d) ,(e,f) )
set1,set2=zip(*tup) #unzips means opposite of what zip does
u={5,6,4,2,4,5,6,75,34,1,2,3,5,7,5.5}
for i in sorted(u):
    print(i,end=" ")
print()
for i in reversed(sorted(list(u))): #first converted to list, then sorted in ascending then reversed so result is descending order
    print(i,end=" ")
print()
d={2:'two',6:'six'}
print(type(d))
for i in d:
    print(i,d[i])
a=[3,4]
b=(3,5)
d = tuple(d.items()) #dictionary to tuple conversion, for that item() function needs to be attached to dict
p=7,'i'
c={d[1]:p}
print(c,type(c))
di={'i':5,0:'g'}
print(di['i'])
keys = list(di.keys())
print(keys[0])
u=list(u) #set converted to list, still duplicate values are omiited
u.sort() #now sorted, can also do, u = sorted(u)
for i in range(0,len(u)-1): #for loop range can iterate over anything with even different starting point and ending point, not possible for sets, since they dont have indices
    print(u[i],end=" ")
u.reverse() #reverses, can also do. u = reversed(u)
print(u)
print()
print(len(di))
for i in range(0,1):
    print(keys[i],di[i])

#packing and unpacking
#* is used to pack/unpack for array,list and tuple
# ** is used for same in case for dictionary
t=9,3,4,'ab'; d={'a':10,'b':20,'c':30}
print(*t,'\n',*d,sep='-') #unapcking, for dict- it prints key values
def fun(a,b,c):
    print(a,b,c)
fun(**d) # it prints values of keys
def fun2(*l): #packing elements into tuple(default tuple is created)
    print(l,*l) #packed tuple , unpacked tuple
fun2(1,2,3,4,5) #giving multiple arguments
def fun3(**d2): # packs data into dictionary
    print(d2)
    for i in d2:
        print(i,d2[i])
fun3(a=2,b=4) #giving values