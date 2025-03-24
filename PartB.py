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