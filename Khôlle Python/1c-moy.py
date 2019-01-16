#!/usr/bin/python3.6
#EXERCICE : 1b-dic
#DESCRIPTION : Demander une saisie utilisateur de plusieurs notes et prénoms
#NOM : SEGHIR
#PRENOM : Souleimane
#DATE : 23/10/2018
 
table = []     #Tableau vide qui va stocker les prénoms et les notes.
i = 0          #indice qui correspond à une case du tableau.
moy = 0        #Moyenne de toutes les notes.

while 1 :      #Boucle infinie.

	prenom = input("Saisissez un prénom : ")
	note = input("Saisissez une note : ")


	try:   #Retourne une erreur si la note entrée n'est pas de type int.

		num = int(note)
	except ValueError:
		print("Erreur : La note saisie doit être un nombre.")
		break


	table.insert(i, prenom + " > " + note + "/20")   #insère la note et le nom dans le tableau.
	moy += int(note)                                 #Somme de la moyenne actuelle avec la note saisie.
	i += 1                                           #On incrémente i pour passer à la case suivante.

	print("Continuer ou quitter la saisie ?[c/q]")
	keypress = input()                                              #On crée une variable que l'on associe à un input.

	if keypress == "q":                                             #Si cette variable correspond à "q", on quitte. 
		print("Saisie quittée.")
		print(table)                                            #Affichage du tableau (nom et notes).
		moy = moy/i				                #On divise la somme des notes par le nombre de notes.
		print("La moyenne totale est de {}/20.".format(moy)) 
		break                                                   #Sortie de la boucle.
