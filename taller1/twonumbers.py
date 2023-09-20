import time
name = input('¿Como te llamas? ')
print('Hola ',name,' hora de jugar')
print()
time.sleep(2)
print('Comieza a adivinar')
time.sleep(0.5)
palabra = 'mexico'
tupalabra = ''
vidas = 5

while vidas > 0 :
    fallas = 0
    for letra in palabra:
        if letra in tupalabra:
            print(letra, end ='')
        else:
            print('_',end='')
            fallas += 1
    if fallas == 0:
        print('GANASTE')
        break
    tuletra = input('\nIntroduce una letra => ')
    tupalabra += tuletra

    if tuletra not in palabra:
        print('letra incorrecta')
        vidas -= 1
        print(f'Te quedan {vidas} vidas')

    if vidas == 0:
        print('PERDISTE')
        break