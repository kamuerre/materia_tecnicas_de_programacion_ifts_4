#1.-Escenario
#Modifica la primera línea de código en el editor, usando las palabras claves reservadas sep y end, para que se obtenga la salida esperada. 
# Emplea dos funciones print() en el editor.

#No cambies nada en la segunda invocación del print().

#Salida Esperada
#Mi***primer***programa...Python

#El código a modificar es el siguiente:


print("Mi","primer","programa")
print("Python") 

print("=============°=================")
print("Mi","primer","programa", sep="***", end="...")
print("Python")
print("=============°=================")
#2.-

#Vamos a darle formato a la salida

#Escenario
#Te pido que juegues con el código que realiza algunos (quizás incluso destructivos) cambios. 
# Siéntete libre de modificar cualquier parte del código, pero hay una condición - aprende de tus 
# errores y saca tus propias conclusiones.

#Intenta:
#hacer que la flecha sea el doble de grande (pero mantener las proporciones)[v]
#duplica la flecha, colocando ambas flechas una al lado de la otra; [v]
# nota: una cadena se puede multiplicar usando el siguiente truco: "string" * 2 producirá "stringstring" (pronto contaremos más al respecto)[v]
#elimina cualquiera de las comillas y observe detenidamente la respuesta de Python; presta atención a dónde Python ve un error - ¿es este el lugar donde realmente existe el error?
# haz lo mismo con algunos de los paréntesis;[v]
#cambia cualquiera de las palabras print por otra cosa, que difiera solo en mayúsculas y minúsculas (por ejemplo, Print) - qué sucede ahora?
#reemplaza algunas de las comillas con apóstrofes; observa lo que sucede con cuidado.
#El código es el siguiente:
#print("Ejemplo:)
print("Ejemplo")
#Le quite las comillas que cierran el string en la linea 35 y python lo reconcio y me marco el error
#SyntaxError: unterminated string literal (detected at line 35)
print(" ")
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

#Podés escribir las respuestas como comentarios dentro del archivo .py
#minimizar el número de invocaciones de la función print() insertando \n en las cadenas;
print("aplicando salto de linea dentro del mismo print para minimizar la cantidad de print")
print("    *\n   * *\n  *   *\n *     * \n***   *** \n  *   * \n  *   *\n  *****\n" )
print("usando *2 para duplicar el string")
print("    *       \n   * *      \n  *   *     \n *     *     \n***   ***  \n  *   *     \n  *   *    \n  *****    \n"*2)
print("duplicar el tamaño de la fecha y duplicar la flecha con *2")
#Le tuve que agregar espacios antes de las comillas que cierran el string, porque sino se superponian las flechas.
print("      *       "*2)
print("    *   *     "*2)
print("   *     *    "*2)
print("  *       *   "*2)
print(" *         *  "*2)
print("***       *** "*2)
print("  *       *   "*2)
print("  *       *   "*2)
print("  *********   "*2)
print("agrandando la flecha:\n")
print("       *")
print("     *   *")
print("    *     *")
print("   *       *")
print("  *         *")
print(" *           *")
print("***         ***")
print("  *         *")
print("  *         *")
print("  *         *")
print("  *         *")
print("  ***********")
print("errores a propósito:")
#Print(" ")
# File "c:\Users\User0055\TecnicasdeProgramación\Nueva carpeta\flecha_Rasnosky.py", line 83, in <module>
    #Print(" ")
    #^^^^^
#NameError: name 'Print' is not defined. Did you mean: 'print'?
#print(´    *´)
# File "c:\Users\User0055\TecnicasdeProgramación\Nueva carpeta\flecha_Rasnosky.py", line 88
    #print(´    *´)
         #^
#SyntaxError: invalid character '´' (U+00B4)
print("   * *");#Coloque; al finalizar.
#PRINT("  *   *")
# File "c:\Users\User0055\TecnicasdeProgramación\Nueva carpeta\flecha_Rasnosky.py", line 94, in <module>
   #PRINT("  *   *")
    #^^^^^
#NameError: name 'PRINT' is not defined


print("eso fue to-to-to-todo amigos...")