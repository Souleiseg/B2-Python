#!/usr/bin/python3.6

#Import des modules requis
from stats import money
import random

#Variables du jeu
rules = 'none'
playing = True
num = 51
color = 'none'

#Message de bienvenue 
print('\n           ### Bienvenue au jeu de la roulette. ###\n')


#On propose au joueur de lire les règles du jeu
while(rules != 'o' and rules != 'n'):
    rules = input('Souhaitez vous lire les règles ? [o/n] : ')

if(rules == 'o'):
    f = open("rules.txt", "r")
    text = f.read()
    print(text)
    f.close()

elif(rules == 'n'):
     rules = 'n'

print('Vous démarrez la partie avec ${}'.format(money))

#On boucle sur la partie en cours
while(playing is True):
    finish = 'none'
#Nombre aléatoire entre 1 et 50
    rand = random.randint(1,51)
    
    while(num < 1 or num > 50):
        num = int(input('\nSur quel numéro souhaitez vous miser ? [1 à 50] : '))
        bet = float(input('Somme que vous misez : $'))
    

#On vérifie si la somme pariée est supérieure à la somme possédée
    while(bet > money):
        print('Il vous reste ${} et vous vouliez parier ${}.'.format(money, bet))
        bet = float(input('Somme que vous misez : $'))
    print('Vous avez misé ${} sur le numéro {} !'.format(bet, num))
    print('\n           *** Le croupier fait tourner la roulette ***\nLa bille s\'est arrêtée sur le numéro {} !'.format(rand))
    
#On relève la couleur de la case dans laquelle la bille s'est arrêtée
    if(rand %2 == 0):
        color = 'noire'
    elif(rand %2 != 0):
        color = 'rouge'

#Cas où le joueur a misé sur le bon nombre
    if(num == rand):
        print('Jackpot ! Le croupier vous remet ${}.'.format(bet*3))
        money -= bet
        money += bet + bet*3

#Cas où le joueur a misé sur le mauvais nombre
    elif(num != rand):
        if(color is 'noire' and num %2 == 0):
            print('Le nombre sur lequel vous avez misé et la case sur laquelle la bille s\'arrêtée sont de couleur {}.\n\nLe croupier vous remet ${}.'.format(color, bet+bet/2))
            money -= bet
            money = money + (bet + bet/2)
            print('Vous possédez désormais ${}.\n'.format(money))
        
        elif(color is 'rouge' and num %2 !=0):
            print('Le nombre sur lequel vous avez misé et la case sur laquelle la bille s\'arrêtée sont de couleur {}.\n\nLe croupier vous remet ${}.'.format(color, bet+bet/2))
            money -= bet
            money = money + (bet + bet/2)
            print('Vous possédez désormais ${}.\n'.format(money))
        else:
            money -= bet
            print('Vous avez perdu ${}.\nVous possédez désormais ${}.\n'.format(bet, money))
    
    if(money == 0):
        print('           *** Vous êtes ruiné. Vous avez été jeté du casino... ***')
        break

    while(finish != 'o' and finish != 'n'):
        finish = input('Souhaitez vous parier à nouveau ? [o/n] : ')

    if(finish == 'o'):
        num = 51
    elif(finish == 'n'):
        print('Vous quittez le Casino avec ${} en poche.'.format(money))
        break
#On attribue une valeur hors de l'intervalle [0;49] afin de relancer la boucle 'while(playing)'
print('\nPartie terminée. Merci d\'avoir joué !')
