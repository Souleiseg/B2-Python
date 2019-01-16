#!/usr/bin/python3.6

#Import du module random
import random

#On déclare un tableau dans lequel le robot va choisir son signe.
signe = [0, 1, 2]

#Signe choisit.
playerScore = 0
oponentScore = 0
minRounds =1
rounds = int(input('\nSaisissez le nombre de manche à jouer : '))

while minRounds <= rounds:
    chosen = random.choice (signe)
    player = int(input('\nSaisisez un nombre :\n[0] Pierre\n[1] Papier\n[2] Ciseaux\nNombre choisit : '))
    while player < 0 or player > 2:
        print('Saisissez un des 3 nombres...')
        player = int(input('\nSaisisez un nombre :\n[0] Pierre\n[1] Papier\n[2] Ciseaux\nNombre choisit : '))
    
    print('Début de la manche n°{}'.format(minRounds))
    if chosen == 0:
        chosen = 'Pierre'
        if player == 0 :
            player = 'Pierre'
            print('\n> Vous jouez {}.\n> L\'adversaire joue {}.\n### Egalité ###'.format(player, chosen))
        elif player == 1:
            player = 'Papier'
            print('\n> Vous jouez {}.\n> L\'adversaire joue {}.\n### Manche gagnée ###'.format(player, chosen))
            playerScore +=1
        elif player == 2:
            player = 'Ciseaux'
            print('\n> Vous jouez {}.\n> L\'adversaire joue {}.\n### Manche perdue ###'.format(player, chosen))
            oponentScore += 1
        
    elif chosen == 1:
        chosen = 'Papier'
        if player == 0:
            player = 'Pierre'
            print('\n> Vous jouez {}.\n> L\'adversaire joue {}.\n### Manche perdue ###'.format(player, chosen))
            oponentScore += 1
        elif player == 1:
            player = 'Papier'
            print('\n> Vous jouez {}.\n> L\'adversaire joue {}.\n### Egalité ###'.format(player, chosen))
        elif player == 2:
            player = 'Ciseaux'
            print('\n> Vous jouez {}.\n> L\'adversaire joue {}.\n### Manche gagnée ###'.format(player, chosen))
            playerScore +=1

    elif chosen == 2:
        chosen = 'Ciseaux'
        if player == 0:
            player = 'Pierre'
            print('\n> Vous jouez {}.\n> L\'adversaire joue {}.\n### Manche gagnée ###'.format(player, chosen))
            playerScore += 1
        elif player == 1:
            player = 'Papier'
            print('\n> Vous jouez {}.\n> L\'adversaire joue {}.\n### Manche perdue ###'.format(player, chosen))
            oponentScore += 1
        elif player == 2:
            player = 'Ciseaux'
            print('\n> Vous jouez {}.\n> L\'adversaire joue {}.\n### Egalité ###'.format(player, chosen))
    print('Fin de la manche n°{}'.format(minRounds))
    minRounds += 1

if playerScore > oponentScore:
    print('Fin de la partie.\nScore final : {} - {}\n### Vous remportez la partie ###'.format(playerScore, oponentScore))
elif playerScore < oponentScore:
    print('Fin de la partie.\nScore final : {} - {}\n### Vous perdez la partie ###'.format(oponentScore, playerScore))
