#Algoritmo que realice el cifrado de una cadena de caracteres mediante un método de sustitución Polialfabético de Vigenère.
#La cadena se ingresa al iniciar el algoritmo. El algoritmo debe mostrar la cadena de caracteres ingresada, la clave de cifrado y la cadena de caracteres cifrada.
#Entrada del usuario para el mensaje y la clave de cifrado
mensaje = input("Escribe el mensaje a encriptar: ")
llave = input("Escribe la clave de encriptación: ")

#Variable para almacenar el texto encriptado
mensaje_cifrado = ""

#Índice para recorrer la clave de encriptación
indice_clave = 0

#Recorre cada caracter en el mensaje
for pos in range(len(mensaje)):
    if mensaje[pos].isalpha():  # Verifica si es una letra
        # Realiza el cifrado de Vigenère
        letra_cifrada = chr((ord(mensaje[pos]) + ord(llave[indice_clave].lower()) - 2 * ord('a')) % 26 + ord('a'))
        mensaje_cifrado += letra_cifrada
        # Actualiza el índice de la clave
        indice_clave = (indice_clave + 1) % len(llave)
    else:
        # Agrega el carácter sin cambiarlo si no es letra
        mensaje_cifrado += mensaje[pos]

# Muestra los resultados
print("Mensaje original:", mensaje)
print("Clave utilizada:", llave)
print("Mensaje encriptado:", mensaje_cifrado)