import time

def rc4(key, texto):
    # Inicializar el vector S
    S = list(range(256))
    j = 0
    
    # Inicialización del estado de la permutación
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    
    # Cifrado del texto
    i = 0
    j = 0
    resultado = []
    for char in texto:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        resultado.append(chr(ord(char) ^ K))
    
    return ''.join(resultado)

# 1. Leer el archivo txt con el texto del mensaje a cifrar
def leer_archivo():
    with open('C://Users//usuario//Downloads//TAREA04-U01-G02//TAREA04-U01-G02//txt//1000.txt', 'r', encoding='utf-8') as f:
        return f.read()

# 2. Generar la clave de cifrado (debe ser una clave de bytes)
def generar_clave():
    clave = "mi_clave_secreta"
    return [ord(c) for c in clave]  # Convertir la clave en una lista de valores ASCII

# 3. Función principal que hace todo
def main():
    # 1. Leer el archivo
    inicio = time.perf_counter()
    texto_original = leer_archivo()
    fin_lectura = time.perf_counter()
    print(f"Tiempo de lectura del archivo: {fin_lectura - inicio:.6f} segundos")

    # 2. Generar e imprimir la clave de cifrado
    clave = generar_clave()
    print(f"Clave de cifrado/descifrado: {''.join(chr(c) for c in clave)}")
    fin_clave = time.perf_counter()
    print(f"Tiempo para generar la clave: {fin_clave - fin_lectura:.9f} segundos")

    # 3. Cifrar el texto
    inicio_cifrado = time.perf_counter()
    texto_cifrado = rc4(clave, texto_original)
    fin_cifrado = time.perf_counter()
    print(f"Texto cifrado: {texto_cifrado}")
    tiempo_cifrado = fin_cifrado - inicio_cifrado
    print(f"Tiempo para cifrar: {tiempo_cifrado:.9f} segundos")

    # 4. Descifrar el texto
    inicio_descifrado = time.perf_counter()
    texto_descifrado = rc4(clave, texto_cifrado)
    fin_descifrado = time.perf_counter()
    print(f"Texto descifrado: {texto_descifrado}")
    tiempo_descifrado = fin_descifrado - inicio_descifrado
    print(f"Tiempo para descifrar: {tiempo_descifrado:.9f} segundos")
    
    #Datos tabla
    print(f"Tiempo para cifrar: {tiempo_cifrado:.9f} segundos")
    print(f"Tiempo para descifrar: {tiempo_descifrado:.9f} segundos")

    #Caracteres entrada-salida
    print(f"Número de caracteres de entrada: {len(texto_descifrado)}")
    print(f"Número de caracteres de salida: {len(texto_cifrado)}")

# Ejecutar el programa
if __name__ == '__main__':
    main()
