from abc import ABC, abstractmethod

class CupCake(ABC):
    size = "regular"
    def __init__(self, name, price, flavor, filling, frosting):
        self.name = name
        #expect float for price
        self.price = price
        self.flavor = flavor
        self.filling = filling
        self.frosting = frosting 
        #expect boolean for sprinkles
        self.sprinkles = []
    
    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)

    @abstractmethod 
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


my_cupcake = CupCake('Cookie dough', 3.50, 'vanilla', 'cookie dough', 'butter cream', False)
my_cupcake.add_sprinkles('cookie crumble', 'oreo crumble', 'chocolate')
my_cupcake.filling = "chocolate chip cookie dough"
my_cupcake.frosting = "whiped cream"

my_cupcake_mini = Mini("Chocolate", 1.99, "Chocolate", "White")

print(my_cupcake.sprinkles)
print(my_cupcake.filling)

print(my_cupcake_mini.name)
print(my_cupcake_mini.size)
print(my_cupcake_mini.price)