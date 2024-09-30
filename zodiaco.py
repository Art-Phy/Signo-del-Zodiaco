### Tu Signo del Zodiaco ###

# importamos datetime de Python para tener un control de los días de cada mes.
from datetime import datetime

def fecha_valida(día, mes):
    try:
        datetime(2024, mes, día) # importante para los años bisiestos
        return True
    except ValueError:
        return False
    
# creamos una función dónde se indican las fechas de inicio de los signos del zodiaco.
def signos_zodiaco(día, mes):
    # definimos los rangos de inicio y fin de cada signo del zodiaco usando tuplas.
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
        
def solicitar_fecha():
    while True:
        try:
            # entrada del usuario
            día = int(input("Ingresa el día en que naciste: "))
            mes = int(input("Ingresa el mes: "))

            # verificar la fecha
            if fecha_valida(día, mes):
                return día, mes
            else:
                print("La fecha ingresada no es válida. Inténtalo de nuevo.")
        except ValueError:
            print("Ingresa sólo valores numéricos, gracias.")

# principal
while True:
    día, mes = solicitar_fecha()

    # mostrar el signo zodiacal
    print("Tu signo del zodiaco es:", signos_zodiaco(día, mes).title())

# añadimos pregunta para que el usuario decida si quiere seguir o no
    repetir = input("¿Quieres probar con otra fecha? (s/n): ").lower()
    if repetir != 's':
        print("Entendido. ¡Nos vemos!")
        break
