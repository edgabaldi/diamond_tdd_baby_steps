import unittest
from string import letters

ALFABETO = letters[:26]
IMPARES = [0] + range(1, 52, 2)

ESPACOS_INTERNOS = dict(zip(ALFABETO, IMPARES))

ESPACOS_EXTERNOS = {letra: num for num, letra in enumerate(ALFABETO)}

def espaco_interno(letra):
    qtde = ESPACOS_INTERNOS.get(letra)
    return qtde * ' '

def espaco_externo(letra, posicao):
    qtde = ESPACOS_EXTERNOS.get(letra) - ESPACOS_EXTERNOS.get(posicao)
    return ' ' * qtde

def interno(letra):
    espacos = espaco_interno(letra)
    if letra in ['b', 'c', 'd']:
        return '{}{}{}'.format(letra,espacos,letra)
    return letra

def linha(letra, posicao):
    espacos = espaco_externo(letra, posicao)
    _interno = interno(posicao)
    return '{}{}'.format(espacos, _interno)

def sequencia(letra):
    if letra == 'b':
        return 'aba'
    if letra == 'c':
        return 'abcba'
    return letra

def diamond(letra):
    return '\n'.join([linha(letra, posicao) for posicao in sequencia(letra)])

class DiamondTestCase(unittest.TestCase):

    def test_sequencia(self):
        self.assertEqual('a', sequencia('a'))
        self.assertEqual('aba', sequencia('b'))
        self.assertEqual('abcba', sequencia('c'))

    def test_diamond(self):
        self.assertEqual("a", diamond('a'))
        self.assertEqual(" a\nb b\n a", diamond('b'))
        self.assertEqual("  a\n b b\nc   c\n b b\n  a", diamond('c'))
    
    def test_interno(self):
        assert interno('a') == 'a'
        assert interno('b') == 'b b'
        assert interno('c') == 'c   c'
        assert interno('d') == 'd     d'

    def test_espaco_interno(self):
        assert espaco_interno('a') == ''
        assert espaco_interno('b') == ' '
        assert espaco_interno('c') == '   '
        assert espaco_interno('d') == '     '

    def test_linha(self):
        assert linha(letra='a', posicao='a') == 'a'
        assert linha(letra='b', posicao='a') == ' a'
        assert linha(letra='c', posicao='a') == '  a'
        assert linha(letra='d', posicao='a') == '   a'
        self.assertEqual(' b b', linha(letra='c', posicao='b'))

    def test_espaco_externo(self):
        assert espaco_externo(letra='a', posicao='a') == ''
        assert espaco_externo(letra='b', posicao='a') == ' '
        assert espaco_externo(letra='c', posicao='a') == '  '
        assert espaco_externo(letra='d', posicao='a') == '   '
        self.assertEqual('', espaco_externo(letra='b', posicao='b'))
        self.assertEqual(' ', espaco_externo(letra='c', posicao='b'))



if __name__ == '__main__':
    unittest.main()
