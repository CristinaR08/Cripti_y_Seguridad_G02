import random
import time
import json

# Función para leer el archivo de texto
def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        return archivo.read()

# Función para generar las claves (pública y privada)
def generar_claves_mqq():
    clave_privada = [random.randint(1, 100) for _ in range(10)]
    clave_publica = [x * 3 + 7 for x in clave_privada]  # Relación pública basada en la privada
    return clave_privada, clave_publica

# Función para cifrar el texto
def cifrar_mqq(texto, clave_publica):
    texto_cifrado = [ord(c) + sum(clave_publica) % 256 for c in texto]
    return texto_cifrado

# Función para descifrar el texto
def descifrar_mqq(texto_cifrado, clave_privada):
    texto_descifrado = ''.join(
        chr((c - sum([x * 3 + 7 for x in clave_privada]) % 256) % 256) for c in texto_cifrado
    )
    return texto_descifrado

# Función principal
def main():
    archivo = 'C://Users//usuario//Downloads//TAREA04-U01-G02//TAREA04-U01-G02//txt//10000000.txt'
    texto = leer_archivo(archivo)

    # Mostrar el texto a cifrar
    print("Texto a Cifrar:")
    print(texto)

    # Fase 1: Generar las claves
    clave_privada, clave_publica = generar_claves_mqq()
    
    # Fase 2: Cifrar el texto
    start_time = time.perf_counter()
    texto_cifrado = cifrar_mqq(texto, clave_publica)
    print("\nTexto Cifrado (Simulación MQQ):")
    print(texto_cifrado)
    #print(f"Tiempo para cifrar el texto: {time.perf_counter() - start_time:.9f} segundos")
    tcifrado= f"Tiempo para cifrar el texto: {time.perf_counter() - start_time:.9f} segundos"

    # Guardar texto cifrado en un archivo
    with open("texto_cifrado.json", "w", encoding="utf-8") as archivo_cifrado:
        json.dump(texto_cifrado, archivo_cifrado)

    # Fase 3: Descifrar el texto
    

    start_time = time.perf_counter()
    texto_descifrado = descifrar_mqq(texto_cifrado, clave_privada)
    print("\nTexto Descifrado:")
    print(texto_descifrado)
    print("\nClave Privada:")
    print(clave_privada)
    print("\nClave Pública:")
    print(clave_publica)
    print(tcifrado)
    print(f"Tiempo para descifrar el texto: {time.perf_counter() - start_time:.9f} segundos")

    # Verificar si el texto descifrado coincide con el original
    if texto == texto_descifrado:
        print("\nEl texto descifrado coincide con el texto original.")
    else:
        print("\nError: El texto descifrado no coincide con el texto original.")
    #Num caracteres
    print(len(texto_cifrado))
if __name__ == '__main__':
    main()
