class Driver:
    def __init__(self,name,age,driving_license_number,license_validity_period):
        self.name = name
        self.age = age
        self.driving_license_number = driving_license_number
        self.license_validity_period = license_validity_period

    def display_confirmation(self):
        print("\nThanks for using GoRide,Registration Successful !")

class Car:
    def __init__(self,category,car_number,colour,company,model):
        self.category = category
        self.car_number = car_number
        self.colour = colour
        self.company = company
        self.model = model

    def display_confirmation(self):
        print("\nThanks for using GoRide,Registration Successful !")

def is_driver(selection):
    if selection.lower() == "driver":
        return True


def registration():
    print("Welcome to GoRide !\nDo you want to  register as driver or owner ?")
    selection = input("select driver/owner :")
    if is_driver(selection):
        name = input("Enter your name : ")
        age = input("Enter your age : ")
        driving_license_number = input("Enter your driving license number : ")
        license_validity_period = input("Enter your license validity (dd - mm - yy) :")
        driver_object = name+age
        driver_object = Driver(name,age,driving_license_number,license_validity)
        driver_object.display_confirmation()                                
    else:
        print("Select car category as micro- can accomodate upto 4 people / XL- can accomodate upto 10 people")
        category = input("Enter your car category : ")
        car_number = input("Enter your car number : ")
        colour = input("Enter your car colour : ")
        company = input("Enter your car company : ")
        model = input("Enter your car model : ")
        car_object = Car(category,car_number,colour,company,model)
        car_object.display_confirmation()
        
registration()

"""
Input and output :

Welcome to GoRide !
Do you want to  register as driver or owner ?
select driver/owner :owner
Select car category as micro- can accomodate upto 4 people / XL- can accomodate upto 10 people
Enter your car category : XL
Enter your car number : TN 01 PA 1234
Enter your car colour : green
Enter your car company : honda
Enter your car model : city

Thanks for using GoRide,Registration Successful !

"""
        
    
