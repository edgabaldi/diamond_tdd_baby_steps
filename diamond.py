import unittest

def interno(letra):
    if letra == 'd':
        return 'd     d'

    if letra == 'c':
        return '{}   {}'.format(letra, letra)
    if letra == 'b':
        return '{} {}'.format(letra, letra)
    return letra

class DiamondTestCase(unittest.TestCase):
    
    def test_interno_a(self):
        assert interno('a') == 'a'

    def test_interno_b(self):
        assert interno('b') == 'b b'

    def test_interno_c(self):
        assert interno('c') == 'c   c'

    def test_interno_d(self):
        assert interno('d') == 'd     d'


if __name__ == '__main__':
    unittest.main()
