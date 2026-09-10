import unittest

def calcular_desconto(valor):
    if valor <= 0:
        raise ValueError("O valor da compra deve ser maior que zero.")

    if valor <= 100:
        return valor

    if valor <= 500:
        return valor * 0.90

    return valor * 0.80


class TestCalculadoraDesconto(unittest.TestCase):

    def test_compra_ate_100_nao_recebe_desconto(self):
        self.assertEqual(calcular_desconto(100), 100)

    def test_compra_50_nao_recebe_desconto(self):
        self.assertEqual(calcular_desconto(50), 50)

    def test_compra_acima_100_recebe_10_porcento(self):
        self.assertEqual(calcular_desconto(200), 180)

    def test_compra_de_500_recebe_10_porcento(self):
        self.assertEqual(calcular_desconto(500), 450)

    def test_compra_acima_500_recebe_20_porcento(self):
        self.assertEqual(calcular_desconto(600), 480)

    def test_valor_zero_lanca_value_error(self):
        with self.assertRaises(ValueError):
            calcular_desconto(0)

    def test_valor_negativo_lanca_value_error(self):
        with self.assertRaises(ValueError):
            calcular_desconto(-100)


if __name__ == "__main__":
    unittest.main()


DESCONTO_10 = 0.10
DESCONTO_20 = 0.20

LIMITE_SEM_DESCONTO = 100
LIMITE_DESCONTO_10 = 500


def calcular_desconto(valor):
    """Calcula o valor final da compra conforme as regras de desconto."""

    if valor <= 0:
        raise ValueError("O valor da compra deve ser maior que zero.")

    percentual = _obter_desconto(valor)

    return valor * (1 - percentual)


def _obter_desconto(valor):
    if valor <= LIMITE_SEM_DESCONTO:
        return 0

    if valor <= LIMITE_DESCONTO_10:
        return DESCONTO_10

    return DESCONTO_20