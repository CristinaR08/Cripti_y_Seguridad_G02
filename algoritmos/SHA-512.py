import hashlib
import time

# Función para leer el archivo de texto
def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        return archivo.read()

# Función para generar el hash SHA-512
def generar_clave_sha512(texto):
    sha512_hash = hashlib.sha512()
    sha512_hash.update(texto.encode('utf-8'))
    return sha512_hash.hexdigest()

# Función para cifrar el texto (en realidad solo generamos el hash)
def cifrar(texto):
    return generar_clave_sha512(texto)

# Función principal
def main():
    archivo = 'C://Users//usuario//Downloads//TAREA04-U01-G02//TAREA04-U01-G02//txt//1000.txt'
    texto = leer_archivo(archivo)

    # Mostrar el texto a cifrar
    print("Texto a Cifrar:")
    print(texto)

    # Fase 1: Cifrar el texto (obtenemos el hash)
    start_time = time.perf_counter()
    texto_cifrado = cifrar(texto)
    print("\nTexto Cifrado (SHA-512):")
    print(texto_cifrado)
    print(f"Tiempo para cifrar el texto: {time.perf_counter() - start_time:.9f} segundos")
    
    #Num caracteres
    print(len(texto_cifrado))
    

if __name__ == '__main__':
    main()
