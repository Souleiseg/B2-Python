#!/usr/bin/python3.6
#EXERCICE : 1b-dic
#DESCRIPTION : Trier et stocker les noms saisis par l'utilisateur par ordre alphabétique dans une collection.
#NOM : SEGHIR
#PRENOM : Souleimane
#DATE : 23/10/2018

def addDic():              #Fonction appelée par le script.
        name_dic={}        #On crée un liste vide.
        i=0                #Indice de la position dans le tableau (0 correspond à la position 1).
        while 1:           #Boucle infine pour répéter l'opération.
            print("Entrez le nom à ajouter ou \"q\" pour quitter.")
            saisie=input()                        #On associe une variable à un champ input vide.
            if saisie == "q":                     #Si la saisie correspond à "q", on quitte la boucle
                    print("fin de la saisie")
                    break
            else:
                    name_dic[str(i)]=saisie       #Sinon on stock la saisie dans la liste.
                    i=i+1                         #On incrémente i de 1 pour passer à l'emplacement suivant dans la liste.
        name_dic=sorted(name_dic.values())        #A la sortie de la boucle, on trie le contenu de la liste par ordre alphabétique.
        print(name_dic)                           #Affichage de la liste.
addDic()                                          #Appel de la fonction.
