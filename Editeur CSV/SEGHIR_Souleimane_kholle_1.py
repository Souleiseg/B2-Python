#!/usr/bin/python3.6

#Import du module csv pour lire et écrire dans la liste de nombres.
import csv
#Import du module argparse pour pouvoir attribuer des options au programme.
import argparse
#Import du module pandas pour chercher le nombre le plus grand dans une colonne.
import pandas as pd

#On instancie une nouvelle classe ArgumentParser et on crée un message personnalisé.
parser = argparse.ArgumentParser(description='### [Manuel d\'utilisation de la commande] ### - Programme réalisé par : Souleimane SEGHIR [Ynov Informatique B2A]')

#On définit les options du progamme.
parser.add_argument('-l', '--list', help='Affiche le contenu de la liste.', action='store_true')
parser.add_argument('-a', '--add', nargs='+', help='Ajouter des nombres à la liste (ex: -a 12 -45 0.29).')
parser.add_argument('-c', '--clear', help='Supprimer tous les éléments de la liste.', action='store_true')
parser.add_argument('-s', '--select', help='Retourne une valeur en fonction de l\'option choisie (--max, --min, --moy, --sum).',action='store_true')
parser.add_argument('--max', help='Affiche la valeur maximum contenue dans la liste.', action='store_true')
parser.add_argument('--min', help='Affiche la valeur minimum contenue dans la liste.', action='store_true')
parser.add_argument('--moy', help='Affiche la moyenne de tous les élements de la liste.', action='store_true')
parser.add_argument('--sum', help='Affiche la somme de tous les éléments de la liste.', action='store_true')
parser.add_argument('-t', '--trier', help='Trie la liste dans l\'ordre croissant', action='store_true')
parser.add_argument('--desc', help='Trie la liste dans l\'ordre décroissant (utilisation : -t --desc).', action='store_true')
args = parser.parse_args()


# 1 - Afficher la liste des nombres.
if args.list:
  #On ouvre le fichier list.csv pour le lire.  
  with open('list.csv') as csvfile:
    reader = csv.reader(csvfile)
    print('\n   ###   Voici tous les éléments contenus dans le fichier   ###\n')
    i = 1
    #Boucle qui parcours le fichier et retourne toutes les valeurs de la colonne avec leur numéro de ligne.
    for row in reader:      
      print('Ligne n°{} : {}\n'.format(i, ''.join(row)))
      i += 1
    print('*** INFO - Si rien n\'apparait, c\'est que le fichier est vide. ***\n')


# 2 - Ajouter des nombres à la liste.
elif args.add:
  #On ouvre le fichier list.csv pour y écrire ('append' mode pour ne pas supprimer les nombres déjà présents).
  with open('list.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    #On récupère chaque nombre saisit en argument puis on les insère dans la liste.
    for number in args.add:
      csvfile.write(number + '\n')
    print('\nTous les éléments ont été ajoutés avec succès !\n')


# 3 - Supprimer tous les éléments de la liste.
elif args.clear:
  #On ouvre le fichier list.csv pour y écrire.
  with open('list.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    #On remplace tout le texte par le nom de la colonne.
    csvfile.write('Valeurs\n')
  print('\nTous les élements ont été supprimés avec succès !\n')


#Option -s qui permet de sélectionner puis retourner une valeur en fonction du paramètre saisit.
elif args.select:

  # 4 - Affiche la valeur maximum contenue dans la liste.
  if args.max:
    df = pd.read_csv('list.csv')
    p = df['Valeurs'].max()
    print('\nValeur maximum contenue dans la liste : {}\n'.format(p))


  # 5 - Affiche la valeur minimum contenue dans la liste.
  elif args.min:
    df = pd.read_csv('list.csv')
    p = df['Valeurs'].min()
    print('\nValeur minimum contenue dans la liste : {}\n'.format(p) )


  # 6 - Affiche la moyenne des valeurs contenues dans la liste.
  elif args.moy:
    df = pd.read_csv('list.csv')
    p = df['Valeurs'].mean()
    print('\nMoyenne des valeurs contenues dans la liste : {}\n'.format(p))


  # 7 - Affiche la somme de toutes les valeurs contenues dans la liste.
  elif args.sum:
    df = pd.read_csv('list.csv')
    p = df['Valeurs'].sum()
    print('\nSomme des valeurs contenues dans la liste : {}\n'.format(p))


# Option -t qui permet de modifier l'ordre des valeurs contenues dans la liste.
elif args.trier:

  # 8 - Trier dans l'ordre décroissant.
  if args.desc:
    df = pd.read_csv('list.csv')
    p = df.sort_values(by='Valeurs', ascending=False)
    p.to_csv('list.csv', index=False)
    print('\nListe triée dans l\'ordre décroissant avec succès !\n')
  
  # 9 - Trier dans l'ordre croissant.
  else:
    df = pd.read_csv('list.csv')
    p = df.sort_values(by='Valeurs', ascending=True)
    p.to_csv('list.csv', index=False)
    print('\nListe triée dans l\'ordre croissant avec succès !\n')

      
#Gestion des erreurs.
elif args.max or args.min or args.moy or args.sum:
    print('Erreur : Argument -s manquant.\n')

