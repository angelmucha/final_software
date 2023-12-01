from fastapi import FastAPI, HTTPException
from typing import List
from datetime import datetime

app = FastAPI()

class Cuenta:
    def __init__(self, numero, nombre, saldo=0, contactos=None):
        self.numero = numero
        self.nombre = nombre
        self.saldo = saldo
        self.contactos = contactos or {}
        self.operaciones = []

    def historial(self):
        return {"saldo": self.saldo, "operaciones": self.operaciones}

    def pagar(self, destino, valor):
        if destino not in self.contactos:
            raise HTTPException(status_code=400, detail="El destino no es un contacto válido.")
        if self.saldo < valor:
            raise HTTPException(status_code=400, detail="Saldo insuficiente para realizar la operación.")

        self.saldo -= valor
        operacion = Operacion(numero_destino=destino, valor=valor)
        self.operaciones.append(operacion)

        # Añadir el monto a la cuenta destino
        cuenta_destino = BD.get(destino)
        #print(cuenta_destino.saldo)
        cuenta_destino.depositar(valor)
        return operacion
    
    def depositar(self, valor):
        self.saldo += valor
        operacion = Operacion(numero_destino=self.numero, valor=valor)
        self.operaciones.append(operacion)

class Operacion:
    def __init__(self, numero_destino, valor):
        self.numero_destino = numero_destino
        # Utiliza una librería para obtener la fecha actual
        self.fecha = datetime.now()
        self.valor = valor

# Inicializar la aplicación con un conjunto de cuentas y contactos
BD = {
    "21345": Cuenta(numero="21345", nombre="Arnaldo", saldo=200, contactos=["123", "456"]),
    "123": Cuenta(numero="123", nombre="Luisa", saldo=400, contactos=["456"]),
    "456": Cuenta(numero="456", nombre="Andrea", saldo=300, contactos=["21345"]),
}

@app.get("/billetera/contactos")
def obtener_contactos(minumero: str):
    cuenta = BD.get(minumero)
    if cuenta:
        return {contacto: BD[contacto].nombre for contacto in cuenta.contactos}
    raise HTTPException(status_code=404, detail="Cuenta no encontrada.")

@app.get("/billetera/contactos")
def obtener_contactos(minumero: str):
    cuenta = BD.get(minumero)
    if cuenta:
        contactos_info = {contacto: {"nombre": BD[contacto].nombre, "numero": contacto} for contacto in cuenta.contactos}
        return contactos_info
    raise HTTPException(status_code=404, detail="Cuenta no encontrada.")



@app.post("/billetera/pagar")
def realizar_pago(minumero: str, numerodestino: str, valor: float):
    cuenta = BD.get(minumero)
    destino = BD.get(numerodestino)
    
    if cuenta and destino:
        operacion = cuenta.pagar(numerodestino, valor)
        # Añadir la operación al historial del destinatario
        destino.operaciones.append(Operacion(numero_destino=minumero, valor=valor))
        return {"mensaje": f"Operación realizada en {operacion.fecha}."}
    
    raise HTTPException(status_code=404, detail="Cuenta no encontrada.")

@app.get("/billetera/historial")
def obtener_historial(minumero: str):
    cuenta = BD.get(minumero)
    if cuenta:
        historial = cuenta.historial()
        historial["operaciones"] = [{"tipo": "Pago realizado", "valor": op.valor, "destino": op.numero_destino} for op in cuenta.operaciones]
        return historial
    
    raise HTTPException(status_code=404, detail="Cuenta no encontrada.")
