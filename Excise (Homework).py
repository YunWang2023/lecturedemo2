'''
#2. Variables and interactive programs
#2-1
print("Hello Wang Yun")


#2-2
Radius = float(input("Radius: "))
Area= 3.14*(Radius**2)
print(f"Area={Area:.2f}")

#2-3

a = int(input('Enter a: '))
b = int(input('Enter b: '))
print(f"a={a},b={b}")
print(f"a={b},b={a}")

length=float(input('Enter length: '))
width=float(input('Enter width: '))

print(f"length={length},width={width}")
print(f"Perimeter={length*2+width*2}")
print(f"Area={length*width}")


#2-4
a=int(input('Enter a: '))
b=int(input('Enter b: '))
c=int(input('Enter c: '))
print(f"a={a},b={b},c={c}")
sum= a+b+c
product = a*b*c
average=sum/3
print(f"sum={sum},product={product},average={average:.2f}")


#2-5
talents=float(input("Enter Talents: "))
pounds=float(input("Enter Pounds: "))
lots=float(input("Enter Lots: "))

total_lots=talents*20*32+pounds*32+lots
total_grams=total_lots*13.3

kilograms=float(total_grams//1000)
grams=total_grams%1000

print(f"The weight in modern units:{kilograms:.0f} kilograms and {grams:.2f} grams.")


#2-6
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


#5. List structures and iterative loops (for)
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

#6. Functions
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

#7. Tuple, set, and dictionary
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

#8 Using relational databases
#8-1
import mysql.connector

def get_airport_info(cursor, icao_code):
    query = "SELECT name, municipality FROM airports WHERE ident = %s"
    cursor.execute(query, (icao_code,))
    result = cursor.fetchone()
    return result

def main():
    icao_code = input("Enter the ICAO code of the airport: ")

    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='200687',
        database='countries',
        autocommit=True
    )

    cursor = connection.cursor()

    airport_info = get_airport_info(cursor, icao_code)

    if airport_info:
        airport_name, municipality = airport_info
        print(f"Airport: {airport_name}, Location: {municipality}")
    else:
        print("No airport found.")

    cursor.close()
    connection.close()

if _name_ == "_main_":
    main()

#8-2
import mysql.connector

def fetch_airports_by_country(cursor, iso_country):
    query = """
    SELECT type, COUNT(*) as count
    FROM airports
    WHERE iso_country = %s
    GROUP BY type
    ORDER BY count DESC
    """
    cursor.execute(query, (iso_country,))
    return cursor.fetchall()

def main():
    iso_country = input("Enter the ISO country code (e.g., 'FI' for Finland): ").upper()

    connection = mysql.connector.connect(
        host='127.0.1.1',
        port=3306,
        database='countries',
        user='root',
        password='200687',
        autocommit=True
    )

    cursor = connection.cursor()

    airport_data = fetch_airports_by_country(cursor, iso_country)
    if airport_data:
        print(f"Airports in country '{iso_country}':")
        for airport_type, count in airport_data:
            print(f"{count} {airport_type} airport(s)")
    else:
        print(f"No airports found for country code '{iso_country}'.")

    cursor.close()
    connection.close()

if _name_ == "_main_":
    main()


#8-3
import mysql.connector
from geopy.distance import geodesic

def coordinates(cursor, ident):
    query = f"SELECT latitude_deg, longitude_deg FROM airports WHERE ident = '{ident}'"
    cursor.execute(query)
    result = cursor.fetchone()
    return result

def calculate_distance(coord1, coord2):
    return geodesic(coord1, coord2).kilometers

def main():
    airport1_icao = input("Enter the ICAO code of the first airport: ").upper()
    airport2_icao = input("Enter the ICAO code of the second airport: ").upper()

    connection = mysql.connector.connect(
        host='127.0.1.1',
        port=3306,
        database='countries',
        user='root',
        password='200687',
        autocommit=True
    )

    try:
        cursor = connection.cursor()

        airport1_coords = coordinates(cursor, airport1_icao)
        airport2_coords = coordinates(cursor, airport2_icao)

        if airport1_coords is None or airport2_coords is None:
            print("One or both airports not found in the database.")
            return

        distance = calculate_distance(airport1_coords, airport2_coords)
        print(f"The distance between {airport1_icao} and {airport2_icao} is {distance:.3f} kilometers.")

    finally:
        cursor.close()
        connection.close()

if _name_ == "_main_":
    main()


#9 Fundamentals of object-oriented programming

#9-1
class Car:

    def __init__(self,registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def __str__(self):
        return f'{self.registration_number},{self.maximum_speed},{self.current_speed},{self.travelled_distance}'

#main
car = Car("ABC-123","142")
print(str(car))


#9-2
class Car:

    def __init__(self,registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self,change_of_speed):

        if self.current_speed + change_of_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed + change_of_speed  < 0:
             self.current_speed = 0
        else:
            self.current_speed +=  change_of_speed
        print(self)

    def __str__(self):
        return f'registration_number：{self.registration_number}, maximum_speed：{self.maximum_speed} km/h, current_speed：{self.current_speed} km/h, travelled_distance:{self.travelled_distance} km'

#main
car = Car("ABC-123",142)
print(car)
car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
car.accelerate(-200)


#9-3
class Car:

    def __init__(self,registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self,change_of_speed):

        if self.current_speed + change_of_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed + change_of_speed  < 0:
             self.current_speed = 0
        else:
            self.current_speed +=  change_of_speed
        print(f"With the change of speed {change_of_speed},the car's information : \n{self}")

    def drive(self,hours):
        self.travelled_distance += self.current_speed*hours
        print(f"After {hours}h,the car's information : \n{self}")

    def __str__(self):
        return f'registration_number：{self.registration_number}, maximum_speed：{self.maximum_speed} km/h, current_speed：{self.current_speed} km/h, travelled_distance:{self.travelled_distance} km'

#main
car = Car("ABC-123",142)
car.current_speed = 60
car.travelled_distance = 2000

print(car)
car.drive(1.5)


#9-4
import random
class Car:

    def __init__(self,registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self,change_of_speed):

        if self.current_speed + change_of_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed + change_of_speed  < 0:
             self.current_speed = 0
        else:
            self.current_speed +=  change_of_speed


    def drive(self,hours):
        self.travelled_distance += self.current_speed*hours


    def __str__(self):
        return f'registration_number：{self.registration_number}, maximum_speed：{self.maximum_speed} km/h, current_speed：{self.current_speed} km/h, travelled_distance:{self.travelled_distance} km'

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            change_of_speed = random.randint(-10, 15)
            car.accelerate(change_of_speed)
            car.drive(1)

    def print_status(self):
        print(f"Status of the race '{self.name}':\n")
        print(f"{'Car':<15} {'Speed (km/h)':<15} {'Distance (km)'}")
        print("-" * 40)
        for car in self.cars:
            print(f"{car.registration_number:<15} {car.current_speed:<15} {car.travelled_distance}")
        print("\n")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False

# Main program
if __name__ == "__main__":
    cars = [Car(f"Car-{i+1}", random.randint(100, 200)) for i in range(10)]
    race = Race("Grand Demolition Derby", 8000, cars)
    hours = 0
    while not race.race_finished():
        race.hour_passes()
        hours += 1
        if hours % 10 == 0:
            race.print_status()


    print(f"The race '{race.name}' is finished after {hours} hours!")
    race.print_status()

'''
#10 Association

#10-1
class Elevator:

    floor_now = 0

    def __init__(self,bottom,top):
        self.bottom = 1
        self.top = top

    def floor_up(self):
        self.floor_now += 1

    def floor_down(self):
        self.floor_now -= 1

    def go_to_floor(self,choice):
        if choice == 1:
            print(f"It is floor {self.floor_now}")
        else:
            while choice > self.floor_now:
                self.floor_up()
                print(f"It is floor {self.floor_now}")
                choice -= 1
            while choice < self.floor_now:
                self.floor_down()
                print(f"It is floor {self.floor_now}")
                choice += 1

#main
h = Elevator(1,10)
h.go_to_floor(5)
h.go_to_floor(1)
