class Flavour:
    def __init__(self,flavour,fcost):
        self.__flavour = flavour
        self.__fcost = fcost

    def get_flavour_cost(self):
        return self.__fcost

    def get_flavour_name(self):
        return self.__flavour

class Type:
    def __init__(self,type,tcost):
        self.__type = type
        self.__tcost = tcost

    def get_type_cost(self):
        return self.__tcost

    def get_type_name(self):
        return self.__type

class Icecream:
    def __init__(self,flavour,fcost,type,tost):
        self.flavour_object = Flavour(flavour,fcost)
        self.type_object = Type(type,tcost)

    def total_cost(self,quantity):
        return (self.flavour_object.get_flavour_cost()+self.type_object.get_type_cost())*quantity

    def total_with_topping_cost(self,quantity,toppings):
        print("Chocolate flavour has toppings option :")
        for topping,cost in toppings.items():
            if topping != "no":
                print(topping,":","Rs",cost)
        topping = input("\nChoose any one of the toppings mentioned above,Else type no : ")
        topping = topping.lower()
        return (self.flavour_object.get_flavour_cost()+self.type_object.get_type_cost()+toppings[topping])*quantity

        
def menucard(icecream_objects):
    for icecream_object in icecream_objects:
        print(icecream_object.flavour_object.get_flavour_name()+" "+icecream_object.type_object.get_type_name()," "*(18-len(icecream_object.flavour_object.get_flavour_name()+icecream_object.type_object.get_type_name())),icecream_object.flavour_object.get_flavour_cost()+icecream_object.type_object.get_type_cost())


    
flavours = {"vanilla" : 20,"strawberry" : 60,"chocolate" : 40}
types = {"stick" : 5,"cone" : 10,"cup" :15}
toppings ={"caramel" : 10,"choco chips" : 15,"nuts" : 13,"no" : 0}
icecream_objects =[]
for flavour,fcost in flavours.items():
    for type,tcost in types.items():
        icecream_object = flavour+" "+type
        icecream_object = Icecream(flavour,fcost,type,tcost)
        icecream_objects.append(icecream_object)

        
print("*-*-*Welcome to Green-icecream stall*-*-*")
print("*---------------MENU CARD---------------*\n")
print("ICE CREAM          COST\n")
menucard(icecream_objects)
print("\nChoose your favourite ice-cream :",end=" ")
choice = input().split()
quantity = int(input("Please enter the quantity in number : "))
for icecream_object in icecream_objects:
    if icecream_object.flavour_object.get_flavour_name() == choice[0].lower() and icecream_object.type_object.get_type_name() == choice[1].lower():
        if choice[0].lower() == "chocolate":
            print("The total cost is",icecream_object.total_with_topping_cost(quantity,toppings))
            
        else:
            print("The total cost is",icecream_object.total_cost(quantity))

