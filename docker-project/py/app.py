from random import randint

min_number = int(input('Número Menor: '))
max_number = int(input('Número Maior: '))

if(min_number > max_number): 
    print('Informações invalidas')
else:
    rnd_number = randint(min_number, max_number)
    print(rnd_number)