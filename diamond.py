import unittest

def interno(letra):
    return letra

class DiamondTestCase(unittest.TestCase):
    
    def test_interno_a(self):
        assert interno('a') == 'a'

if __name__ == '__main__':
    unittest.main()
