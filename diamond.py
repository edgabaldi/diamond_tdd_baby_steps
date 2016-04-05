import unittest

def espaco_interno(letra):
    if letra == 'd':
        return '     '
    if letra == 'c':
        return '   '
    if letra == 'b':
        return ' '
    return ''

def interno(letra):
    espacos = espaco_interno(letra)
    if letra in ['b', 'c', 'd']:
        return '{}{}{}'.format(letra,espacos,letra)
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

    def test_espaco_interno_a(self):
        assert espaco_interno('a') == ''

    def test_espaco_interno_b(self):
        assert espaco_interno('b') == ' '

    def test_espaco_interno_c(self):
        assert espaco_interno('c') == '   '

    def test_espaco_interno_d(self):
        assert espaco_interno('d') == '     '


if __name__ == '__main__':
    unittest.main()
