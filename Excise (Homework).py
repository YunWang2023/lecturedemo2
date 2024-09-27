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
width=float(input('Enter width: '))

print(f"length={length},width={width}")
print(f"Perimeter={length*2+width*2}")
print(f"Area={length*width}")


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
for I in numbers:
    sum += I
print(f"The sum is {sum}")

#5-1b
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

#5-2
numbers = []
while True:
    number = input("Enter a number:")
    if number =="":
        break
    numbers.append(int(number))

sorted_numbers=sorted(numbers,reverse=True)
print(sorted_numbers)

#5-3
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

#5-3b
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


#5-4
cities_list = []
city = input("Enter a city:")
while city !="" :
    cities_list.append(city)
    city = input("Enter a city:")
for city in cities_list :
    print (f"-{city} ")


#6-1
import random
def random_dic():
    dic = int(random.randint(1,6))
    return dic

while True:
    random_number = random_dic()
    print(random_number)
    if random_number == 6 :
        break


#6-2
import random

def random_dic(n):
    dic = int(random.randint(1,n))
    return dic

def main():
    max_number = int (input("Enter the max_number:"))
    while True:
        random_number = random_dic(max_number)
        print(random_number)
        if random_number == max_number :
            break
if __name__ == '__main__':
    main()

#6-3
def gal_to_l (gal) :
    l = float(gal) * 3.78541
    return l

gal_str = input("Enter the gallons:")

while gal_str!= "" :
    gal = gal_to_l(gal_str)
    print(gal)
    gal_str = input("Enter the gallons:")


#6-4
def sum_of_list (list):
    sum=0
    for i in list:
        sum+=i
        return sum

numbers_list = []
number = input("Enter a number:")
while number != "" :
    number_int=int(number)
    numbers_list.append(number_int)
    number = input("Enter a number:")

the_sum_of_list = sum_of_list(numbers_list)
print(f"The sum is {the_sum_of_list}")


#6-5
def cut_uneven_number (list):
    even_number = []
    for number in list:
        if number % 2 == 0:
            even_number.append(number)
    return even_number

original_list=[]
number = input("Enter a number:")
while number != "" :
    number_int=int(number)
    original_list.append(number_int)
    number = input("Enter a number:")

print(original_list)
even_number = cut_uneven_number(original_list)
print(even_number)


#6-6
import math
def calculates_unit_price(price,diameter):
    unit_price = price/((diameter/2)**2*math.pi)
    return unit_price

diameter_first_pizza = float(input("Enter the diameter of the first pizza in centimeters:"))
price_first_pizza= float(input("Enter the price of the first pizza:"))
diameter_second_pizza = float(input("Enter the diameter of the second pizza in centimeters:"))
price_second_pizza= float(input("Enter the price of the second pizza:"))

if calculates_unit_price(price_first_pizza,diameter_first_pizza) < calculates_unit_price(price_second_pizza,diameter_second_pizza):
    print("The first pizza provides better value for money ")
elif calculates_unit_price(price_first_pizza,diameter_first_pizza) > calculates_unit_price(price_second_pizza,diameter_second_pizza):
    print("The first pizza provides better value for money ")
else:
    print("The two pizzas have the same value for money ")


#7-1
seasons=("spring", "spring","spring","summer", "summer","summer","autumn", "autumn","autumn","winter","winter","winter")
number_of_month=int(input("Enter the number of months:"))
if number_of_month==12 :
    print(seasons[0])
elif 0<number_of_month<12 :
    print(seasons[number_of_month-1])
else:
    print("The number must be between 1 and 12")


#7-2
names_set=set()
name_input=input("Enter a name:")
while name_input !="":
    if name_input in names_set:
        print(f"Existing name")
    else:
        print(f"New name")
        names_set.add(name_input)
    name_input = input("Enter a name:")
print(f"The list of names is :")
for name in names_set:
    print(name)



#7-3

airport_data = dict()

while True:
    print("Enter a new airport,press 1")
    print("Fetch the information,press 2")
    print("Quick,press Enter")
    choice = input("What is your choice?\n")

    if choice == "1":
        new_ICAO_code = input("Enter a new ICAO code:")
        new_airport = input("Enter new airport:")
        airport_data [new_ICAO_code] = new_airport
        print("Date updated\n")


    elif choice == "2":
        ICAO_code_to_check = input("Enter ICAO code:")
        print(f"The airport is {airport_data[ICAO_code_to_check]}\n")

    elif choice == "":
        break

    else:
        print("Invalid input\n")
print("Bye\n")


'''

#8-1
import random
from random import randint
e=randint(1,6)
print(e)



