class Student:
    count = 0
    department = "ICT"
    def __init__(self, name, age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        Student.count = Student.count + 1
        self.email = f'{self.name}@metropolia.fi'
        self.courses = []

# setter and getter
    def __str__(self):
        return f'{self.name} {self.age} {self.gender}'

    def getName(self):
        return self.name.upper()

    def getAge(self):
        return self.age

    def getGender(self):
        return self.gender

    def setAge(self, age):
        self.age = age

    def setGender(self, gender):
        self.gender = gender

    def setName(self, name):
        self.name = name


Hou = Student("Hou Wenhuang",30,"M")
Yan = Student('Yan Xin',20,'M')
Wu = Student('Wu Zongyan',22,'M')
Luo = Student('Luo Ying',25,'F')

print(f"Hou's name is {Hou.getName()},and age is {Hou.getAge()}.")

Hou.setName('How Wenhuang2')

print(f"Hou's new mew name is {Hou.getName()},{Student.department}")
print(str(Hou))
print(f'There are {Student.count} students in the classroom.')
print(Hou.email)
#

class Course:
    def __init__(self,name):
        self.name = name
        self.students = []

    def students_add(self, student):
        self.students.append(student)
        print(student.name + "is added to " + self.name)
        return

    def students_remove(self, student):
        self.students.remove(student)
        print(student.name + "is removed from" + self.name)
        return

class Student:

    def setage(self,age):
        self.age = age
        return self.age

    def setgender(self,gender):
        self.gender = gender
        return self.gender

    def enrollCourse(self,course):



course1=