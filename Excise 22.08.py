
#2. Variables and interactive programs

'''
#1
print("Hello Wang Yun")


#2
Radius = float(input("Radius: "))
Area= 3.14*(Radius**2)
print(f"Area={Area:.2f}")

#3

a = int(input('Enter a: '))
b = int(input('Enter b: '))
print(f"a={a},b={b}")
print(f"a={b},b={a}")

length=float(input('Enter length: '))
wideth=float(input('Enter wideth: '))

print(f"length={length},wideth={wideth}")
print(f"Perimeter={length*2+wideth*2}")
print(f"Area={length*wideth}")


#4
a=int(input('Enter a: '))
b=int(input('Enter b: '))
c=int(input('Enter c: '))
print(f"a={a},b={b},c={c}")
sum= a+b+c
product = a*b*c
average=sum/3
print(f"sum={sum},product={product},average={average:.2f}")


#5
talents=float(input("Enter Talents: "))
pounds=float(input("Enter Pounds: "))
lots=float(input("Enter Lots: "))

total_lots=talents*20*32+pounds*32+lots
total_grams=total_lots*13.3

kilograms=float(total_grams//1000)
grams=total_grams%1000

print(f"The weight in modern units:{kilograms:.0f} kilograms and {grams:.2f} grams.")


#6
import random

num3_1=random.randint(0,9)
num3_2=random.randint(0,9)
num3_3=random.randint(0,9)
print(f"3-digit code is: {num3_1}{num3_2}{num3_3}")

num3_11=random.randint(0,9)
num3_22=random.randint(0,9)
num3_33=random.randint(0,9)
print(f"3-digit code is: {num3_11}{num3_22}{num3_33}")

num4_1=random.randint(1,6)
num4_2=random.randint(1,6)
num4_3=random.randint(1,6)
num4_4=random.randint(1,6)
print(f"4-digit code is: {num4_1}{num4_2}{num4_3}{num4_4}")

num4_11=random.randint(1,6)
num4_22=random.randint(1,6)
num4_33=random.randint(1,6)
num4_44=random.randint(1,6)
print(f"4-digit code is: {num4_11}{num4_22}{num4_33}{num4_44}")



#3. Conditional structures (if)

#3-1

length = int(input("Enter the length of a zander in centimeters:"))
limit = 42
if length>= 42 :
    print("It is OK")
else:
    x= limit - length
    print(f"Release the fish back into the lake. {x} centimeters below the size limit.")


#3-2

input_class = input("enter the cabin class of a cruise ship:")
if input_class == "LUX":
    print("upper-deck cabin with a balcony.")
elif input_class == "A":
    print("above the car deck, equipped with a window.")
elif input_class == "B":
    print("windowless cabin above the car deck.")
else:
    print("windowless cabin below the car deck.")


#3-3
input_hemoglobin = input("Enter biological gender(M or F):").upper()

input_biological = float(input("Enter hemoglobin:"))

if input_hemoglobin == "F" and 117<=input_biological<=155 or input_hemoglobin == "M" and 134<=input_biological<=167:
    print("Normal")

elif input_hemoglobin == "F" and 117>input_biological or input_hemoglobin == "M" and 134>input_biological:
    print("Low")

else:
    print("High")


#3-4

input_year=int(input("Enter year:"))
if input_year%4==0 and input_year%100!=0 or input_year%400==0:
    print("This is a leap year.")
else:
    print("This is not a leap year.")



#4. While loops (while)

#4-1 Write a program that uses a while loop to print out all numbers divisible by three in the range of 1-1000.

limit = 1000
start = 1
while start <= limit :
    if start % 3 == 0 :
       print(start)
    start += 1



#4-2 Write a program that converts inches to centimeters until the user inputs a negative value. Then the program ends.

inch = float(input("Enter inch:"))
while inch>=0 :
    cm=2.54*inch
    print(f"{inch}in.={cm}cm")
    inch = float(input("Enter inch:"))


#4-3 Write a program that asks the user to enter numbers until they enter an empty string to quit. Finally, the program prints out the smallest and largest number from the numbers it received.

numbers = input("Enter numbers:")
numbers_float = float(numbers)
largest = numbers_float
smallest = numbers_float

while numbers != "" :
    numbers_float = float(numbers)
    if numbers_float > largest :
        largest = numbers_float
    elif numbers_float < smallest :
        smallest = numbers_float
    numbers = input("Enter numbers:")
print(f"The smallest number is {smallest} and largest number is {largest}")


#4-4

import random

target_number = random.randint(1,10)
guess_number = int(input("Enter a number:"))
while guess_number != target_number:

  if guess_number > target_number:
    print(f"Too high.")
  elif guess_number < target_number:
    print(f"Too low.")
  guess_number =int(input("Enter a number:"))
print(f"Correct")


#4-5
username = input("Enter your username:")
pswd = input("Enter your password:")
times = 0

while times<= 5:
    if username != "python" or pswd != "rules":
        print("WAccess denied.")
        times+=1
        username = input("Enter your username:")
        pswd = input("Enter your password:")
    else:
        print("Welcome")
        break


#4-6
import random
N = int(input("How many random points to generate:"))
times = 0
n = 0
while times <= N :
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if x**2 + y**2 < 1:
        times+=1
        n+=1
    else :
        times+=1
pi = 4*(n/N)
print(f"The value of pi is {pi}.")



#5-1
import random
numbers = []
number = int(input("How many dice to roll:"))
count = 0
sum = 0
while count < number:
    n = random.randint(1,6)
    print(n)
    numbers.append(n)
    count+=1
for i in numbers:
    sum += i
print(f"The sum is {sum}")

#5-2
numbers = []
while True:
    number = input("Enter a number:")
    if number =="":
        break
    numbers.append(int(number))

sorted_numbers=sorted(numbers,reverse=True)
print(sorted_numbers[0],sorted_numbers[1],sorted_numbers[2],sorted_numbers[3],sorted_numbers[4])

'''
#5-3
number = input("Enter a number:")
dividend = 2
while True :
    if number % dividend == 0 :
        break



print(number,"is a prime number")


