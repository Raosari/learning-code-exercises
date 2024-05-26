import unittest
import main

class TestMain(unittest.TestCase):
    def test_simple_5(self):
        test_param = 1
        result = main.simple_5(test_param)
        self.assertEqual(result,6)
    

    def test2_simple_5(self):
        test_param = 'adwlnkwd'
        result = main.simple_5(test_param)
        self.assertIsInstance(result,TypeError)
    
    def test3_simple_5(self):
        test_param = 0
        result = main.simple_5(test_param)
        self.assertEqual(result,5)

if __name__ == '__main__':
    unittest.main()
