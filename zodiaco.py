### Tu Signo del Zodiaco ###

# creamos una función dónde se indican las fechas de los signos del zodiaco y cuáles son
def signos_zodiaco(día, mes):
    fechas = [(21, 3), (20, 4), (21, 5), (21, 6), (23, 7), (23, 8), (23, 9), (23, 10),
              (22, 11), (22, 12), (21, 1), (20, 2)]
    signos = ['aries', 'tauro', 'géminis', 'cáncer', 'leo', 'virgo', 'libra', 'escorpio',
              'sagitario', 'capricornio', 'acuario', 'piscis']
    
día = int(input("Ingresa el día en que naciste: "))
mes = int(input("Ingresa el mes: "))

signo = signos_zodiaco(día, mes)
print(f"Tu signo del zodiaco es: ")
