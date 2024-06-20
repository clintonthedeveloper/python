# CREATE A CLASS CARS WITH THE FOLLOWING ATTRIBUTES
# MODEL, YEAR OF MANUFATURE, TYPE, COLOR

# CREATE A METHOD TO PRINT
# MY DREAN CAR IS..MANUFUCTURE IN...BEING A...TYPE..COLR
# UTOLIZE AT LIST 5 OBJECTS

class cars:
    def __init__(self, model, year , color, Type):
        self.model = model
        self.year = year
        self.color = color
        self.Type = Type
    def display(self):
        print(f" My dream car is {self.model} and the year is {self} and color is {self.color}")
car1 = cars("Ford",2000,"red","SUV")
car1.display()
car2 = cars("Lanica ",2011,"red","Delta Gold")
car2.display()
car3 = cars("Honda",2000,"blue","EX sedan")
car3.display()
car4 = cars("Tesla",2000,"blue","")
car4.display()

#
class fruits:
    def __init__(self, name, price, color):
        self.name = name
        self.price = price
        self.color = color

    def display(self):
        print(f" My fruit is {self.name} and the color is{self.color} and the price is {self.price}")
fruit1 = fruits("banana",5,"yello")
fruit1.display()
fruit2 = fruits("watermelon",3,"red")
fruit2.display()
fruit3 = fruits("mango",20,"blue")
fruit3.display()