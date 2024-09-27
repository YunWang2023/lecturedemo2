'''
#1
import random
random_number = random.randint(1, 10)
user_number = int(input("Enter a number between 1 and 10: "))

while random_number != user_number:
    user_number = int(input("Enter a number between 1 and 10: "))
    if user_number == random_number:
        print("Congratulations! You have won!")


#2
import random
target_number = random.randint(1, 3)
number=0
while True :
    user_number = int(input("Enter a number between 1 and 3: "))
    number += 1
    if user_number == target_number:
        print(f"Well guessed! You tried {number} times .")
        break
    else:
        print("Try again!")

#3
import random
result = random.choice(["heads", "tails"])
while result  != "heads":
    print("Flipped", result)
    result = random.choice(["heads", "tails"])
print("Finally , flipped:", result )

#4
first = 0
while first <5:
    second = 1
    while second < 5:
        print(f"{first} times {second} is " , first*second)
        second += 1
    first += 1
print("All done")


5

for  i in range  (5):
    print(i)



#List
names = []
name = input("Enter a name: ")
print(name)
while name != "":
    names.append(name)
    name = input("Enter a name: ")
    print(name)
print(names)
print(len(names))
print(id(names))
print(names[0])


names = []

name = input("Enter the first name or quit by pressing Enter: ")
while name!="":
    names.append(name)
    name = input("Enter the next name or quit by pressing Enter: ")

print(names)



import numbers

names = ["wang","zhang","li","zhao","fei"]
print(names)

names.remove("wang")
print(names)

names.append("hu")
print(names)

print(len(names))
print(id(names))
print(names[0])

names.insert(0,"chen")
print(names)

othernames = ["xiao","liu"]
names.extend(othernames)
print(names)

what_index = names.index("zhang")
print(what_index)

for x in names:
    print(x)

names.sort()
print(names)
print(names[1])

names.sort(reverse=True)
print(names)

names.sort(key=len)
print(names)

names2 = sorted(names)
print(names2)



for x in range(3,33,3) :
 print(x)



def sum(a,b):
 sum = a + b
 return sum

def multiply(a,b):
 multiply = a * b
 return multiply

def divide(a,b):
  if b == 0：
    break
  else:
    quotient = a / b

  return quotient

def subtract(a,b):
 subtract = a - b
 return subtract

print(f"The sum is :",sum(2,5))
print(f"The product is :",multiply(2,5))
print(f"The quotient is :",divide(2,5))
print(f"The difference is :",subtract(2,5))


#6
numbers = []

def sum (numbers) :
    total = 0
    for number in numbers:
       total += number
    return total

def find_largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

def find_smallest(numbers):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest


while True:
    number = input("Enter a number: ")
    if number == "":
        break
    else:
        number = int(number)
        numbers.append(number)


print(f"sum is : {sum(numbers)} \n largest is :{find_largest(numbers)}\n smallest is: {find_smallest(numbers)}")



#7 Tuple
days_of_the_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
day_number = int(input("Enter the day number (1-7): "))
day = days_of_the_week[day_number-1]
print(f"Day number {day_number} is {day}.")



#7a
day_weeks = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
day_number = int(input("Enter the day number (1-7): "))
day = day_weeks[day_number-1]
print(f"Day number {day_number} is {day}.")


#7b
import random
def cast():
    first,second = random.randint(1,6),random.randint(1,6)
    return first,second
dice1,dice2 = cast()
print(f"The dice shows {dice1} and {dice2}")


#7c
fruits = "orange","apple","bananas"
print(fruits)
first,second,third = fruits
print(f"first fruit is {first}, second fruit is {second}")

#7d

# fruits = "Orange", "Banana", "Apple"
# (first, second, third) = fruits
# print(f"The fruits are: {first}, {second} and {third}.")

#7e
import random

def cast():
    first, second ,third = random.randint(1,6), random.randint(1,6),random.randint(1,6)
    return first, second,third

die1, die2 ,die3= cast()
print(f"The dice show {die1} and {die2} and {die3}.")


#7f
my_list = [1,2,3]
my_list.append(4)
print(my_list)
my_list.remove(3)
print(my_list)
my_list2 = my_list.pop()
print(my_list2)
print(my_list)
my_list.append(5)
my_list.append(6)
my_list.append(7)
print(my_list)
my_list3 = my_list.pop(3)
print(my_list3)
print(my_list)


#7g
my_tuple = (1,2,3,4,6,4,2,3,7,7,7)
count_of_7 = my_tuple.count(7)
print(count_of_7)
index_of_7 = my_tuple.index(7)
print(index_of_7)


#7h

my_dt1 = {"Zhang":87,"Li":99,"Wang":60}
print(my_dt1)
my_dt1["Zhao"] = 100
search_name = input("Enter a name: ")
if search_name in my_dt1:
    print(f"The score of {search_name} is :{my_dt1[search_name]}")

#5a
import random
numbers = []
number = int(input("How many dice to roll:"))
sum = 0
for i in range(number):
    number = random.randint(1,6)
    numbers.append(number)
    sum += number
print(numbers)
print(f"The sum is :{sum}")

#5b
numbers = []
while True:
    number = input("Enter a number:")
    if number =="":
        break
    numbers.append(int(number))

sorted_numbers=sorted(numbers,reverse=True)
print(sorted_numbers)

#5c
number = int(input("Enter a number:"))
dividend = 1
if number==1:
   print(f"{number} is not a prime number")
else:
    while True  :
        dividend += 1
        if dividend <= number and number % dividend ==0:
           break
    if dividend  < number:
        print (f"{number} is not a prime number")
    else:
        print(f"{number} is a prime number")


#5d
number = int(input("Enter a number:"))
dividend = 1
if number==1:
   print(f"{number} is not a prime number")
else:
    for i in range(2,int(number**0.5+1)):
        if number % i == 0:
            print(f"{number} is not a prime number")
            break

    else:
        print(f"{number} is a prime number")

# 12
def creat_list(number):
    new_list = []
    for i in range(1,number+1):
        new_list.append(2*i)
    return new_list


number = 7
print(creat_list(number))

'''
a = "6"
b = 3
c = "2"
d = 1

print(a+c)
print(b+d)
print(a*b)
