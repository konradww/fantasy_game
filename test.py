import unittest
import game_fantasy

inventory = {
    'element_1': 1,
    'element_2': 2,
   }
gift = ['element_2', 'element_2', 'element_1', 'element_2', 'element_4']
class TestGame(unittest.TestCase):
    def test_addToInventory(self):
        result = game_fantasy.addToInventory(inventory, gift)
        for v, k in result.items():
            if v == 'element_1':
                self.assertEqual(k, 2)
            elif v == 'element_2':
                self.assertEqual(k, 5)
            elif v == 'element_4':
                self.assertEqual(k, 1)

if __name__ == '__main__':
    unittest.main()
