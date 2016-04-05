import unittest

ESPACOS_INTERNOS = {
    'a': 0,
    'b': 1,
    'c': 3,
    'd': 5,
}

def espaco_interno(letra):
    qtde = ESPACOS_INTERNOS.get(letra)
    return qtde * ' '

def espaco_externo(letra, posicao):
    if letra == 'd' and posicao == 'a':
        return '   '
    if letra == 'c' and posicao == 'a':
        return '  '
    if letra == 'b' and posicao == 'a':
        return ' '
    return ''

def interno(letra):
    espacos = espaco_interno(letra)
    if letra in ['b', 'c', 'd']:
        return '{}{}{}'.format(letra,espacos,letra)
    return letra

def linha(letra, posicao):
    espacos = espaco_externo(letra, posicao)
    if letra == 'd' and posicao == 'a':
        return '{}a'.format(espacos)
    if letra == 'c' and posicao == 'a':
        return '{}a'.format(espacos)
    if letra == 'b' and posicao == 'a':
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

    def test_linha_a(self):
        assert linha(letra='a', posicao='a') == 'a'

    def test_linha_letra_b_posicao_a(self):
        assert linha(letra='b', posicao='a') == ' a'

    def test_linha_letra_c_posicao_a(self):
        assert linha(letra='c', posicao='a') == '  a'

    def test_linha_letra_d_posicao_a(self):
        assert linha(letra='d', posicao='a') == '   a'

    def test_espaco_externo_letra_a_posicao_a(self):
        assert espaco_externo(letra='a', posicao='a') == ''

    def test_espaco_externo_letra_b_posicao_a(self):
        assert espaco_externo(letra='b', posicao='a') == ' '

    def test_espaco_externo_letra_c_posicao_a(self):
        assert espaco_externo(letra='c', posicao='a') == '  '

    def test_espaco_externo_letra_d_posicao_a(self):
        assert espaco_externo(letra='d', posicao='a') == '   '



if __name__ == '__main__':
    unittest.main()
