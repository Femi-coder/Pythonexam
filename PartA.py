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