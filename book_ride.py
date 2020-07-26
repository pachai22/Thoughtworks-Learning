class Category:
    def __init__(self,type,range,price,with_ac):
        self.type = type
        self.with_ac = with_ac
        if self.with_ac == "yes":
            self.ac = Ac(type,range,price)
        else:
            self.non_ac = NonAc(type,range,price)


class Ac:
    def __init__(self,type,range,price):
        self.type = type
        self.range = range
        self.price = price

    def get_range(self):
        return self.range

    def get_price(self):
        return self.price

class NonAc:
    def __init__(self,type,range,price):
        self.type = type
        self.range = range
        self.price = price

    def get_range(self):
        return self.range

    def get_price(self):
        return self.price


def is_valid_category(type):
    category_list =[]
    for category in categories:
        category_list.append(category.type.lower())
    if type in category_list:
        return True
    else:
        return False
        
def filter_category(type):
    filtered_list = []
    for category in categories:
        if category.type.lower() == type:
            filtered_list.append(category)
    return filtered_list
            

def is_option_available(filtered_categories,with_ac_or_not):
    option_list =[]
    for filtered_category in filtered_categories:
        option_list.append(filtered_category.with_ac.lower())
    if with_ac_or_not in option_list:
        return option_list,True
    else:
        return option_list,False

def display_price(filtered_categories,with_ac_or_not):
    print("Range(km)    :   price/km")
    if with_ac_or_not == "yes":
        for option in filtered_categories:
            if option.with_ac == "yes":
                print(option.ac.get_range(),":",option.ac.get_price())
    else:
        for option in filtered_categories:
            if option.with_ac == "no":
                print(option.non_ac.get_range(),":",option.non_ac.get_price())
    print("Thanks for riding with us!")
        
    
    
def book_ride():
    while True:
        type = input("select any one of the above category : ")
        if is_valid_category(type):
            break
        else:
            print("please enter a valid category")
    filtered_categories = filter_category(type.lower())
    while True:
        with_ac_or_not = input("Do you want ac? (yes/no) : ")
        (option_list,selection) = is_option_available(filtered_categories,with_ac_or_not.lower())
        if selection:
            break
        else:
            print("Option not available,please select again !")
    display_price(filtered_categories,with_ac_or_not)
    
    
auto1 = Category("Auto",[0,15],10,"yes")
auto2 = Category("Auto",[16,30],8,"yes")
auto3 = Category("Auto",[31,1000],15,"yes")
micro1 = Category("Micro",[0,15],12,"yes")
micro2 = Category("Micro",[16,1000],10,"yes")
micro3 = Category("Micro",[0,15],14,"no")
micro4 = Category("Micro",[16,1000],12,"no")
xl1 = Category("XL",[0,15],14,"yes")
xl2 = Category("XL",[16,1000],14,"yes")
xl3 = Category("XL",[0,15],15,"no")
xl4 = Category("XL",[16,1000],15,"no")
categories = [auto1,auto2,auto3,micro1,micro2,micro3,micro4,xl1,xl2,xl3,xl4]
print("Welcome to GoRide!\n Auto : can accomodate upto 3 peole\n Micro : can accomodate upto 4 people\n XL : can accomodate upto 10 people")

book_ride()
        
   



