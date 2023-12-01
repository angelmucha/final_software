import unittest
from main import Cuenta, Operacion

class TestBilletera(unittest.TestCase):
    def test_obtener_contactos_exitoso(self):
        cuenta = Cuenta(numero="123", nombre="Luisa", saldo=400, contactos=["456"])
        contactos = cuenta.contactos
        self.assertEqual(contactos, ["456"])


    def test_obtener_contactos_error_cuenta_no_encontrada(self):
        cuenta = Cuenta(numero="123", nombre="Luisa", saldo=400, contactos=["456"])
        with self.assertRaises(Exception):
            contactos = cuenta.contactos_invalida  # Esto debería lanzar una excepción

    def test_realizar_pago_error_saldo_insuficiente(self):
        cuenta_origen = Cuenta(numero="123", nombre="Luisa", saldo=50, contactos=["456"])
        cuenta_destino = Cuenta(numero="456", nombre="Andrea", saldo=300, contactos=["123"])
        
        with self.assertRaises(Exception):
            cuenta_origen.pagar(destino="456", valor=100)  # Esto debería lanzar una excepción

    def test_realizar_pago_error_destino_invalido(self):
        cuenta_origen = Cuenta(numero="123", nombre="Luisa", saldo=400, contactos=["456"])
        cuenta_destino = Cuenta(numero="789", nombre="Otro", saldo=200, contactos=["999"])
        
        with self.assertRaises(Exception):
            cuenta_origen.pagar(destino="789", valor=50)  # Esto debería lanzar una excepción

if __name__ == '__main__':
    unittest.main()
