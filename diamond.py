import unittest

ESPACOS_INTERNOS = {
    'a': 0,
    'b': 1,
    'c': 3,
    'd': 5,
}

ESPACOS_EXTERNOS = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
}

def espaco_interno(letra):
    qtde = ESPACOS_INTERNOS.get(letra)
    return qtde * ' '

def espaco_externo(letra, posicao):
    qtde = ESPACOS_EXTERNOS.get(letra)
    return ' ' * qtde

def interno(letra):
    espacos = espaco_interno(letra)
    if letra in ['b', 'c', 'd']:
        return '{}{}{}'.format(letra,espacos,letra)
    return letra

def linha(letra, posicao):
    espacos = espaco_externo(letra, posicao)
    if posicao == 'a':
        if letra == 'd':
            return '{}{}'.format(espacos, posicao)
        if letra == 'c':
            return '{}{}'.format(espacos, posicao)
        if letra == 'b':
            return ' a'
    return 'a'

class DiamondTestCase(unittest.TestCase):
    
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

    def test_espaco_externo(self):
        assert espaco_externo(letra='a', posicao='a') == ''
        assert espaco_externo(letra='b', posicao='a') == ' '
        assert espaco_externo(letra='c', posicao='a') == '  '
        assert espaco_externo(letra='d', posicao='a') == '   '



if __name__ == '__main__':
    unittest.main()
