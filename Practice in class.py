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

'''
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
