
class student:
    #     constractor
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        # Method
    def display(self):
             print(self.first_name, self.last_name)
# object

my_student = student('john', 'smith')
my_student.display()
my_student2 = student('clinton', 'vivvan')
my_student2.display()
my_student3 = student('Elly', 'smith')
my_student3.display()
my_student4 = student('vivian', 'viv')
my_student4.display()
my_student5 = student('Capello', 'Captain')