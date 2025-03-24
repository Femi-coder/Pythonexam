import unittest
from PartA import House, RentalHouse

class TestHouseClasses(unittest.TestCase):
    
    def setUp(self):
        self.house1 = House(2,"Banana Ireland","Dublin 1", 3, 400000)
        self.rental1 = RentalHouse(70, "Castletown", "Dublin 10", 5, 400000, 1400, True)
        
#B2 Testing if object is in instance of class
def test_is_instance(self):
    self.assertIsInstance(self.house1, House)
    self.assertIsInstance(self.rental1, RentalHouse)
    self.assertIsInstance(self.rental1, House)
    
# B3: Test if object is NOT an instance of a class
def test_is_not_instance(self):
        self.assertNotIsInstance(self.house1, RentalHouse)
        
# B4: Testing if 2 objects are identical
def test_objects_identity(self):
    same_house = self.house1
    self.assertsIs(self.house1, same_house)
    
    another_house = House(2,"Banana Ireland","Dublin 1", 3, 400000)
    self.assertIsNot(self.house1, another_house)
    
#B5 Testing update methods in house
def test_update_methods(self):
    self.house1.update_price(420000)
    self.assertEqual(self.house1.price, 420000)

    self.house1.update_number_of_beds(4)
    self.assertEqual(self.house1.number_of_beds, 4)

    self.house1.update_street("Updated Street")
    self.assertEqual(self.house1.street, "Updated Street")

    self.house1.update_area("Dublin 5")
    self.assertEqual(self.house1.area, "Dublin 5")

    self.house1.update_house_number(202)
    self.assertEqual(self.house1.house_number, 202)
    
#B5 Testing Updates in the rental house part
def test_update_rental_methods(self):
        self.rental1.update_monthly_rent(1600)
        self.assertEqual(self.rental1.monthly_rent, 1600)

        self.rental1.update_is_furnished(False)
        self.assertFalse(self.rental1.is_furnished)
    
