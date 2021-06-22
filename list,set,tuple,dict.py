#!/usr/bin/env python
# coding: utf-8

# In[1]:


colour = ["red", "blue", "green","yellow"] 
print(colour)


# In[2]:


# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.
# Lists allow duplicate values
colour = ["red", "blue", "green","yellow", "red"]
print(colour)


# In[3]:


# To determine how many items a list has, use the len() function:
len(colour)


# In[4]:


# List items can be of any data type:string, int or bool
l1=[1,3,5,6,7,8,9,3]
l2=["red", "blue", "green","yellow"] 
l3=[True, False]
print(l1, l2, l3)


# In[5]:


# A list can contain different data types:
Mylist=["red", "blue", "green","yellow", True, False, 1,4,7]
print(Mylist)


# In[7]:


# type()
print(type(Mylist))


# In[8]:


# List constructor
Mylist2=list(("red", "blue", "green", True, False, 1,4,7))
print(Mylist2)


# In[19]:


# Access Items, The first item has index 0.
colour = ["red", "blue", "green","yellow"] 
print(colour[0])
print(colour[1])
print(colour[2])
print(colour[3])
print(colour[-1])
print(colour[-4])


# In[26]:


Numlist=[1,2,3,4,5,6,7,8,56,34,25]
print(Numlist[0:4]) # # index 4 will not be included
print(Numlist[0:8]) # index 8 will not be included
# By leaving out the start value, the range will start at the first item:
print(Numlist[:6])
#By leaving out the end value, the range will go on to the end of the list:
print(Numlist[0:])
print(Numlist[-1:-5])
print(Numlist[-5:-1])


# In[27]:


# To determine if a specified item is present in a list use the in keyword:
Mylist2=["red", "blue", "green", True, False, 1,4,7]
if "blue" in Mylist:
    print("blue is there in the list")
else:
    print("blue is not there in the list")


# In[28]:


Mylist2=["red", "blue", "green", True, False, 1,4,7]
if "Apple" in Mylist:
    print("Apple is there in the list")
else:
    print("Apple is not there in the list")


# In[31]:


Mylist2=["red", "blue", "green", True, False, 1,4,7]
if "Apple" in Mylist:
    print("Apple is there in the list")
else:
    print("Apple is not there in the list")


# In[36]:


# Change a Range of Item Values
# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
list1=["Shaheema","Vidya","Karishma", "Rahul","Sanjay"]
print(len(list1))
list1[3:4]=["Jikki","Krishna"]
print(list1)
#print(len(list1))


# In[33]:


list1=["Shaheema","Vidya","Karishma", "Rahul","Sanjay"]
list1[3:5]=["Jikki","Krishna"]
print(list1)


# In[40]:


# Insert Items
colour=[1,2,3,4,6,7,8,9]
colour.insert(4,5)
print(colour)


# In[46]:


# Add list items 
Student=["Ram", "Sam","Shyamili"]
Student.append("Nila") # To add an item to the end of the list, use the append() method:
print(Student)
Student.append("Rooby")
print(Student)


# In[47]:


# To append elements from another list to the current list, use the extend() method.
Student=["Ram", "Sam","Shyamili"]
list1=["Shaheema","Vidya","Karishma", "Rahul","Sanjay"]
Student.extend(list1)
print(Student)


# In[52]:


# Add Any Iterable
list1=["Shaheema","Vidya","Karishma", "Rahul","Sanjay"]
set={1,2,3,4,5}
tuple1=(23,34,45)
list1.extend(set)
print(list1)
tuple1=(23,34,45)
list1.extend(tuple1)
print(list1)


# In[53]:


# Remove Specified Item
list1 = ['physics', 'chemistry', 'Biology']
list1.remove('physics')
list1


# In[54]:


# Remove Specified Index, The pop() method removes the specified index.
list1.pop(0)
list1


# In[55]:


# If you do not specify the index, the pop() method removes the last item.
list1=["Shaheema","Vidya","Karishma", "Rahul","Sanjay"]
list1.pop()
list1


# In[57]:


# The del keyword also removes the specified index:
list1=["Shaheema","Vidya","Karishma", "Rahul","Sanjay"]
del list1[0]
print (list1)


# In[60]:


list1=["Shaheema","Vidya","Karishma", "Rahul","Sanjay"]
del list1[1:3]
print (list1)


# In[62]:


# The del keyword can also delete the list completely.
list1=["Shaheema","Vidya","Karishma", "Rahul","Sanjay"]
del list1


# In[65]:


# The clear() method empties the list.
list1=["Shaheema","Vidya","Karishma", "Rahul","Sanjay"]
list1.clear()
list1


# In[66]:


# Print all items in the list, one by one:
Student=["Ram", "Sam","Shyamili"]
for x in Student:
    print(x)


# In[68]:


# Print all items by referring to their index number:
colour= ["Red", "Black", "White", "Yellow"]
for x in range(len(colour)):
  print(colour[x])


# In[71]:


colour= ["Red", "Black", "White", "Yellow"]
i = 0
while i < len(colour):
  print(colour[i])
  i+=1


# In[73]:


# Looping Using List Comprehension
colour= ["Red", "Black", "White", "Yellow"]
[print(x) for x in colour]


# In[74]:


colour= ["Red", "Black", "White", "Yellow"]
[print(x) for x in colour]


# In[76]:


colour= ["Red", "Black", "White", "Yellow", "Orange"]
list1 = []

for x in colour:
  if "a" in x:
   list1.append(x)

print(list1)


# In[77]:


colour= ["Red", "Black", "White", "Yellow", "Orange"]
Newlist=[x for x in colour if "a" in x]
print(Newlist)


# In[85]:


colour= ["Red", "Black", "White", "Yellow", "Orange"]
newlist = [x for x in colour if x != "Black"]
print(newlist)
list2 = [x for x in colour]
print(list2)
list3= [x for x in range(6)]
print(list3)
list4=[x for x in range(9) if x<5]
print(list4)


# In[87]:


# Set the values in the new list to upper case:
colour= ["Red", "Black", "White", "Yellow", "Orange"]
colour1 = [x.upper() for x in colour]
print(colour1)


# In[88]:


colour= ["Red", "Black", "White", "Yellow", "Orange"]
colour1 = [x.lower() for x in colour]
print(colour1)


# In[89]:


newlist = ['nil' for x in colour1]
print(newlist)


# In[94]:


colour= ["Red", "Black", "White", "Yellow", "Orange"]
list1=[x if x != "Red" else "Blue" for x in colour]
print(list1)


# In[95]:


colour= ["Red", "Black", "White", "Yellow", "Orange"]
colour.sort()
colour


# In[96]:


Numlist=[12,56,6,78,90,23,43,1,345]
Numlist.sort()
Numlist


# In[98]:


Numlist=[12,56,6,78,90,23,43,1,345]
Numlist.sort(reverse=True)
Numlist


# In[100]:


Numlist=[12,56,6,78,90,23,43,1,345]
list2=Numlist.copy()
list2


# In[101]:


# list built-in function 
Numlist=[12,56,6,78,90,23,43,1,345]
list2=Numlist.copy()
list2=list(Numlist)
list2


# In[108]:


# Join lists
l1=[1,3,5,6,7,8,9,3]
l2=["red", "blue", "green","yellow"] 
list3 = list1 + list2 
list3


# In[109]:


l1=[1,3,5,6,7,8,9,3]
l2=["red", "blue", "green","yellow"] 
for x in l1:
    l2.append(x)
print(l2)


# In[110]:


l1=[1,3,5,6,7,8,9,3]
l2=["red", "blue", "green","yellow"] 
l1.extend(l2)
l1


# In[112]:


# Exercise on list
#Print the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
print(fruits[1])


# In[114]:


#Change the value from "apple" to "kiwi", in the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits[0]="kiwi"
fruits


# In[116]:


# Use the append method to add "orange" to the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits


# In[118]:


#Use the insert method to add "lemon" as the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")
fruits


# In[123]:


# Use the remove method to remove "banana" from the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
fruits


# In[124]:


# Use negative indexing to print the last item in the list.
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])


# In[125]:


# Use a range of indexes to print the third, fourth, and fifth item in the list.
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])


# In[126]:


# Use the correct syntax to print the number of items in the list.
fruits = ["apple", "banana", "cherry"]
len(fruits)


# In[128]:


# Dict
Mydict = {'name': 'shaheema','age': 25,'job': 'SRF', 'city': 'india', 'email': 'shahee@yahoo.com'}
print(Mydict)


# In[130]:


# Print the "name" value of the dictionary and duplicates not allowed
print(Mydict["name"])


# In[131]:


Mydict = {'name': 'shaheema','age': 25,'job': 'SRF', 'city': 'india', 'email': 'shahee@yahoo.com', 'name':'Wafiya'}
print(Mydict)


# In[133]:


# To determine how many items a dictionary has, use the len() function, The values in dictionary items can be of any data type:
print(len(Mydict))
print(type(Mydict))


# In[136]:


#Accessing items using get()
Mydict = {'name': 'shaheema','age': 25,'job': 'SRF', 'city': 'india', 'email': 'shahee@yahoo.com'}
x=Mydict.get("name")
x


# In[137]:


# The keys() method will return a list of all the keys in the dictionary.
Mydict = {'name': 'shaheema','age': 25,'job': 'SRF', 'city': 'india', 'email': 'shahee@yahoo.com'}
x=Mydict.keys()
print(x)


# In[138]:


Mydict["Gender"]="female"
print(Mydict)


# In[139]:


x=Mydict.keys()
print(x)


# In[140]:


# Get a list of the values:
Mydict.values()


# In[141]:


Mydict["name"]="Wafiya"
Mydict.values()


# In[142]:


y=Mydict.items()
print(y)


# In[143]:


Mydict["email"]="Wafiya@gmail.com"
z=Mydict.items()
print(z)


# In[144]:


# Check if "model" is present in the dictionary:
Mydict = {'name': 'shaheema','age': 25,'job': 'SRF', 'city': 'india', 'email': 'shahee@yahoo.com'}
if "job" in Mydict:
    print("Yes, there is a key called Job")
else:
    print(False)


# In[145]:


# update dict
Mydict = {'name': 'shaheema','age': 25,'job': 'SRF', 'city': 'india', 'email': 'shahee@yahoo.com'}
Mydict.update({'age':'26'})
print(Mydict)


# In[146]:


# Python - Add Dictionary Items
Mydict = {'name': 'shaheema','age': 25,'job': 'SRF', 'city': 'india', 'email': 'shahee@yahoo.com'}
Mydict["Gender"]="female"
print(Mydict)


# In[149]:


# Python - Remove Dictionary Items
Mydict = {'name': 'shaheema','age': 25,'job': 'SRF', 'city': 'india', 'email': 'shahee@yahoo.com'}
Mydict.pop("city")
Mydict


# In[150]:


# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
Mydict = {'name': 'shaheema','age': 25,'job': 'SRF', 'city': 'india', 'email': 'shahee@yahoo.com'}
Mydict.popitem()
print(Mydict)


# In[151]:


# The del keyword removes the item with the specified key name:
Mydict = {'name': 'shaheema','age': 25,'job': 'SRF', 'city': 'india', 'email': 'shahee@yahoo.com'}
del Mydict["city"]
Mydict


# In[153]:


del Mydict


# In[154]:


Mydict = {'name': 'shaheema','age': 25,'job': 'SRF', 'city': 'india', 'email': 'shahee@yahoo.com'}
# The clear() method empties the dictionary:
Mydict.clear()
Mydict


# In[156]:


# Print all key names in the dictionary, one by one:
Mydict = {'name': 'shaheema','age': 25,'job': 'SRF', 'city': 'india', 'email': 'shahee@yahoo.com'}
for x in Mydict:
    print(x)


# In[158]:


# Print all values in the dictionary, one by one:
Mydict = {'name': 'shaheema','age': 25,'job': 'SRF', 'city': 'india', 'email': 'shahee@yahoo.com'}
for i in Mydict:
    print(Mydict[i])


# In[163]:


Mydict = {'name': 'shaheema','age': 25,'job': 'SRF', 'city': 'Coimbatore', 'email': 'shahee@yahoo.com'}
for x in Mydict.values():
  print(x)


# In[164]:


for x in Mydict.keys():
  print(x)


# In[165]:


#Loop through both keys and values, by using the items() method:
for x,y in Mydict.items():
    print(x,y)


# In[166]:


# Python - Copy Dictionaries
x=Mydict.copy()
print(x)


# In[167]:


y=dict(Mydict)
print(y)


# In[168]:


# Nested Dictionaries
# A dictionary can contain dictionaries, this is called nested dictionaries.
School = {
  "Student1" : {
    "name" : "shaheema",
    "Age" : 23
  },
  "Student2" : {
    "name" : "Karishma",
    "year" : 27
  },
  "Student3" : {
    "name" : "Vidya",
    "Age" : 21
  }
}
School


# In[170]:


Student1 = {"name" : "shaheema", "Age" : 23}
Student2  ={"name" : "Karishma","Age" : 27}
Student3 = {"name" : "Vidya","Age" : 21}
School= {"Student1": Student1, "Student2": Student2, "Student3": Student3}
print(School)


# In[171]:


# Dict Exercises
# Use the get method to print the value of the "model" key of the car dictionary.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964}
print(car.get("model"))


# In[172]:


# Change the "year" value from 1964 to 2020.
car["year"]=2020
print(car)


# In[173]:


# Add the key/value pair "color" : "red" to the car dictionary.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964}
car["color"]="red"
car


# In[174]:


#Use the pop method to remove "model" from the car dictionary.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964}
car.pop("model")
car


# In[175]:


# Use the clear method to empty the car dictionary.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964}
car.clear()
print(car)


# In[177]:


# Tuples, A tuple is a collection which is ordered and unchangeable.
# Since tuples are indexed, they can have items with the same value:
# A tuple can contain different data types:
my_Tuple=(1,2,"Kerala","India",1.23,1, True)
print(my_Tuple)


# In[180]:


# To determine how many items a tuple has, use the len() function:
print(len(my_Tuple))


# In[182]:


# To create a tuple with only one item, you have to add a comma after the item, 
#otherwise Python will not recognize it as a tuple.
Tuple1=("Apple")
print(type(Tuple1))
Tuple2=("Apple",)
print(type(Tuple2))


# In[184]:


#It is also possible to use the tuple() constructor to make a tuple.
tuple1 = tuple(("red", "black", "yellow")) # note the double round-brackets
print(tuple1)


# In[186]:


# Print the third item in the tuple, The first item has index 0.
print(tuple1[2])
# Negative Indexing
print(tuple1[-1])
print(tuple1[-2])


# In[187]:


# Range of Indexes
my_Tuple=(1,2,"Kerala","India",1.23,1, True)
print(my_Tuple[3:6])


# In[188]:


my_Tuple=(1,2,"Kerala","India",1.23,1, True)
print(my_Tuple[:6])


# In[189]:


my_Tuple=(1,2,"Kerala","India",1.23,1, True)
print(my_Tuple[3:])


# In[190]:


my_Tuple=(1,2,"Kerala","India",1.23,1, True)
print(my_Tuple[-6:-3])


# In[191]:


my_Tuple=(1,2,"Kerala","India",1.23,1, True)
if True in my_Tuple:
    print("Tuple contains Bool object")
else:
    print("Nil")


# In[192]:


# Convert the tuple into a list to be able to change it:
x = ("Red", "green", "yellow")
y = list(x)
y[1] = "black"
x = tuple(y)

print(x)


# In[195]:


my_Tuple=(1,2,"Kerala","India",1.23,1, True)
x=list(my_Tuple)
x.append("orange")
print(x)
my_Tuple= tuple(x)
print(my_Tuple)


# In[196]:


print(type(my_Tuple))


# In[197]:


# Add tuple to a tuple
Student=("liya", "Naseen", "Raju")
x=("Arya","Namitha",)
Student+=x
print(Student)


# In[200]:


# Tuples are unchangeable, so you cannot remove items from it
x = ("Red", "green", "yellow")
y = list(x)
y.remove("green")
print(y)
x=tuple(y)
print(x)


# In[202]:


del x


# In[203]:


my_tuple = (3, 4.6, "dog")
a, b, c = my_tuple
print(a)      
print(b)      
print(c)  


# In[204]:


T = ('red', 'green', 'blue', 'cyan')
a,b,c,d= T
print(a)


# In[205]:


# If the number of variables is less than the number of values,
# you can add an * to the variable name and the values will be assigned to the variable as a list:
T = ('red', 'green', 'blue', 'cyan')
a,*b= T
print(b)


# In[207]:


# If the asterisk is added to another variable name than the last, 
#Python will assign values to the variable until the number of values left matches the number of variables left.
T = ('red', 'green', 'blue', 'cyan','white','pink')
a,*b, c= T
print(a)
print(b)
print(c)


# In[209]:


my_Tuple=(1,2,"Kerala","India",1.23,1, True)
for i in my_Tuple:
    print(i)


# In[211]:


# Loop Through the Index Numbers
my_Tuple=(1,2,"Kerala","India",1.23,1, True)
for i in range(len(my_Tuple)):
  print(my_Tuple[i])


# In[212]:


# Using a While Loop
my_Tuple=(1,2,"Kerala","India",1.23,1, True)
i = 0
while i < len(my_Tuple):
  print(my_Tuple[i])
  i += 1


# In[215]:


# To join two or more tuples you can use the + operator:
Tuple1= (1,3,4,5,7,8)
Tuple2=(2,6,9)
print(Tuple1 + Tuple2)


# In[216]:


Tuple1= (1,3,4,5,7,8)
x= Tuple1 * 5
print(x)


# In[220]:


# tuple exercise
#Print the first item in the fruits tuple.
fruits = ("apple", "banana", "cherry")
print(fruits[0])


# In[221]:


# Use the correct syntax to print the number of items in the fruits tuple.
print(len(fruits))


# In[223]:


# Use negative indexing to print the last item in the tuple.
print(fruits[-1])


# In[224]:


# Use a range of indexes to print the third, fourth, and fifth item in the tuple.
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])


# In[225]:


# Once a set is created, you cannot change its items, but you can add new items.
# Sets cannot have two items with the same value.
S = {'red', 'green', 'blue', 'red'}
print(S) # Sets are unordered, so you cannot be sure in which order the items will appear.


# In[227]:


print(len(S))


# In[229]:


# A set can contain different data types:
set_new = {"abc", 34, True, 40, "male"}
set_new


# In[230]:


print(type(set_new))


# In[238]:


# Python - Access Set Items
set_new = {"abc", 34, True, 40, "male"}
for i in set_new:
    print(i)


# In[239]:


# Check if an item is present in the set:

set_new = {"abc", 34, True, 40, "male"}
print(34 in set_new)


# In[240]:


set1={1,3,4,5,6,7,8,9,78}
set1.add(100)
print(set1)


# In[241]:


set1={1,3,4,5,6,7,8,9,78}
list1=[23,24,25]
set1.update(list1)
print(set1)


# In[242]:


set1={1,3,4,5,6,7,8,9,78}
set1.update([23,24,25])
print(set1)


# In[243]:


s1={1,2,3}
s2={4,5,6}
s1.update(s2)
s1


# In[244]:


# Python - Remove Set Items
set1={1,3,4,5,6,7,8,9,78}
set1.remove(78)
set1


# In[245]:


# If the item to remove does not exist, remove() will raise an error.
# If the item to remove does not exist, discard() will NOT raise an error.
set1={1,3,4,5,6,7,8,9,78}
set1.remove(100)
set1


# In[246]:


set1={1,3,4,5,6,7,8,9,78}
set1.discard(100)

set1


# In[247]:


set1.discard(78)
set1


# In[248]:


# The return value of the pop() method is the removed item.
S = {'red', 'green', 'blue'}
x = S.pop()
print(S)
# removed item
print(x)


# In[249]:


S = {'red', 'green', 'blue'}
S.clear()
S


# In[251]:


del S
print(S)


# In[252]:


# You can loop through the set items by using a for loop:
S = {'red', 'green', 'blue'}
for x in S:
    print(x)


# In[255]:


# Join Two Sets 1) The union() method returns a new set with all items from both sets:
set1= {"shaheema", "Vidya"}
set2={"Karishma"}
set3= set1.union(set2)
set3


# In[256]:


# The update() method inserts the items in set2 into set1:
set1= {"shaheema", "Vidya"}
set2={"Karishma"}
set1.update(set2)
set1


# In[259]:


set1= {"shaheema", "Vidya", "Karishma"}
set2={"Karishma"}
set3= set1.intersection(set2)
set3


# In[260]:


# The intersection() method will return a new set, that only contains the items that are present in both sets. 
# whereas The intersection_update() method will keep only the items that are present in both sets.
set1= {"shaheema", "Vidya", "Karishma"}
set2={"Karishma"}
set1.intersection_update(set2)
set1


# In[262]:


# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
x = {"red", "green", "blue"}
y = {"yellow", "green", "pink"}

x.symmetric_difference_update(y)

print(x)


# In[265]:


# The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
x = {"red", "green", "blue"}
y = {"yellow", "green", "pink"}

z=x.symmetric_difference(y)

print(z)


# In[266]:


# exersices
# Check if "apple" is present in the fruits set.
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")


# In[269]:


# Use the add method to add "orange" to the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
fruits


# In[271]:


# Use the correct method to add multiple items (more_fruits) to the fruits set.
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
fruits


# In[272]:


# Use the remove method to remove "banana" from the fruits set.

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
fruits


# In[273]:


# Use the discard method to remove "banana" from the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
fruits


# In[ ]:




