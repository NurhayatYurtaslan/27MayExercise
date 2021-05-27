"""
Write a program that inputs an integer value (stop_number) from the user and prints the sum of all numbers from
0 to stop_number. You can assume the user will enter a valid value.
"""
"""
stop_number = int(input("Please enter a stop number: "))
result = 0
for i in range(0, stop_number):
    result = result + i
    print(result)
print(result)
"""

"""
Extend your program to also input the start_number from the user. In this case, your program will add all
numbers from start_number to stop_number. You can assume that the user will enter two valid values.
"""
"""
start_number = int(input("Please enter a start number: "))
stop_number = int(input("Please enter a stop number: "))
result = 0
for i in range(start_number, stop_number):
    result += i
    #print(result)
print(result)
"""

"""
Extend your program to check if the start_number is an integer between 0 and 100. If so, your program will
continue to ask for the second input and perform calculations; otherwise, it prints an error and stops execution.
"""
"""
start_number = int(input("Please enter a start number: "))
if 0 <= start_number <= 100:
    stop_number = int(input("Please enter a stop number: "))
    if start_number <= stop_number <= 100:
        result = 0
        for i in range(start_number, stop_number):
            result += i
        print(result)
    else:
        print("Invalid stop number")
else:
    print("Invalid start number")
"""

"""
They are tools that contain some functions and attributes that enable us to perform some functions easily. It
provides the opportunity to use these functions it hosts in different files and programs over and over again.
Thanks to the modules, Python has become a much more useful and easy-to-implement.
In order to use any module in Python, we first need to 'import' it. Importing means making functions and
attributes within one module available from within another program.
"""
"""
import random as rnd
secret = rnd.randint(1,100)
check = False
#guess = int(input("Please enter you guess: "))
for x in range(5):
    guess = int(input("Please enter you guess: "))
    if guess == secret:
        print("Congrats!!")
        check = True
        break
    elif guess < secret:
        print("Please enter a greater number!!")
    else:
        print("Please enter a smaller number!!")
if not check:
    print("Looseer..The number was: ", secret)
"""

#Dictionaries
"""
d={}
print(d)
print(type(d))
"""
"""
d={"python":1, "Course":2}
print(d)
print(d["Course"])
print(d.keys())
print(d.values())
print(d.items())
for v in d.values():
    print(v)
for v,k in d.item():
    if v == 2:
        print(k)
d["a"]=[3,4,5,6]
#d.pop("python")
#print(d)

print(len(d))

print("a" in d)


"""
"""
d2={"machine":"learning", "artificial":"intelligence"}
print(d2)
print(d2["artificial"])

d2["java"]= "programming"
print(d2)

d2["rubby"]= "programming"
print(d2)

d2["rubby"]= "language"
print(d2)

print(d2.keys())
print(d2.values())
print(d2.items)

for k in d2.keys():
    print(k)
for v in d2.values():
    print(v)

for k,v in d2.items():
    print("Key",k, "Value",v)

del d2 ["rubby"]
print(d2)

d2_copy=d2.copy()
print(d2_copy)
"""

"""
d4 = {"human":2, "cat":4, "spider":8}
for i in d4:
    leg = d4[i]
    print("%s has %d legs " % (i,leg))
    print(str(i) + " has " + str(leg) +" legs.")

for i,leg in d4.items():
    print(str(i) + " has " + str(leg) +" legs.")
"""
"""
districts = {"İstanbul":["Bostancı", "Beşiktaş", "Kadıköy"],"Ankara":["Çankaya", "Gölbaşı", "Kızılcahamam"],"İzmir":["Çeşme","Bornova","Foça"]}
print(districts["İstanbul"])
print(type(districts))
print(type(districts["Ankara"]))
print(districts["İzmir"][0][0])
print(districts["İzmir"][2])

"""

"""
#creating a dictionary from a list
nums = list(range(9)) # [0,1,2,3,4,5,6,7,8]
even_sqr = {x: x**2 for x in nums if x % 2 == 0}
print(even_sqr)

"""

"""
#Sets


s = {"python", 5,6,8,5,6,"abc", "python","python","python","python","python","python","python","python","python"}
print(s)
empty = set()
print(type(empty))
empty2={}
print(type(empty2))


s2 = set(["python", 5,6,8,5,6,"abc", "python"])
print(s2)

ne = set("pineapple")
print(ne)

s2.add("ai")
print(s2)
print(len(s2))

s2.remove("ai")
print(s2)
print(len(s2))

"""
"""
#karekök bulma
from math import sqrt
#import math
print({x for x in list(range(10))})
print({sqrt(x) for x in list(range(10))})
"""

#Tuples
"""
tupl = (1,2,3,4,5)
print(tupl)
print(type(tupl))
tuple2 = ()
print(type(tuple2))
print(tupl[3])
print(tupl[-2])
print(tupl[:4])

dm3 = ("nur", 5, 8, "december")
dm3.index("december")
print(dm3)
print(dm3.count(5))
print(dm3)
"""
"""
# creating a dictionary in which tuples are keys.
a = {(x, x+1): x for x in range(10)}
print(a)
"""
"""
s5 = (5,6)
print(type(s5))
#print(a[s5])
"""

vegetables = ['squash', 'pea', 'carrot', 'potato']
vegetables.sort()
print(vegetables)

fruit = ['watermelon','pineapple', 'apple', 'banana', 'apricot']
sorted(fruit)
print(fruit)