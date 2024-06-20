class Person:
    def __init__(self,first_name,last_name, age):
        self.first_name = first_name
        self.last_name= last_name
        self.age = age
    def print_name(self):
        print(f"My name is {self.first_name} {self.last_name}, I am {self.age} years")

class Student(Person):
    def __init__(self,first_name,last_name, age,):
        super().__init__(first_name,last_name,age)


myStudent = Student("Flex","Flow",9632)
myStudent.print_name()
myStudent2 = Student("Flex","Flow",14)
myStudent2.print_name()
myStudent3 = Student("Flex","Flow",25)
myStudent3.print_name()



