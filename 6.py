#Algoritmo que realice el cifrado de una cadena de caracteres utilizando la siguiente tabla de cifrado:
#La cadena de caracteres se ingresa al iniciar el programa. Si algún caracter del texto no existe en la matriz, coloque "**".
# Imprima la matriz de cifrado, el mensaje original y el mensaje cifrado.

matriz = [['*', 'A', 'S', 'D', 'F', 'G'],
          ['Q', 'a', 'b', 'c', 'd', 'e'],
          ['W', 'f', 'g', 'h', 'i', 'j'],
          ['E', 'k', 'l', 'm', 'n', 'o'],
          ['R', 'p', 'q', 'r', 's', 't'],
          ['T', 'u', 'v', 'x', 'y', 'z']]

def print_matriz(matriz):
    for fila in matriz:
        print(' '.join(fila))
    print()

def obtener_coordenadas(caracter, matriz):
    # Devuelve las coordenadas de un carácter en la matriz o None si no existe
    for i, fila in enumerate(matriz):
        if caracter in fila:
            return (i, fila.index(caracter))
    return None

def cifrar_cadena(cadena, matriz):
    #Cifra una cadena de caracteres utilizando la matriz de cifrado
    resultado = ""
    for char in cadena:
        if char.isalpha():
            coordenadas = obtener_coordenadas(char, matriz)
            if coordenadas:
                i, j = coordenadas
                resultado += matriz[i][0] + matriz[0][j]  # Agregar la fila y columna
            else:
                resultado += '**'
        else:
            resultado += ' '  # Mantener los espacios en blanco
    return resultado

# Entrada del usuario
cadena = input("Ingresa la cadena para cifrar: ").lower()

# Imprimir resultados
print("Matriz de Cifrado:")
print_matriz(matriz)
print("El mensaje es:", cadena)
print("El mensaje cifrado es:", cifrar_cadena(cadena, matriz))
