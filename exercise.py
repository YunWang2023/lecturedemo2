
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
    def __init__(self,name,age,gender,membership_id,books_written):
        Member.__init__(self,membership_id)
        Author.__init__(self,books_written)

    def introduce(self):
        return f"I am {self.name},{self.age}years old,{self.gender} with membership_id: {self.membership_id}. Books written:{self.list_books}"
