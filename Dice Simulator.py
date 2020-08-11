import random
print("Dice Stimulator")

ch='y'

while ch=='y':
    number=random.randint(1,6)

    if number==1:
        print('___________')
        print('|         |')
        print('|         |')
        print('|    O    |')
        print('|         |')
        print('|_________|')

    elif number==2:
        print('___________')
        print('|         |')
        print('|         |')
        print('|  O   O  |')
        print('|         |')
        print('|_________|')

    elif number==3:
        print('___________')
        print('|         |')
        print('| O       |')
        print('|    O    |')
        print('|      O  |')
        print('|_________|')
    
    elif number==4:
        print('___________')
        print('|         |')
        print('|  O   O  |')
        print('|         |')
        print('|  O   O  |')
        print('|_________|')

    elif number==5:
        print('___________')
        print('|         |')
        print('|  O   O  |')
        print('|    O    |')
        print('|  O   O  |')
        print('|_________|')

    else:
        print('___________')
        print('|         |')
        print('|  O   O  |')
        print('|  O   O  |')
        print('|  O   O  |')
        print('|_________|')
    
    print('Do you want to roll again? (y/n)')
    ch=input('')


