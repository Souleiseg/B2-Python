#!/usr/bin/python3.6
#EXERCICE : 3a-save.py
#DESCRIPTION : Sauvegarde d'archives
#NOM : SEGHIR
#PRENOM : Souleimane
#DATE : 06/11/2018


import signal
import shutil
import gzip
import os
import sys
import subprocess


def closeProgramme(signal, frame):
    exit()

signal.signal(signal.SIGINT, closeProgramme)


# Creeer une Archive
def createArchive():
    os.remove(dossierData + '/archive.tar.gz')
    shutil.move(archive + '.tar.gz', dossierData)


# Supprime l'archive
def deleteArchive():
    if os.path.exists(archive + '.tar.gz'):
        os.remove(archive + '.tar.gz')
#
# Varibales
#

dossierData = os.path.expanduser('./data/')
dossierScripts = os.path.expanduser('../scripts')
archive = os.path.expanduser('./archive')

# Création dossier 'Data'
os.makedirs(dossierData, exist_ok=True)
sys.stdout.write('\nLe dossier \'data\' vient d\'être créé.\n')

shutil.make_archive(archive, 'gztar', dossierScripts)

# Existance d'une sauvegarde
if os.path.exists(dossierData + '/archive.tar.gz'):

    with gzip.open(dossierData + '/archive.tar.gz', 'rb') as f:
        exist_save = f.read()

    with gzip.open(archive + '.tar.gz', 'rb') as f:
        new_save = f.read()

    if exist_save != new_save:
        createArchive()
        sys.stdout.write('\nSUCCES - Sauvegarde créée dans le répertoire\'data\'.\n')

    else:
        deleteArchive()
        sys.stdout.write('\nSUCCES - Sauvegarde supprimée.\n')

else:
    shutil.move(archive + '.tar.gz', dossierData)
    sys.stdout.write('SUCCES - Sauvegarde archivée. \'data\'.\n')
