#string
gfg = "geeksforgeeks"
gfg = "".join(reversed(gfg)) # Reverse the string using reversed and join function
print(gfg[::-1]) #slicing, start 0, end last character by default and step is -1 means it prints back
del gfg # deletes whole string
#strings cant be edited so a new string can created by changing old string
String1 = "Hello, I'm a Geek"
print(String1) 
String2 = String1[0:2] + String1[3:] #deletes character at index 2
print("\nDeleting character at 2nd Index: ") 
print(String2) 
String1 = "Hello, I'm a Geek"
print(String1) 
#updating character
list1 = list(String1) 
list1[2] = 'p' #lists can be added
String2 = ''.join(list1)  #join is needed to convert listb to string
print("\nUpdating character at 2nd Index: ") 
print(String2) 
String3 = String1[0:2] + 'p' + String1[3:] #deleted character at 2nd position and then added 'p'
print(String3) 

#array
import array as ary #name changed from array to ary
a= ary.array('i',{1,2,3}) #array.array is module.function, creates array with datatype 'i' and values which can be set/list/tuple
l=[3.5,6.7,1.2,6.7,1.2]
b=ary.array('d',l)
print(a[0],b[2])
a.insert(1,4) #adds 4 at index 1
b.append(5.6) #adds 5.6 at end
x=a.pop(2) #removes value at index 2 and returns the value
b.remove(6.7) #removes the value 6.7 as first occurence
print(b.index(1.2)) #gives index at which 1.2 located, gives its first appearance
print("1.2 =",b.count(1.2)) # no of occurences
a[0]=10 #can edit values
print(*a) # * unpacks elements from it, works on list too, basically breaks single entity like array into multiple individual entities that is its elements
a.reverse() #reverses array and doesnt return anything
print(*a)
n=[x for x in range(10,21)]
c=ary.array('i',n)
for i in range(10):
    print(c[i],end=' ')
#slicing
c1=c[3:7]
print()
for i in range(len(c1)):
    print(c1[i],end=' ')
print()
c2=c[::2]
for i in range(len(c2)):
    print(c2[i],end=' ')

a.extend(n) #combines 2 array to existingb array, here n is added to a
print()
print(*a)
l=[1,2,3]
a.fromlist(l) #adds list to an array, same as extend func, just works on list
print(*a)
l=a.tolist() #converts array to list
print(l)

#read array module and nymphy module