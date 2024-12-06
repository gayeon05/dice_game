import unittest
from dice_game import roll_dice

class MyTest(unittest.TestCase):
    def test_roll_dice(self):
        dice1,dice2=roll_dice()
        self.assertIn(dice1, range(1,7))
        self.assertIn(dice2, range(1,7))
        self.assertIn(dice1+dice2, range(2,13))    
if __name__ == '__main__': 
    unittest.main()