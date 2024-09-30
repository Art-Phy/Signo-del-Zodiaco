### Tu Signo del Zodiaco ###

# creamos una función dónde se indican las fechas de inicio de los signos del zodiaco.
def signos_zodiaco(día, mes):
    # definimos los rangos de inicio y fin de cada signo del zodiaco
    signos_fechas = [((21, 3), (20, 4), 'aries'),
                     ((21, 4), (20, 5), ' tauro'),
                     ((21, 5), (20, 6), 'géminis'),
                     ((21, 6), (22, 7), 'cáncer'),
                     ((23, 7), (22, 8), 'leo'),
                     ((23, 8), (22, 9), 'virgo'),
                     ((23, 9), (22, 10), 'libra'),
                     ((23, 10), (22, 11), 'escorpio'),
                     ((23, 11), (21, 12), 'sagitario'),
                     ((22, 12), (20, 1), 'capricornio'),
                     ((21, 1), (19, 2), 'acuario'),
                     ((20, 2), (20, 3), 'piscis')
                     ]
    # ver los rangos para determinar el signo
    for(inicio, fin, signo) in signos_fechas:
        inicio_dia, inicio_mes = inicio
        fin_dia, fin_mes = fin

        # verificamos si el día y mes ingresados está dentro de los rangos de los signos
        if(mes == inicio_mes and día >= inicio_dia) or (mes == fin_mes and día <= fin_dia):
            return signo
        
    return "Algún dato es incorrecto, por favor empieza de nuevo" # por si algo se escribe mal

# entrada del usuario
día = int(input("Ingresa el día en que naciste: "))
mes = int(input("Ingresa el mes: "))

# mostrar el resultado
print(f"Tu signo del zodiaco es: ", signos_zodiaco(día, mes))