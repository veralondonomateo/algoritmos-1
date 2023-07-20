import random
def adivinar():

    print('Bienvenido a las adivinanzas')
    print('Debes adivinar un numero entre 1 y 100')
    num_adivinar = random.choice(range(1,101))
    while True:
        #Ciclo infinito hasta la adivinación del número a encontrar
        eleccion = int(input('elige un numero => '))
       
        if eleccion > 100 : 
            print('Recuerda que el número a adivinar esta entre 1 y 100')
        elif eleccion == num_adivinar:
            print('¡FELICIDADES! Adivinaste')
            break
        elif eleccion < num_adivinar:
            print('Es un número mayor')
        elif eleccion > num_adivinar:
            print('Es un numero menor') 
        
adivinar()
while True:
    #Ciclo infinito para la toma de decisiones
    decision = input('Deseas probaro otra vez? ')
    decision = decision.lower
    if decision == 'si':
        break
#Nuevo llamado a la función 

    else:
        adivinar()