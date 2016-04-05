import unittest

def interno(letra):
    if letra == 'b':
        return 'b b'
    return letra

class DiamondTestCase(unittest.TestCase):
    
    def test_interno_a(self):
        assert interno('a') == 'a'

    def test_interno_b(self):
        assert interno('b') == 'b b'

if __name__ == '__main__':
    unittest.main()
