class IceCream:
    stick = 5
    cone = 10
    cup = 15
    vanilla = 20
    chocolate = 40
    strawberry = 60
    def __init__(self,flavour,shape):
        self.flavour = flavour
        self.shape = shape
    def cost(self):
        return getattr(ice_object,self.flavour) + getattr(ice_object,self.shape)
        

class Chocolate(IceCream):
    chocochips = 15
    caramel = 10
    nuts = 13
    no = 0
    def __init__(self,flavour,shape):
        super().__init__(flavour,shape)
    def toppings(self):
        topping = input("\nChocolate flavour has topping options as chocochips :Rs 15,caramel :Rs 10,nuts :Rs 13 !\nChoose any one of the toppings mentioned above,Else type no : ")
        topping = topping.lower()
        return getattr(ice_object,topping)
            

print("*-*-*Welcome to Green-icecream stall*-*-*")
print("*---------------MENU CARD---------------*\n")
print("ICE CREAM          flavour+type    COST\nChocolate stick    40+5           Rs 45\nChocolate cone     40+10          Rs 50\nChocolate cup      40+15          Rs 55\nVanilla stick      20+5           Rs 25\nVanilla cone       20+10          Rs 30\nVanilla cup        20+15          Rs 35\nStrawberry stick   60+5           Rs 65\nStrawberry cone    60+10          Rs 70\nStrawberry cup     60+15          Rs 75")
print("\nChoose your favourite ice-cream :",end=" ")
choice = input().split()
ice_object = Chocolate(choice[0].lower(),choice[1].lower())
if choice[0].lower() != "chocolate":
    print("The cost of ice-cream is : Rs",ice_object.cost())
else:
    print("The cost of ice-cream is : Rs",ice_object.cost()+ice_object.toppings())
