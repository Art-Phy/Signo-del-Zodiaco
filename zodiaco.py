### Tu Signo del Zodiaco ###

# creamos una función dónde se indican las fechas de inicio de los signos del zodiaco.
def signos_zodiaco(día, mes):
    fecha_inicio = [21, 20, 21, 21, 22, 21, 23, 23, 23, 23, 22, 22]
    signos = ['aries', 'tauro', 'géminis', 'cáncer', 'leo', 'virgo', 'libra', 'escorpio',
              'sagitario', 'capricornio', 'acuario', 'piscis']
    # determinamos el signo
    if día < fecha_inicio[mes - 1]: # si el día es menor al inicio de ese signo
        signo = signos[mes -2] # signo del mes anterior
    else:
        signo = signos[mes -1] # signo del mes actual

    return (signo)

# entrada del usuario
día = int(input("Ingresa el día en que naciste: "))
mes = int(input("Ingresa el mes: "))

# mostrar el resultado
print(f"Tu signo del zodiaco es: ", signos_zodiaco(día, mes))