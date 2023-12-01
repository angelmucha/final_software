import unittest
from main import Cuenta, Operacion

class TestBilletera(unittest.TestCase):
    
    # Este test verifica que la función 'contactos' de la clase 'Cuenta' 
    # devuelve correctamente la lista de contactos de la cuenta.
    def test_obtener_contactos_exitoso(self):
        cuenta = Cuenta(numero="123", nombre="Luisa", saldo=400, contactos=["456"])
        contactos = cuenta.contactos
        self.assertEqual(contactos, ["456"])

    #Se está probando el escenario en el que se intenta realizar un depósito con un monto negativo en la cuenta de origen
    def test_depositar_monto_negativo(self):
        cuenta_origen = Cuenta(numero="123", nombre="Luisa", saldo=400, contactos=["456"])

        with self.assertRaises(ValueError):
            cuenta_origen.depositar(-50)

    # Este test verifica que la función 'pagar' de la clase 'Cuenta' 
    # lanza una excepción cuando se intenta realizar un pago pero el saldo es insuficiente.
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
