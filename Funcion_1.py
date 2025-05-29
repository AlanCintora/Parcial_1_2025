#Función cargar_matriz_notas(): Recibe dos enteros n y m y permite
#cargar n x m notas válidas entre 1 y 10 inclusive. La validación debe
#hacerse dentro de esta función.

def cargar_matriz_notas(n, m):
    """
    Carga una matriz de notas de tamaño n x m, donde cada fila representa a un alumno
    y cada columna un examen.
    """

    matriz = []
    i = 0
    while i < n:
        fila = []
        j = 0
        while j < m:
            entrada = input(f"Ingrese nota [{i}][{j}] (1-10): ")
            if entrada.isdigit():
                nota = int(entrada)
                if 1 <= nota <= 10:
                    fila.append(nota)
                    j += 1
                else:
                    print("La nota debe estar entre 1 y 10.")
            else:
                print("Entrada inválida. Debe ingresar un número entero.")
        matriz.append(fila)
        i += 1

    """
    Retorna list: matriz de enteros con las notas válidas (entre 1 y 10 inclusive)
    """    
    return matriz


