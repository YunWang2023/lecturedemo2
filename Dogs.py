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

