# final_software

Pregunta 3:

Se requiere realizar un cambio en el software para que soporte un valor máximo de 200 soles a transferir por día.
Qué cambiaría en el código (Clases / Métodos) - No implementación.
Nuevos casos de prueba a adicionar.
Cuánto riesgo hay de “romper” lo que ya funciona?
# Respuesta

Se agregaria un atributo limite que tenga un valor de 200 que se actualice despues de las 12 de la noche, luego en el metodo pagar le agrego una resta a ese atributo limite y que valide que su limite sea mayor que 0 sino que imprima un mensaje que el monto pasa el limite de transferencias por dias y que imprima cuanto es lo que le queda por el dia de hoy.

- Agregaria un test validando cuando quieran depositar mas del limite.
- Un test validando si esta bien el limite de una cuenta despues de usar el metodo pagar.
- Test para actualizar límite diario después de medianoche

Hay un poco de riesgo en romper lo que ya funciona ya que estariamos modificando la clase Cuenta y el método pagar. Pero no es altamente riesgoso ya que solo estamos trabajando sobre un nuevo atributo y que se actualice. Lo unico "riesgoso" seria la actualizacion al momento de cumplirse el dia. Ya que debe acceder a todas las cuentas y cambiar su limite por 200. Pero no deberia haber mucho problema.
