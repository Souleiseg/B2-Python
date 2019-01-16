#!/usr/bin/python3.6
#EXERCICE : 1a-add
#DESCRIPTION : Saisie et somme de deux nombres avec vérification du type de l'input.
#NOM : SEGHIR
#PRENOM : Souleimane
#DATE : 23/10/2018


def add():
	number1 = input("Saisissez un premier nombre : ") #On saisit deux nombres stockés dans deux variables.
	number2 = input("Saisissez un second nombre : ")  
	
	try:
		num1 = int(number1)           #On vérifie que les nombres sont bien de type int
		num2 = int(number2)
		sum = num1+num2               #Puis on fait leur somme
		print("La somme de {} et {} vaut {}.".format(number1, number2, sum)) #Affichage propre avec un ".format".
	except ValueError:
		print("Erreur : Une ou plusieurs variables saisies ne sont pas des nombres.")  #Erreur retournée si la saisie ne comporte pas deux nombres.
add()   #Appel de la fonction.
