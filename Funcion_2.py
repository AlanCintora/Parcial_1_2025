#Función porcentaje_aprobados(): Calcula el porcentaje de
#exámenes aprobados (nota ≥ 6) por cada alumno y muestra un resumen
#individual. Usar contadores y acumuladores.

def porcentaje_aprobados(matriz):
    alumno = 0

    
    """
    Calcula y muestra el porcentaje de exámenes aprobados (nota >= 6) por cada alumno.
    """

    while alumno < len(matriz):
        fila = matriz[alumno]
        aprobados = 0
        examenes = 0
        i = 0
        while i < len(fila):
            if fila[i] >= 6:
                aprobados += 1
            examenes += 1
            i += 1
        porcentaje = (aprobados * 100) / examenes
        print(f"Alumno {alumno + 1}: {porcentaje}% de exámenes aprobados.")
        alumno += 1

