import unittest

def interno(letra):
    return 'a'

class DiamondTestCase(unittest.TestCase):
    
    def test_interno_a(self):
        assert interno('a') == 'a'

if __name__ == '__main__':
    unittest.main()
