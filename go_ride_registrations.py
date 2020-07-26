import re
class Owner:
    def __init__(self,name,age,driving_license_number,license_validity_period,category,car_number,colour,company,model):
        self.name = name
        self.age = age
        self.driving_license_number = driving_license_number
        self.license_validity_period = license_validity_period
        self.car_object = Car(category,car_number,colour,company,model)
    def display_confirmation(self):
        print("\nThanks for using GoRide,Registration Successful !")

class Car:
    def __init__(self,category,car_number,colour,company,model):
        self.category = category
        self.car_number = car_number
        self.colour = colour
        self.company = company
        self.model = model

def registration():
    print("Welcome to GoRide !")
    name = input("Enter your name : ")
    age = input("Enter your age : ")
    while True:
        driving_license_number = input("Enter your driving license number : ")
        if re.match(r"([A-Z]{2}[0-9]{2})((19|20)[0-9][0-9])([0-9]{7})",driving_license_number):
            break
        else:
            print("please enter a valid license number")
    while True:
        license_validity_period = input("Enter your license validity (dd-mm-yyyy) : ")
        if re.match(r"(0[1-9]|[12][0-9]|3[01])[-](0[1-9]|1[012])[-](202[1-9])",license_validity_period):
            break
        else:
            print("please enter the valid date !")
    print("Select car category as micro- can accomodate upto 4 people / XL- can accomodate upto 10 people ")
    category = input("Enter your car category : ")
    car_number = input("Enter your car number : ")
    colour = input("Enter your car colour : ")
    company = input("Enter your car company : ")
    model = input("Enter your car model : ")
    
    owner_object = Owner(name,age,driving_license_number,license_validity_period,category,car_number,colour,company,model)
    owner_object.display_confirmation()
        
registration()

"""
Input and output :

Welcome to GoRide !
Enter your name : Pachai
Enter your age : 20
Enter your driving license number : AB2320001234567
Enter your license validity (dd-mm-yyyy) : 12-12-2022
Select car category as micro- can accomodate upto 4 people / XL- can accomodate upto 10 people 
Enter your car category : micro
Enter your car number : TN 01 23 4567
Enter your car colour : green
Enter your car company : honda
Enter your car model : city

Thanks for using GoRide,Registration Successful !

"""
        
    
