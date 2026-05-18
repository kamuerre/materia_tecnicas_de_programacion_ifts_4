#le asigno valor a la variable kilometers
kilometers = 12.25
#le asigno valor a la variable miles (millas)
miles = 7.38
#multiplico la cantidad de millas por 1.61
miles_to_kilometers = miles * 1.61
#divido la cantidad de kilometros por 1.61
kilometers_to_miles = kilometers/1.61
#muestro la primer salida cantidad de kilometros que son 7.38 millas
print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
#muestro la segunda salida cantidad de millas que son 12.25 kilometros
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")


""" Salida Esperada
7.38 millas son 11.88 kilómetros
12.25 kilómetros son 7.61 millas
 """