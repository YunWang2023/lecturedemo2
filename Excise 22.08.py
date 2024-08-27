
#2. Variables and interactive programs

''''
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



#2. Variables and interactive programs

#2-1

length = int(input("Enter the length of a zander in centimeters:"))
limit = 42
if length>= 42 :
    print("It is OK")
else:
    x= limit - length
    print(f"Release the fish back into the lake. {x} centimeters below the size limit.")



#2-2

input_class = input("enter the cabin class of a cruise ship:")
if input_class == "LUX":
    print("upper-deck cabin with a balcony.")
elif input_class == "A":
    print("above the car deck, equipped with a window.")
elif input_class == "B":
    print("windowless cabin above the car deck.")
else:
    print("windowless cabin below the car deck.")



#2-3
input_hemoglobin = input("Enter biological gender(M or F):")

input_biological = float(input("Enter hemoglobin:"))

if input_hemoglobin == "F" and 117<=input_biological<=155 or input_hemoglobin == "M" and 134<=input_biological<=167:
    print("Normal")

elif input_hemoglobin == "F" and 117>input_biological or input_hemoglobin == "M" and 134>input_biological:
    print("Low")

else:
    print("High")


#2-4

input_year=int(input("Enter year:"))
if input_year%4==0 and input_year%100!=0 or input_year%400==0:
    print("This is a leap year.")
else:
    print("This is not a leap year.")

'''
