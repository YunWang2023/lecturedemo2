'''

class Dog:
  count = 0
  def __init__(self, name, age):
    self.name = name
    self.age = age
    Dog.count = Dog.count + 1

  #Gasp method

# Setter and getter
  def change_name(self,name):
      self.name = name

  def getName(self):
      return self.name

  def getAge(self):
      return self.age

  def __str__(self):
      return f'{self.name},{self.age}'

mydog = Dog("Chick",3)
yourdog = Dog("Lily",2)
hisdog = Dog("Jack",1)
herdog = Dog("Lucy",5)

print(f"Dog's name :{mydog.name} is {mydog.age} years old")

mydog.change_name("Chick2")
yourdog.change_name("Lily2")

print(f"Dog's name :{mydog.name} is {mydog.age} years old")

print(mydog.getAge())

print(str(mydog))

print(f'There are {Dog.count} dogs in all.')

class Nursing:
    
    def __init__(self):
        self.dogs = []

    def addDog(self,name):
        self.dogs.append(Dog(name))
        print(f"the {self.dogs} is added")

    def getDog(self):
        for dog in self.dogs:
            print(dog.getName(),dog.getAge())


class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        pass

    def get_name(self):
        return self.name

    def set_name(self,name):
        self.name = name

class Student(Person):
    def __init__(self,name,age,gender,student_id):
        super().__init__(name,age,gender)
        self.student_id = student_id

    def introduce(self):
        return f"{self.student_id},{self.name},{self.age},{self.gender}"

class Teacher(Person):
    def __init__(self,name,age,gender,teacher_title):
        super().__init__(name,age,gender)
        self.teacher_title = teacher_title

    def introduce(self):
        return f"{self.teacher_title},{self.name},{self.age},{self.gender}"

class Assistant(Teacher):
    def __init__(self,name,age,gender,teacher_title,monthly_salary):
        super().__init__(name,age,gender,teacher_title)
        self.monthly_salary = monthly_salary

    def introduce(self):
        return f"Assistant:{self.name},{self.age},{self.gender},{self.teacher_title}, and monthly salary:{self.monthly_salary}"

class Parttime_teacher(Teacher):
    def __init__(self,name,age,gender,teacher_title,hourly_salary):
        super().__init__(name,age,gender,teacher_title)
        self.hourly_salary = hourly_salary

    def introduce(self):
        return f"PartTime:{self.name},{self.age},{self.gender},{self.teacher_title}, and hourly salary:{self.hourly_salary}"


assistants=[]
assistant1 = Assistant("Lily",22,"F","math",2000)
assistants.append(assistant1)

parttime_teachers = []
parttime_teachers1 = Parttime_teacher("Chick",35,"M","finnish",15)
parttime_teachers.append(parttime_teachers1)

for i in assistants:
    print(i.introduce())

for i in parttime_teachers:
    print(i.introduce())


#------------------------------------
class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        return f"{self.name} , {self.age} ,{self.gender}"
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getGender(self):
        return self.gender


class Teacher:
    def __init__(self,teacher_title):


#_______________________________

import json
import requests

keyword = input("Enter keyword: ")

# Request template: https://api.tvmaze.com/search/shows?q=girls
request = "https://api.tvmaze.com/search/shows?q=" + keyword

try:
    response = requests.get(request)
    if response.status_code==200:
        json_response = response.json()
        # print(json.dumps(json_response, indent=2))
        for a in json_response:
            print(a["show"]["name"])
except requests.exceptions.RequestException as e:
    print ("Request could not be completed.")

'''

class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def introduce(self):
        return f"I am {self.name},{self.age}years old,{self.gender}"

class Member(Person):
    def __init__(self,name,age,gender,membership_id):
        super.__init__(name,age,gender)
        self.membership_id = membership_id
    def introduce(self):
        return f"I am {self.name},{self.age}years old,{self.gender} with membership_id: {self.membership_id}"

class Author(Person):
    def __init__(self,name,age,gender,books_written):
        super.__init__(name,age,gender)
        self.books_written = books_written
    def list_books(self):
        list_books = []
        list_books.append(self.books_written)
        return f"Books written:{list_books}"

class AuthorMember(Member,Author):
    def __init__(self,membership_id,books_written):
        Member.__init__(self,membership_id)
        Author.__init__(self,books_written)

    def introduce(self):
        return f"I am {self.name},{self.age}years old,{self.gender} with membership_id: {self.membership_id}. Books written:{self.list_books}"

#Main
person1 = Person("Chick",35,"M")
person2 = Person("Lily",22,"F")
person3 = Person("Lucy",40,"M")

print(person1.introduce())
print(person2.introduce())
print(person3.introduce())




