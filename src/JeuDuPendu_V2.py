from random import * 

# ouverture du fichier texte 
f=open("liste.de.mots.francais.frgut.txt",'r')
lignes = f.read().splitlines()
f.close()

liste_de_mots_a_deviner= lignes
index_du_mot_a_deviner = randint(0,len(liste_de_mots_a_deviner)-1)

mot_a_deviner= liste_de_mots_a_deviner[index_du_mot_a_deviner]

mot_en_cours=''

for index in range(0, len(mot_a_deviner)):
    mot_en_cours = mot_en_cours + "-"

nombre_de_vie=10

while True:
    print("Le nombre de vie restante est : ", nombre_de_vie)

    print("Le mot à deviner est : ", mot_en_cours)

    lettre_proposee=input("Entrez une lettre : ")

    une_lettre_trouvee = False

    for index in range (0,len(mot_a_deviner)):
        if lettre_proposee == mot_a_deviner[index]:
            mot_en_cours = mot_en_cours[:index] + lettre_proposee + mot_en_cours[index + 1:]
            une_lettre_trouvee = True

    if not une_lettre_trouvee:
        nombre_de_vie = nombre_de_vie - 1

    if nombre_de_vie == 0:
        print('bouhhhhhhhhhh tu as perdu !!! Le mot était :',mot_a_deviner,'. C était facile pourtant.')
        break
    elif mot_a_deviner == mot_en_cours :
        print("tu as gagné. le mot était :", mot_en_cours)
        break

