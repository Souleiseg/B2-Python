#!/usr/bin/python3.6
#EXERCICE : 2a-mol.py
#DESCRIPTION : Jeu "Plus ou Moins" qui lit dans un fichier externe.
#NOM : SEGHIR
#PRENOM : Souleimane
#DATE : 05/11/2018

import sys
import signal
from time import sleep
import random

c = 0                         #Compteur d'essais.
rand = random.randint(0,101)  #Génère un nombre aléatoire compris entre 0 et 100 inclus.

#Ecriture d'un message de bienvenue et des règles dans un fichier externe.
file = open('num.txt', 'w').write("\n### Jeu du plus ou moins ###\n\nRègles :\n- Saisir un nombre compris entre 0 et 100 (inclus\n- Le nombre doit être saisit dans la première ligne.\n- Un message vous indiquera le nombre joué, et si le nombre à trouver est plus ou moins grand.\n\n### Bonne chance ! ###")


#Affiche la solution ainsi qu'un message d'au revoir.
def over():
    print("Le nombre à trouver était {}. Au revoir !".format(rand))
    sys.exit(0)


# Messages affichés dans la console qui fait tourner le jeu.
print("### Jeux du plus ou moins ###")
print("La valeur est comprise en 0 et 100 \n ")
print("Pour jouer, ouvrez le fichier \"num.txt\".")


while 1:                                         # Boucle qui fait tourner le jeu en permanence (en arrière plan).
    
    prompt = open('num.txt', 'rt').readline(3)   # Correspond au nombre saisit par le joueur dans le fichier "num.txt".

    exit = open('num.txt', 'rt').readline(1) 
    if exit == "q":                              # Si la lettre "q" est saisie en première ligne    
        over()                                   # Alors on exécute la fonction "over()".

    try:
        num = int(prompt)                        # Le type de la saisie du joueur est convertie (str --> int)
     
        if num < rand:                           # Détecte si le nombre saisit est trop petit.
            file = open('num.txt', 'w').write("\nPlus grand !\nNombre joué précedemment : {}".format(num))      # Affiche un message contextuel avec le nombre saisit précedemment.
            c += 1                               # Incrémente le compteur (+1)
     
        elif num > rand:                         # Détecte si le nombre saisit est trop grand.
            file = open('num.txt', 'w').write("\nPlus petit !\nNombre joué précedemment : {}".format(num))
            c += 1
        
        elif num == rand:                        # Détecte si le nombre saisit est égal au nombre aléatoire.
            c += 1
            print("\nC'est gagné ! Le nombre à trouver était {}. Vous avez réussi en {} coups.".format(rand, c)) # Affiche la solution, un message de victoire ainsi que le nombre d'essais dans la console.
            sys.exit(0)

    except ValueError:                           # Si la saisie ne correspond pas à un nombre, elle est ignorée.
            sleep(1)
