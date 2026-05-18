""" Escenario
Observa el código en el editor: lee un valor float, lo coloca en una variable llamada x, 
e imprime el valor de la variable llamada y. Tu tarea es completar el código para evaluar 
la siguiente expresión:

3x**3 - 2x**2 + 3x - 1

El resultado debe ser asignado a y.

Recuerda que la notación algebraica clásica muy seguido omite el operador de multiplicación, aquí se debe de 
incluir de manera explicita. Nota como se cambia el tipo de dato para asegurarnos de que x es del tipo float.

Mantén tu código limpio y legible, y pruébalo utilizando los datos que han sido proporcionados.
 No te desanimes por no lograrlo en el primer intento. Se persistente y curioso.

Copia el código y completa en el editor:


x =  # Codifica tus datos de prueba aquí.

x = float(x)

# Escribe tu código aquí.

print("y =", y)



Ayuda:


Salida de muestra
y = -1.0
y = 3.0
y = -9.0
Valores que debe tomar X:

x = 0
x = 1
x = -1
"""
print("=================================")
#en esta impresión el valor de x es 0.
x=0
print("El valor de \"x\" es: ", x )
y=float(3*x**3 - 2*x**2 + 3*x - 1)
print("El valor de \"y\" es: ", y )
print("=================================")
#en esta impresión el valor de x es 1.
print("El valor de \"x\" es: ", x )
x=1
y=float(3*x**3 - 2*x**2 + 3*x - 1)
print("El valor de \"y\" es: ", y )
print("=================================")
#en esta impresión el valor de x es -1.
x=-1
print("El valor de \"x\" es: ", x )
y=float(3*x**3 - 2*x**2 + 3*x - 1)
print("El valor de \"y\" es: ", y )
