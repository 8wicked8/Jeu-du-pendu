from random import *
from Potence import *

# ouverture du fichier texte 
f=open("src/liste.de.mots.francais.frgut.txt",'r')
lignes = f.read().splitlines()
f.close()

# Initialize les variable globales
liste_de_mots_a_deviner= lignes
index_du_mot_a_deviner = randint(0,len(liste_de_mots_a_deviner)-1)

mot_a_deviner= liste_de_mots_a_deviner[index_du_mot_a_deviner]

mot_en_cours=''

for index in range(0, len(mot_a_deviner)):
    mot_en_cours = mot_en_cours + "-"

nombre_de_vie=11

# Fonction pour changer les variables et redessiner la zone de dessin.
def redessiner():

    global nombre_de_vie
    global mot_en_cours
    global textEntry

    lettre_proposee = textEntry.get()
    textEntry.delete(0, len(lettre_proposee))

    # Met à jour les variables en fonction de la lettre saisie
    if (len(lettre_proposee) == 1):
        une_lettre_trouvee = False

        for index in range (0,len(mot_a_deviner)):
            if lettre_proposee == mot_a_deviner[index]:
                mot_en_cours = mot_en_cours[:index] + lettre_proposee + mot_en_cours[index + 1:]
                une_lettre_trouvee = True

        if not une_lettre_trouvee:
            nombre_de_vie = nombre_de_vie - 1

    # Efface la zone de dessin
    canvas.delete("all")

    # Dessine la potence
    dessiner(canvas, nombre_de_vie)

    # En fonction de où on est dans le jeu, affiche le texte qui va bien
    if nombre_de_vie <= 0:
        canvas.create_text(200, 50, text='tu as perdu !!! Le mot était : ' + mot_a_deviner)
    elif mot_a_deviner == mot_en_cours :
        canvas.create_text(200, 50, text="tu as gagné. le mot était bien : " + mot_en_cours)
    else:
        canvas.create_text(200, 420, text="Le nombre de vie restante est : " + str(nombre_de_vie))
        canvas.create_text(200, 440, text="Le mot à deviner est : "+ str(mot_en_cours))


# Initialize interface graphique
tk = Tk()
tk.title('Le jeu du pendu')
# zone de dessin
canvas = Canvas(tk, width=500, height=500)
canvas.grid(row = 1, column = 1, columnspan=3)
# Etiquette
invitationLabel = Label(tk, text="Entrez une lettre : ")
invitationLabel.grid(row = 2, column = 1)
# Champ texte
textEntry = Entry(tk, width=10)
textEntry.grid(row = 2, column = 2)
# Bouton Ok
boutonOk = Button(tk, text="Ok", command=redessiner)
boutonOk.grid(row = 2, column = 3)

redessiner()

tk.mainloop()

