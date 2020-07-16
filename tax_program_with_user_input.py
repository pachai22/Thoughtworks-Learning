
class product:
    extra_tax = 0
    def __init__(self,id,name,price,category):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
        self.extra_tax = 0
        self.tax=0

    def calculate_tax(self):
        if self.category != "diary":
            if self.price >=500:
                self.tax = (5/100)*self.price
            else:
                self.tax = (2/100)*self.price
        return self.tax
            
class tax(product):
    def __init__(self,id,name,price,category):
        super().__init__(id,name,price,category)

    def additional_tax(self):
        if self.category == "textile":
            self.extra_tax = (1/100)* self.price
        elif self.category == "diary" and self.price >= 1000:
            self.extra_tax = (3/100)* self.price
        else:
            self.extra_tax = 0
        return self.extra_tax

def total_tax(object_name):
    print("The tax of the product",object_name.name,"is "+str(object_name.calculate_tax()+object_name.additional_tax()))
    
        
no_of_products = int(input("Enter the number of products :"))
print("Please follow the order id,name,price,category and select any one of the following category : diary,textile,produce,homeneeds")
objects=[]
for i in range(no_of_products):
    print("Enter the",i+1," th","product details one by one in new line :",end=" ")
    id = int(input())
    name = input()
    price = int(input())
    category = input()
    name = tax(id,name,price,category)
    objects.append(name)
    
for i in range(len(objects)):
    total_tax(objects[i])

"""
User input :

Enter the number of products :8
Please follow the order id,name,price,category and select any one of the following category : diary,textile,produce,homeneeds
Enter the 1  th product details one by one in new line : 1
milky
200
diary
Enter the 2  th product details one by one in new line : 2
kitkat
1500
diary
Enter the 3  th product details one by one in new line : 3
saree
1000
textile
Enter the 4  th product details one by one in new line : 4
chudi
350
textile
Enter the 5  th product details one by one in new line : 5
carrot
760
produce
Enter the 6  th product details one by one in new line : 6
chilli
60
produce
Enter the 7  th product details one by one in new line : 7
toordhal
400
homeneeds
Enter the 8  th product details one by one in new line : 8
uraddhal
600
homeneeds

Output:

The tax of the product milky is 0
The tax of the product kitkat is 45.0
The tax of the product saree is 60.0
The tax of the product chudi is 10.5
The tax of the product carrot is 38.0
The tax of the product chilli is 1.2
The tax of the product toordhal is 8.0
The tax of the product uraddhal is 30.0

"""
    
