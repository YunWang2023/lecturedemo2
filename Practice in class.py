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
'''
#3
import random
result = random.choice(["heads", "tails"])
while result  != "heads":
    print("Flipped", result)
    result = random.choice(["heads", "tails"])
print("Finally , flipped:", result )


"""

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
"""