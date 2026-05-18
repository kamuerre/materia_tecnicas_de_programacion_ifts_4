""" Entrada de muestra: 1

Salida esperada: y = 0.6000000000000001

------------------------------------

Entrada de muestra: 10

Salida esperada: y = 0.09901951266867294

-------------------------------------------
Entrada de muestra: 100

Salida esperada: y = 0.009999000199950014

---------------------------------------------
Entrada de muestra: -5

Salida Esperada: y = -0.19258202567760344

--------------------------------------

Código:

x = float(input("Ingresa el valor para x: "))

# Escribe tu código aquí.

print("y =", y) """


x = float(input("Ingresa el valor para x: "))
y=1/(x+1/(x+1/(x+1/x)))
# Escribe tu código aquí.
print("y =", y) 

