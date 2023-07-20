import secrets

if __name__ == '__main__':
    names = ['Devin', 'Simon' ,'Julian','Saul', 'Andres', 'Felipe','Manuela', 'Julieta','Tomas','Ricardo','Miguel' ]
    names_final = 7

    fivenames = secrets.SystemRandom().sample(names, names_final)
    for i in fivenames:
        print('Hola', i)
