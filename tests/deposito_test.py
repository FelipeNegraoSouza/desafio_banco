import unittest
from app.models.conta import ContaBancaria
from app.services.deposito import depositar

# python -m unittest tests.deposito_test

class TestDeposito(unittest.TestCase):
    def setUp(self):
        self.conta = ContaBancaria(
            numero="12345",
            agencia="001",
            banco="Banco A",
            saldo=1000.0,
            senha="1234"
        )

    def test_deposito_valido(self):
        """Teste para depósito válido."""
        saldo_antes = self.conta.saldo
        valor_deposito = 200.0
        novo_saldo = depositar(self.conta, valor_deposito)
        self.assertEqual(novo_saldo, saldo_antes + valor_deposito)
        self.assertEqual(self.conta.saldo, saldo_antes + valor_deposito)

    def test_deposito_invalido_valor_negativo(self):
        """Teste para depósito com valor negativo."""
        valor_deposito = -100.0
        with self.assertRaises(ValueError):
            depositar(self.conta, valor_deposito)

    # TODO: Verificar o motivo do erro de tipo_incorreto.
    def test_deposito_invalido_tipo_incorreto(self):
        """Teste para depósito com tipo de valor incorreto."""
        valor_deposito = "120"  # Tipo incorreto (string)
        with self.assertRaises(ValueError) as context:
            depositar(self.conta, valor_deposito)
        self.assertEqual(str(context.exception), "O valor deve ser um número válido.")

if __name__ == "__main__":
    unittest.main()
