
class IceCream:
    def __init__(self,flavour,type,fcost,tcost,toppings):
        self.flavour = flavour
        self.type = type
        self.fcost = fcost
        self.tcost = tcost
        self.toppings = toppings
    def cost(self):
        if self.flavour == "chocolate":
            print("Chocolate flavour has toppings option :")
            for topping,cost in self.toppings.items():
                if topping != "no":
                    print(topping,":","Rs",cost)
            topping = input("\nChoose any one of the toppings mentioned above,Else type no : ")
            topping = topping.lower()
            return self.fcost + self.tcost + self.toppings[topping]
        else:
            return self.fcost + self.tcost
        
class IceCreamShop:
    def __init__(self,flavours,types,toppings):
        self.flavours =flavours
        self.types = types
        
        for flavour,fcost in flavours.items():
            for type,tcost in types.items():
                print(flavour+" "+type," "*(18-len(flavour+type)),fcost+tcost)
        
        print("\nChoose your favourite ice-cream :",end=" ")
        choice = input().split()
        quantity = int(input("Please enter the quantity in number : "))
        self.cost = IceCream(choice[0].lower(),choice[1].lower(),self.flavours[choice[0].lower()],self.types[choice[1].lower()],toppings)

        self.quantity = quantity
    def total_cost(self):
            total = self.cost.cost()*self.quantity
            return total



print("*-*-*Welcome to Green-icecream stall*-*-*")
print("*---------------MENU CARD---------------*\n")
print("ICE CREAM          COST\n")

flavours = {"vanilla" : 20,"strawberry" : 60,"chocolate" : 40}
types = {"stick" : 5,"cone" : 10,"cup" :15}
toppings ={"caramel" : 10,"choco chips" : 15,"nuts" : 13,"no" : 0}

ice_object = IceCreamShop(flavours,types,toppings)
print("The total cost is",ice_object.total_cost())

"""
Input and output :

*-*-*Welcome to Green-icecream stall*-*-*
*---------------MENU CARD---------------*

ICE CREAM          COST

vanilla stick        25
vanilla cone         30
vanilla cup          35
strawberry stick     65
strawberry cone      70
strawberry cup       75
chocolate stick      45
chocolate cone       50
chocolate cup        55

Choose your favourite ice-cream : chocolate cone
Please enter the quantity in number : 3
Chocolate flavour has toppings option :
caramel : Rs 10
choco chips : Rs 15
nuts : Rs 13

Choose any one of the toppings mentioned above,Else type no : caramel
The total cost is 180

"""
