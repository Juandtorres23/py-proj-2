class CupCake():
    def __init__(self, name, price, flavor, filling, frosting, sprinkles):
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

my_cupcake = CupCake('Cookie dough', 3.50, 'vanilla', 'cookie dough', 'butter cream', False)
my_cupcake.add_sprinkles('cookie crumble', 'oreo crumble', 'chocolate')
my_cupcake.filling = "chocolate chip cookie dough"
my_cupcake.frosting = "whiped cream"

print(my_cupcake.sprinkles)
print(my_cupcake.filling)
