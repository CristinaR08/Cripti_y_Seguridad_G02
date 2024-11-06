import itertools

def permutaciones_palabra(palabra):
    # Generar todas las permutaciones
    permutaciones = sorted(set(itertools.permutations(palabra)))
    
    # Convertir cada permutación en una cadena de caracteres
    permutaciones = [''.join(p) for p in permutaciones]
    
    # Mostrar el número total de permutaciones
    total_permutaciones = len(permutaciones)
    print(f"Total de permutaciones: {total_permutaciones}")
    
    # Mostrar las primeras 10 permutaciones ordenadas alfabéticamente
    print("Primeras 10 permutaciones:")
    for perm in permutaciones[:10]:
        print(perm)

# Solicitar la palabra al usuario
palabra = input("Ingrese una palabra: ")
permutaciones_palabra(palabra)