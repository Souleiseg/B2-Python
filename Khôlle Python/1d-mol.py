#!/usr/bin/python3.6
#EXERCICE : 1d-mol
#DESCRIPTION : Jeu du plus ou moins.
#NOM : SEGHIR
#PRENOM : Souleimane
#DATE : 23/10/2018

import random
import signal
import sys
from time import sleep

def bye(): #Affiche la solution et un message d'au revoir.
  print("La solution était {}. \nAu revoir !".format(rand))  

def ctrl(signal, frame): #Fonction à exécuter lors d'un CTRL+C.
  print("   --> Programme fermé.")
  bye()
  sys.exit(0)

signal.signal(signal.SIGINT, ctrl) #Exécute la fonction "ctrl" lors d'un CTRL+C.

rand = random.randint(0,101) #Génère un nombre "rand" comprit entre 0 et 100.
print("\n          ### JEU DU PLUS OU MOINS ###\nRègle : Trouvez un nombre compris entre 0 et 100 inclus.\n****Vous pouvez QUITTER la partie à tout moment en pressant la touche Q.***") #Affichage des règles.
num = input("Saisissez un nombre (entre 0 et 100 INCLUS) : \n") #Saisie du premier nombre.


while 1 :   
  
  try:  #Permet de quitter en pressant la lettre Q.
    num = int(num) #Check si num est de type int.
  except ValueError:
    print("Vous avez quitté la partie.")
    bye() #Affiche la solution ainsi qu'un message d'au revoir.
    break #Sort de la boucle

  if num > rand: #Affiche "Plus petit !" si le nombre entré est trop grand. 
    print("Plus petit !")
    num = input("Saisissez un autre nombre : ") #Saisie d'un autre nombre.
 
  elif num < rand: #Affiche "Plus grand !" si le nombre entré est trop petit.
    print("Plus grand !")
    num = input("Saisissez un autre nombre : ") #Saisie d'un autre nombre.

  else: #Message de victoire si l'on trouve le bon nombre
    print("Vous avez gagné !") 
    bye() #Affiche la solution ainsi qu'un message d'au revoir.
    break #Sort de la boucle
