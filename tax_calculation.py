class Product:
    extra_tax = 0
    def __init__(self,id,name,price,category):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
        self.extra_tax = 0
        self.tax = 0

    def calculate_tax(self):
        if self.category != "diary":
            if self.price >=500:
                self.tax = (5/100)*self.price
            else:
                self.tax = (2/100)*self.price
        return self.tax

    def additional_tax(self):
        if self.category == "textile":
            self.extra_tax = (1/100)* self.price
        elif self.category == "diary" and self.price>=1000:
            self.extra_tax = (3/100)* self.price
        else:
            self.extra_tax = 0
        return self.extra_tax

def total(*object_names):
    for product in object_names:
        amount = product.calculate_tax()+ product.additional_tax()
        print("The tax of the product",product.name," is ",amount,"rupees")
        


milky_bar = Product(1,"Milky Bar",200,"diary")
kitkat = Product(2,"Kitkat",1500,"diary")
saree = Product(3,"Saree",1000,"textile")
chudi = Product(4,"Chudi",350,"textile")
carrot = Product(5,"Carrot",760,"produce")
chilli = Product(6,"Chilli",60,"produce")
toor_dhal = Product(7,"Toor_dhal",400,"homeneeds")
urad_dhal = Product(8,"Urad dhal",600,"homeneeds")

total(milky_bar,kitkat,saree,chudi,carrot,chilli,toor_dhal,urad_dhal)

"""
Output:

The tax of the product Milky Bar  is  0 rupees
The tax of the product Kitkat  is  45.0 rupees
The tax of the product Saree  is  60.0 rupees
The tax of the product Chudi  is  10.5 rupees
The tax of the product Carrot  is  38.0 rupees
The tax of the product Chilli  is  1.2 rupees
The tax of the product Toor_dhal  is  8.0 rupees
The tax of the product Urad dhal  is  30.0 rupees

"""
