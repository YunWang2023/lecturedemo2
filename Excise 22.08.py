

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

num1=random.randint(0,9)
num2=random.randint(0,9)
num3=random.randint(0,9)

print(f"3-digit code is: {num1}{num2}{num3}")

num4_1=random.randint(1,6)
num4_2=random.randint(1,6)
num4_3=random.randint(1,6)
num4_4=random.randint(1,6)


print(f"4-digit code is: {num4_1}{num4_2}{num4_2}{num4_4}")
