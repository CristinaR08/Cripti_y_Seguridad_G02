#Algoritmo que realice el cifrado de una cadena de caracteres mediante un método de sustitución 
# Monoalfabético de desplazamiento n caracteres a la derecha. Tanto la palabra como el valor de n se ingresan 
# al iniciar el algoritmo. El algoritmo debe mostrar el alfabeto original, el alfabeto cifrado, la cadena de caracteres ingresada y su resultado. 

from string import ascii_uppercase
import re

# Definición del alfabeto español con la Ñ
alfabeto_base = ascii_uppercase[:14] + 'Ñ' + ascii_uppercase[14:]

# Solicitud de palabra y limpieza de caracteres especiales
texto_usuario = re.sub(r'[^a-zA-Z\s]', '', input("Introduce un texto a cifrar: "))

# Solicitud de valor de desplazamiento (shift)
try:
    desplazamiento = int(input("Introduce el valor del desplazamiento (n): "))
except ValueError:
    print('Error: Introduce un valor numérico válido')
    desplazamiento = 0

# Generación del alfabeto desplazado
alfabeto_desplazado = alfabeto_base[desplazamiento:] + alfabeto_base[:desplazamiento]

# Cifrado del texto ingresado
texto_cifrado = ''
for letra in texto_usuario:
    posicion_original = alfabeto_base.lower().find(letra.lower())
    # Verifica si el caracter está en el alfabeto
    if posicion_original != -1:
      texto_cifrado += alfabeto_desplazado[posicion_original]
    # Agrega el caracter tal cual si no es letra
    else:
      texto_cifrado += letra



# Resultados
print("\nAlfabeto original:")
print(" ".join(alfabeto_base))
print("\nAlfabeto cifrado:")
print(" ".join(alfabeto_desplazado))
print("\nTexto ingresado:", texto_usuario)
print("Texto cifrado:", texto_cifrado)