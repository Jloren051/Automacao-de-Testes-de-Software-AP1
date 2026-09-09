import unittest

def calcular_media(nota1, nota2):
    if nota1 < 0 or nota2 < 0:
        raise ValueError("As notas não podem ser negativas.")

    if not isinstance(nota1, (int, float)) or not isinstance(nota2, (int, float)):
        raise TypeError("As notas devem ser números.")

    return (nota1 + nota2) / 2



class TestCalcularMedia(unittest.TestCase):

    # Teste funcional
    def test_calcular_media(self):
        resultado = calcular_media(8, 6)

        self.assertEqual(resultado, 7)

    # Teste de ValueError
    def test_nota_negativa(self):
        with self.assertRaises(ValueError):
            calcular_media(-5, 8)

    # Teste de TypeError
    def test_nota_invalida(self):
        with self.assertRaises(TypeError):
            calcular_media("8", 6)


if __name__ == '__main__':
    unittest.main()