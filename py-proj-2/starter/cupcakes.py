import csv
from pprint import pprint

def read_csv(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            pprint(row)




from abc import ABC, abstractmethod

class CupCake(ABC):
    size = "regular"

    def __init__(self, name, price, flavor, frosting, filling,):
        self.name = name
        #expect float for price
        self.price = price
        self.flavor = flavor
        self.frosting = frosting 
        #expect boolean for sprinkles
        self.sprinkles = []
    
    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)

    @abstractmethod 
    def calculate_price(self, quantity):
        return quantity * self.price


class Regular(CupCake):
    size = "regular"

    def __init__(self, name, price, flavor, frosting):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []

    def calculate_price(self, quantity):
        return quantity * self.price


class Mini(CupCake):
    size = "mini"

    def __init__(self, name, price, flavor, frosting):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []

    def calculate_price(self, quantity):
        return quantity * self.price

class Large(CupCake):
    size = "large"

    def __init__(self, name, price, flavor, frosting):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []

    def calculate_price(self, quantity):
        return quantity * self.price

cupcake1 = Regular("Stars and Stripes", 2.99, "Vanilla", "Vanilla")
cupcake1.add_sprinkles("Red", "White", "Blue")
cupcake2 = Mini("Oreo", .99, "Chocolate", "Cookies and Cream")
cupcake2.add_sprinkles("Oreo pieces")
cupcake3 = Large("Red Velvet", 3.99, "Red Velvet", "Cream Cheese")
cupcake4 = Regular("Guava King", 3.20, "Vanilla", "Guava paste")
cupcake5 = Large("Cheese Cake", 4.20, "Vanilla", "Creame Cheese")
cupcake5.add_sprinkles("Pie crust")

cupcake_list = [
    cupcake1,
    cupcake2,
    cupcake3,
    cupcake4,
    cupcake5
]


def write_new_csv(file, cupcakes):
    with open(file, "w", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price","flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "filling":cupcake.filling, "sprinkles": cupcake.sprinkles})
            else:
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})



# def add_cupcake(file, cupcake):
#     with open(file, 'a', newline="\n") as csvfile:
#         fieldnames = ["size", "name", "price","flavor", "frosting", "sprinkles", "filling"]
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#         if hasattr(cupcake, "filling"):
#             writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "filling":cupcake.filling, "sprinkles": cupcake.sprinkles})
#         else:
#             writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})

def get_cupcakes(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
        return reader

def find_cupcake(file, name):
    for cupcake in get_cupcakes(file):
        if cupcake["name"] == name:
            return cupcake
    return None

def add_cupcake_dictionary(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(cupcake)




















# write_new_csv("cupcakes.csv", cupcake_list)

# This was a call to create the order.csv file

# with open("order.csv", "w", newline="\n") as csvfile:
#         fieldnames = ["size", "name", "price","flavor", "frosting", "sprinkles", "filling"]
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#         writer.writeheader()