#A2
class House:
    def __init__(self, house_number, street, area, number_of_beds, price):
        self.house_number = house_number  
        self.street = street
        self.area = area
        self.number_of_beds = number_of_beds
        self.price = price 
        
#A3 Mtehod to print atributes
def display_info(self):
    print(f"House Info No: {self.house_number}, Street: {self.street}, Area: {self.area}, Beds: {self.number_of_beds}, Price: €{self.price}")
    
 #A4 Method to update atributes
def update_house_number(self, new_number):
     if isinstance(new_number, int):
         self.house_number = new_number
     else:
        print("housenumber must be an integer.")
        
def update_street(self, new_street):
        if isinstance(new_street, str):
            self.street = new_street
        else:
            print("street must be a string.")
            
def update_area(self, new_area):
    if isinstance(new_area, str):
     self.area = new_area
    else:
         print("area must be a string.")
        
def update_number_of_beds(self, new_beds):
    if isinstance(new_beds, int):
        self.number_of_beds = new_beds
    else:
        print("number_of_beds must be an integer.")
        
def update_price(self, new_price):
    if isinstance(new_price, (int, float)):
        self.price = new_price
    else:
        print("price must be a number.")
        
        
#A5 Im doing Rental House
class RentalHouse(House):
 def __init__(self, house_number, street, area, number_of_beds, price, monthly_rent, is_furnished):
        super().__init__(house_number, street, area, number_of_beds, price)
        self.monthly_rent = monthly_rent
        self.is_furnished = is_furnished
        
#A6 Method to print all the attributes
def display_full_info(self):
        super().display_info()
        print(f"Rental Info -> Rent: €{self.monthly_rent}/month, Furnished: {'Yes' if self.is_furnished else 'No'}")
        
#A7 Updating Methods for extra attributes
def update_montly_rent(self, new_rent):
        if isinstance(new_rent, (int,float)):
            self.montly_rent = new_rent
        else:
         print("monthly rent must be a number.")
         
def update_is_furnished(self, furnished_status):
        if isinstance(furnished_status, bool):
            self.is_furnished = furnished_status
        else:
            print("is_furnished must be a boolean value (True or False).")
            

#A8 Creating Instances
my_house = House(23, "Elm Street", "Dublin 8", 3, 350000)
rental = RentalHouse(50, "Pine avenue", "Dublin 5", 2, 280000, 1500, True)

#A9 Calling the display method
print("Displaying House Info:")
my_house.display_info()

print("\nDisplaying Rental House Info:")
rental.display_full_info()

#A10 Performing updates on the base class
print("\n--- Updating House ---")
my_house.update_price(350000)
my_house.update_number_of_beds(3)
my_house.display_info()

# A10: Perform updates on child class (2 examples)
print("\n--- Updating Rental House ---")
rental.update_monthly_rent(280000)
rental.update_is_furnished(False)
rental.display_full_info()