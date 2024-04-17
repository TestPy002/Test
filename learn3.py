# Declaring elements
l = [3, 2, 1, 3, 'r', 'ab', 'r']
t = (1, 3, 3, 4.5, 'g', 'gg')
s = {1, 2, 3, 4, 'a', 'b'}
d = {'name': 'John', 'age': 20}

# Adding elements
# For list
l.append(5)
print(l)  # Output: [3, 2, 1, 3, 'r', 'ab', 'r', 5]
# For set
s.add('c')
print(s)  # Output: {1, 2, 3, 4, 'a', 'b', 'c'}
# For dictionary
d['gender'] = 'Male'
print(d)  # Output: {'name': 'John', 'age': 20, 'gender': 'Male'}
print(l)
#copying
s1=s.copy() #copy function works on all datatypes

# Deleting elements
# For list
l.remove(3)
print(l)  # Output: [2, 1, 'r', 'ab', 'r', 5]
# For set
s.remove('b')
print(s)  # Output: {1, 2, 3, 4, 'a', 'c'}
# For dictionary
del d['age']
print(d)  # Output: {'name': 'John', 'gender': 'Male'}
#clear function removes all values
#pop means deleting value and storing the deleted value somewhere else
z=l.pop(2)
print(z,l.pop(2)) #works on dictionary too
# Concatenating
# For list
merged_list = l + [6, 7, 8]
print(merged_list)  # Output: [2, 1, 'r', 'ab', 'r', 5, 6, 7, 8]
# For tuple
merged_tuple = t + (6, 7, 8)
print(merged_tuple)  # Output: (1, 3, 3, 4.5, 'g', 'gg', 6, 7, 8)
# For set
merged_set = s | {6, 7, 8}
print(merged_set)  # Output: {1, 2, 3, 4, 'a', 'c', 6, 7, 8}
# For dictionary
merged_dict = {**d, **{'address': 'New York'}} #** is used to unpack dictionary
print(merged_dict)  # Output: {'name': 'John', 'gender': 'Male', 'address': 'New York'}

# Set Operations
print(s & {1, 2, 3})  # &-intersection , can aslo write, s.intersection_update({1, 2, 3})
print(s | {1, 2, 3})  # |-union
print(s - {1, 2, 3})  # difference, can also write, s.difference_update( {1, 2, 3} )
print(s ^ {1, 2, 3})  # ^-symmetric difference or s.symmetric_difference_update({1,2,3})
print({1, 2} <= {1, 2, 3})  # <= is subset checker, returns true if former is subset, or {1,2}.issubset({1,2,3})
print({1,2,3}.issuperset({1,2})) # or can use >= , does opposite as above
print(s.isdisjoint({6, 7,8}))  # isdisjoint() checks if both sets have no element in common
# counting duplicate elements
print(t.count(3)) #count function for tuple and list

#dictionary operations
print(d.keys()) #keys function gives key values
print(d.values()) #values function gives value of the keys
print(d.items()) #items() gives key-value pair

# more operations
l.insert(2,6) #inserts 6 at index 2
print(l)
del l[2] #removes element present at index 2
print(l)
l.extend([3,4]) #adds one list to list l, works for tuple too
s.update([1,2]) # same function as extend
d.update(name='Jane',marks=40) # can change value to existing key like this or like below
d.update({'adrress':'jammu','age':30}) # same work as above
print(l,s,d)
print(l.index(2)) #prints the index position of element 2, works for all datatypes
print()
l2=[x*2 for x in l] # using for, iterates over all elements in l, then creates new list as per x*2 operation
print(l2)
l3=[ [1,2] , ['a',5] , ['a','r'] ]
l4=[x for sublist in l3 for x in sublist] # flattening list
print(l4)
l2= [l]*3
print(l2) # nesting works for all datatypes
print(l!=l2) # comparison != or == works on all datatypes

a,b,c,d,e,f=t #tuple unpacking
print(a,b,c,d,e,f)

#map function- it creates a list,tuple or string by applying opertion(function) on existing one
lis=[1,2,3]
print(list(map(lambda x:x**2, lis )))
print(tuple(map(str.upper, 'hello world')))
x= list(map(int,input("Enter 5 numbers- ").split(" ",4)))
print(x)

#filter function- checks each element of list/tuple/string based on a condition/function which returns true/false
#hence it returns the elements which were true
lt=[1,2,3,4,5,6,7,8]
l=filter( lambda x: x%2==0, lt) #filter(function,datatype)
print("\nEven numbers-")
print(list(l)) #prints by converting raw data into list
def fun(x:int):
    if(x%2==0): return True
    else: return False
l2=filter(lambda x:fun(x),lt)
print(list(l2))
def vowel(x):
    v=['a','e','i','o','u']
    if x in v :return True
    else:False
string='Hello,World'
v= filter(vowel,string)
print('Vowels are')
print(v) #prints location of stored data, that is prints pointer pointing to v
print(*v) # *v prints value that is pointed by pointer