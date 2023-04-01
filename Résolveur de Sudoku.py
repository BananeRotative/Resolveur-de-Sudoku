import turtle
import copy
EnCoursDeResolution = False                                                     #True ou False selon si le programme calcule ou non les valeurs du Sudoku

turtle.title("Sudoku à Résoudre")
turtle.speed(0)

def dessinBoutonTerminer():                                                     #Dessine le bouton terminer qui permet d'arrêter d'écrire des nombres et de résoudre le Sudoku
    turtle.up()
    turtle.goto(170,250)
    turtle.setheading(0)
    turtle.down()
    for t in range(2):
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(35)
        turtle.right(90)
    turtle.up()
    turtle.goto(180,220)
    turtle.write("Terminer",font = ("Arial",16,"normal"))
    turtle.goto(-330,280)

def dessin_grille():                                                            #dessiner la grille de Sudoku
    turtle.up()
    turtle.goto(-330,280)
    turtle.setheading(0)
    turtle.down()
    for i in range(2):
        turtle.width(3)
        turtle.forward(450)
        turtle.backward(450)
        for i in range(3):
            for i in range(3):
                turtle.width(2)
                turtle.right(90)
                turtle.forward(50)
                turtle.left(90)
                if i==2:
                    turtle.width(3)
                else:
                    turtle.width(2)
                turtle.forward(450)
                turtle.backward(450)
        turtle.left(90)
    return

    for i in range(2):
        turtle.width(3)
        turtle.forward(450)
        turtle.backward(450)
        for i in range(3):
            for i in range(3):
                turtle.width(2)
                turtle.right(90)
                turtle.forward(50)
                turtle.left(90)
                if i==2:
                    turtle.width(3)
                else:
                    turtle.width(2)
                turtle.forward(450)
                turtle.backward(450)
        turtle.left(90)
    return

def dessinNb(case,chiffre):                                                     #dessiner un chiffre donné dans une case donnée
    if EnCoursDeResolution == False or SudokuTermine == 1:
        if Debut == 1:
            Nombres[case] = chiffre
        turtle.up()
        turtle.goto((case%9)*50-315,(case//9)*-50+231)
        turtle.width(2)
        turtle.setheading(0)
        turtle.write(chiffre,font = ("Arial",30,"normal"))
        turtle.up()
        turtle.goto((case%9)*50-330,(case//9)*-50+280)
        turtle.down()
    return

def EffacerTurtle():                                                            #Effacer l'entièreté de l'écran avec la tortue
    turtle.color('white')
    turtle.down()
    turtle.width(1000)
    turtle.goto(0,0)
    turtle.width(2)
    turtle.up()
    turtle.color('black')

def NbOuEtQuoi(X,Y):                                                            #Réagit à un clic de souris selon les coordonées
    if EnCoursDeResolution == False:
        global IsFilling
        if IsFilling == 0:
            if X > 170 and X < 270 and Y < 250 and Y > 215:                     #Si les coordonnées du clic sont sur le bouton Terminer
                EffacerCase(CaseSelect)
                ResoudreSudoku()
            elif X > -330 and X < 120 and Y > -170 and Y < 280:                 #Si les coordonnées du clic sont sont le Sudoku
                xCase = (X+330)//50                                             #calcul de l'absisse de la case
                yCase = ((Y-280)//50)*-1-1                                      #calcul de l'ordonnée de la case
                Case = yCase*9+xCase                                            #calcul du numéro de case
                IsFilling = 1                                                   #Indique que la turtle trace déjà
                EffacerCase(CaseSelect)                                         #Retire l'affichage de la sélection de l'ancienne case et le chiffre si il y en a un
                if len(Nombres)-1 >= CaseSelect:
                    if not Nombres[CaseSelect] == 0:
                        dessinNb(CaseSelect,Nombres[CaseSelect])                #Replace le chiffre si il a été retiré de la case précédemment sélectionnée
                SelectionCase(int(Case))                                        #Sélectionne une nouvelle case
                IsFilling = 0                                                   #indique que la turtle ne trace plus


def EffacerCase(case):                                                          #Efface le contenu d'une case donnée
    fond.up()
    fond.goto((case%9)*50-328,(case//9)*-50+278)
    fond.setheading(0)
    fond.begin_fill()
    for o in range(4):
        fond.forward(46)
        fond.right(90)
    fond.color('white')
    fond.end_fill()
    fond.color('black')

def SelectionCase(case):                                                        #Affiche la sélection d'une case donnée
    global CaseSelect
    fond.up()
    fond.goto((case%9)*50-328,(case//9)*-50+278)
    fond.setheading(0)
    fond.begin_fill()
    for o in range(4):
        fond.forward(46)
        fond.right(90)
    fond.color('grey')
    fond.end_fill()
    fond.color('black')
    if len(Nombres)-1 >= case:
        if type(Nombres[case]) is int:
            if not Nombres[case] == 0:
                dessinNb(case,Nombres[case])
    CaseSelect = case


def EntreeDesNombres():                                                         #Démarre la boucle d'écoute de l'appui des touches, qui permet à l'utilisateur d'indiquer au programme quel Sudoku il doit résoudre
    global CaseSelect
    turtle.onscreenclick(NbOuEtQuoi)                                            #Execute la fonction permettant de réagir à un clic de souris en cas de clic sur l'écran de la turtle
    screen.onkey(lambda : dessinNb(CaseSelect,1),"1")                           #Enregistre le chiffre "1" sur la case sélectionnée et l'enregistre
    screen.onkey(lambda : dessinNb(CaseSelect,2),"2")                           # //
    screen.onkey(lambda : dessinNb(CaseSelect,3),"3")                           # //
    screen.onkey(lambda : dessinNb(CaseSelect,4),"4")                           # //
    screen.onkey(lambda : dessinNb(CaseSelect,5),"5")                           # //
    screen.onkey(lambda : dessinNb(CaseSelect,6),"6")                           # //
    screen.onkey(lambda : dessinNb(CaseSelect,7),"7")                           # //
    screen.onkey(lambda : dessinNb(CaseSelect,8),"8")                           # //
    screen.onkey(lambda : dessinNb(CaseSelect,9),"9")                           # //
    screen.onkey(AppuiZero,"0")
    screen.listen()                                                             #Commencer à écouter les instructions d'events
    screen.mainloop()                                                           #Démarre la boucle d'events

def AppuiZero():
    EffacerCase(CaseSelect)
    Nombres[CaseSelect] = 0
    SelectionCase(CaseSelect)

def SupprListeNombres(case,A_Supprimer):                                        #supprime de la liste Nombres, sur la case indiquée la possibilité indiquée
    global Changement
    global Nombres
    for m in range(len(Nombres[case])):
        if Nombres[case][m]==A_Supprimer:
            del Nombres[case][m]
            Changement = 1
            break
    return

def ActualiserColonnes():                                                       #Retire les chiffres connus d'une colonne des possibilités de toutes les cases inconnues de la même colonne
    for i in range(81):
        if type(Nombres[i]) is list:
            for h in range(9,73,9):
                if i-h > -1 and type(Nombres[i-h]) is int:
                    SupprListeNombres(i,Nombres[i-h])
                if i+h < 81 and type(Nombres[i+h]) is int:
                    SupprListeNombres(i,Nombres[i+h])

def ActualiserLignes():                                                         #Retire les chiffres connus d'une ligne des possibilités de toutes les cases inconnues de la même ligne
    for i in range(81):
        if type(Nombres[i]) is list:
            for h in range(1,9):
                if i//9==(i-h)//9:
                    if type(Nombres[i-h]) is int:
                        SupprListeNombres(i,Nombres[i-h])
                if i//9==(i+h)//9:
                    if type(Nombres[i+h]) is int:
                        SupprListeNombres(i,Nombres[i+h])

Carres = [[0,1,2,9,10,11,18,19,20],[3,4,5,12,13,14,21,22,23],[6,7,8,15,16,17,24,25,26],[27,28,29,36,37,38,45,46,47],[30,31,32,39,40,41,48,49,50],[33,34,35,42,43,44,51,52,53],[54,55,56,63,64,65,72,73,74],[57,58,59,66,67,68,75,76,77],[60,61,62,69,70,71,78,79,80]]
#Definit une liste d'éléments de la liste Nombres pour chaque carré (un carré fait 3x3 cases) du Sudoku. On peut ainsi vérifier si des nombres sont dans la même case.

def MemeCarre(Case1,Case2):                                                     #indique True ou False selon si les nombres indiqués sont dans le même carre ou non
    NumMemeCarre=-1
    for k in range(9):
        for l in range(9):
            if Carres[k][l]==Case1:
                NumMemeCarre=k
                break
    message="False"
    for k in range(9):
        if Carres[NumMemeCarre][k]==Case2:
            message="True"
            break
    return message

def ActualiserCarres():                                                         #Retire les chiffres connus d'un carré des possibilités de toutes les cases inconnues du même carré
    for i in range(81):
        if type(Nombres[i]) is list:
            for h in [1,2,7,8,9,10,11,16,17,18,19,20]:
                if i-h > -1:
                    if type(Nombres[i-h]) is int and MemeCarre(i,i-h)=="True":
                        SupprListeNombres(i,Nombres[i-h])
                if i+h < 81:
                    if type(Nombres[i+h]) is int and MemeCarre(i,i+h)=="True":
                        SupprListeNombres(i,Nombres[i+h])

def RemplirDernièreOptionCases():                                               #Valider la possibilité restante d'une case lorqu'il n'en reste qu'une
    global Changement
    global Nombres
    for i in range(81):
        if Nombres[i] is list:
            if len(Nombres[i])==1:
                Nombres[i] = Nombres[i][0]
                Changement = 1

def RemplirDernièreOption(Verrif):                                              #Valider une case lorsque c'est le dernier endroit où un chiffre peut être dans la colonne/ligne/carré
    global Changement
    global Nombres
    for i in range(9):                                                          #Les noms des variables et listes sont pour les colonnes mais cette fonction fonctionne aussi pour les lignes et carrés
        if Verrif=="Colonne":
            ContenuColonne = [Nombres[i],Nombres[i+9],Nombres[i+18],Nombres[i+27],Nombres[i+36],Nombres[i+45],Nombres[i+54],Nombres[i+63],Nombres[i+72]]
        elif Verrif=="Ligne":
            ContenuColonne = [Nombres[i*9],Nombres[i*9+1],Nombres[i*9+2],Nombres[i*9+3],Nombres[i*9+4],Nombres[i*9+5],Nombres[i*9+6],Nombres[i*9+7],Nombres[i*9+8]]
        elif Verrif=="Carre":
            ContenuColonne = []
            for h in range(9):
                ContenuColonne.append(Nombres[Carres[i][h]])
        CompterPossibilites = [0] * 9
        for h in range(9):
            if type(ContenuColonne[h]) is int:
                CompterPossibilites[ContenuColonne[h]-1] = 2
            elif type(ContenuColonne[h]) is list:
                for k in ContenuColonne[h]:
                    CompterPossibilites[k-1] = CompterPossibilites[k-1] + 1
        for p in range(9):
            if CompterPossibilites[p] == 1:
                for h in range(9):
                    if type(ContenuColonne[h]) is list:
                        for k in range(len(ContenuColonne[h])):
                            if ContenuColonne[h][k] == p+1:
                                if Verrif == "Colonne":
                                    Nombres[i+9*h] = p+1
                                    Changement = 1
                                elif Verrif == "Ligne":
                                    Nombres[i*9+h] = p+1
                                    Changement = 1
                                elif Verrif == "Carre":
                                    Nombres[Carres[i][h]] = p+1
                                    Changement = 1

def RéduirePossibilitesPourDeux(Verrif):                                        #Lorsque deux cases contiennent les mêmes deux possibilités et sont sur la même colonne, supprimer ces possibilités sur le reste de la colonne
    for i in range(9):                                                          #idem pour les lignes et carrés (le nom "colonne" a été gardé quand même)
        if Verrif=="Colonne":
            ContenuColonne = [Nombres[i],Nombres[i+9],Nombres[i+18],Nombres[i+27],Nombres[i+36],Nombres[i+45],Nombres[i+54],Nombres[i+63],Nombres[i+72]]
        elif Verrif=="Ligne":
            ContenuColonne = [Nombres[i*9],Nombres[i*9+1],Nombres[i*9+2],Nombres[i*9+3],Nombres[i*9+4],Nombres[i*9+5],Nombres[i*9+6],Nombres[i*9+7],Nombres[i*9+8]]
        elif Verrif=="Carre":
            ContenuColonne = []
            for h in range(9):
                ContenuColonne.append(Nombres[Carres[i][h]])
        for h in range(8):
            if type(ContenuColonne[h]) is list:
                if len(ContenuColonne[h]) == 2:
                    for k in range(h*-1+8):
                        if type(ContenuColonne[h+k+1]) is list:
                            if ContenuColonne[h] == ContenuColonne[h+k+1]:
                                ASupprimer1 = ContenuColonne[h][0]
                                ASupprimer2 = ContenuColonne[h][1]
                                for l in range(9):
                                    if type(ContenuColonne[l]) is list and not ContenuColonne[l] == ContenuColonne[h]:
                                        if Verrif == "Colonne":
                                            SupprListeNombres(i+9*l,ASupprimer1)
                                            SupprListeNombres(i+9*l,ASupprimer2)
                                        elif Verrif == "Ligne":
                                            SupprListeNombres(i*9+l,ASupprimer1)
                                            SupprListeNombres(i*9+l,ASupprimer2)
                                        elif Verrif == "Carre":
                                            SupprListeNombres(Carres[i][l],ASupprimer1)
                                            SupprListeNombres(Carres[i][l],ASupprimer2)

def Contradiction():                                                            #Renvoie "True" ou "False" selon si les règles du Sudoku sont respectées pour les cases trouvées
    message = "False"                                                           #Permet de vérifier si le Sudoku est résoluble ou non
    for i in range(81):
        if type(Nombres[i]) is int:
            for h in range((i//9)*9,(i//9)*9+9):
                if Nombres[i] == Nombres[h]:
                    if not i == h:
                        message = "True"
                        print("Contradiction : Sur la ligne,avec i=",i,"et h=",h)
            for h in range(i%9,i%9+73,9):
                if Nombres[i] == Nombres[h]:
                    if not i == h:
                        message = "True"
                        print("Contradiction : Sur la colonne, avec i=",i,"et h=",h)
            NumCarre=-1
            for k in range(9):
                for l in range(9):
                    if Carres[k][l]==i:
                        NumCarre=k
                        break
            for h in Carres[NumCarre]:
                if Nombres[i] == Nombres[h]:
                    if not i == h:
                        message = "True"
                        print("Contradiction : sur le carré, avec i=",i,"et h=",h)
        elif type(Nombres[i]) is list:
            if len(Nombres[i]) == 0:
                message = "True"
                print("Contradiction : Plus de possibilités sur la case :",i)
    return message

def ResoudreSudoku():                                                           #La fonction principale, exécutant et coordonnant les autres fonctions
    global EnCoursDeResolution
    global Nombres
    global SudokuTermine
    print("Resoudre Sudoku")
    if EnCoursDeResolution == False:                                            #Si le Sudoku n'est pas déjà en train de se résoudre
        EnCoursDeResolution = True                                              #Permet d'éviter que plusieurs clics sur le bouton Terminer ne démarrent plusieurs fois en même temps la résolution du Sudoku
        for t in range(81):                                                     #Remplit les cases non indiquées par [1,2,3,4,5,6,7,8,9] ce qui correspond aux 9 possibilités
            if Nombres[t] == 0:
                Nombres[t] = [1,2,3,4,5,6,7,8,9]
        print("Nombres :",Nombres)

        SudokuTermine = 0                                                       #Définition des variables et listes
        Changement = 0
        Note = -1
        SauvNombres = []
        Hypotheses = []
        CasesHypotheses = []
        Boucle = 1
        Debut = 0
        while SudokuTermine==0:                                                 #Tant que le Sudoku contient des cases inconnues:
            ActualiserLignes()                                                  #Exécute les fonctions de résolution du Sudoku
            ActualiserColonnes()
            ActualiserCarres()

            RemplirDernièreOptionCases()
            RemplirDernièreOption("Colonne")
            RemplirDernièreOption("Ligne")
            RemplirDernièreOption("Carre")

            RéduirePossibilitesPourDeux("Colonne")
            RéduirePossibilitesPourDeux("Ligne")
            RéduirePossibilitesPourDeux("Carre")



            print("Boucle N°",Boucle)

            SudokuTermine=1                                                     #Arrête les tests si le Sudoku est résolu
            for i in range(81):
                if type(Nombres[i]) is list:
                    SudokuTermine = 0
            if SudokuTermine == 1:
                print("SUDOKU TERMINE")
                break

            if Note > -1:                                                       #Si on a fait au moins une hypothèse:
                print("Note > -1")
                if Contradiction() == "True":                                   #Si le Sudoku n'est plus résoluble
                    print("Contradiction = 'True'")
                    if Nombres == SauvNombres[Note]:
                        print("Déjà pareils avant la Sauvegarde")
                    Nombres = SauvNombres[Note]                                 #Revenir à la dernière sauvegarde de Nombres
                    del SauvNombres[Note]                                       #Supprimer la dernière sauvegarde de Nombres
                    SupprListeNombres(CasesHypotheses[Note],Hypotheses[Note])   #Supprimer des possibilités l'hypothèse ayant été testée
                    print("Nombres[",CasesHypotheses[Note],"] =",Nombres[CasesHypotheses[Note]])
                    print("Hypotheses[",Note,"] =",Hypotheses[Note])
                    del CasesHypotheses[Note]                                   #Supprimer de la mémoire la dernière case d'hypothèse et
                    del Hypotheses[Note]                                        # la dernière hypothèse
                    Note = Note - 1                                             #Retirer 1 à Note
                    Changement = 1
                    if Note + 1 == len(SauvNombres) and Note + 1 == len(Hypotheses) and Note + 1 == len(CasesHypotheses):
                        print("Note, SauvNombres, Hypotheses et CasesHypotheses sont toujours coordonnés")


            if Changement == 0:                                                 #Si rien n'a changé durant une boucle entière:
                print("Changement == 0 à la Boucle N°",Boucle)
                SauvNombres.append([])
                Note = Note + 1                                                 #Ajouter 1 à la variable Note, qui permet de numéroter les listes SauvNombres, Hypotheses et CasesHypotheses
                SauvNombres[Note] = copy.deepcopy(Nombres)                      #Copie l'entièreté de Nombres dans une liste de SauvNombres, nommée SauvNombres[Note] (pour la dernière sauvegarde)
                print("len(SauvNombres) :",len(SauvNombres))
                if len(SauvNombres) == Note + 1:
                    print("Note est coordonné à SauvNombres")
                if not SauvNombres[Note] == Nombres:
                    print("SauvNombres EST MAL ENREGISTRE !!!")

                Trouve = 0                                                      #On cherche à avoir la longueur d'hypothèses de la case testée la plus petite possible
                for h in [2,3,4,5,6,7,8,9,1]:                                           #Emet une hypothèse
                    for i in range(81):
                        if type(Nombres[i]) is list:
                            if len(Nombres[i]) == h:
                                print("CA Y EST !!!")
                                Hypotheses.append(Nombres[i][0])
                                CasesHypotheses.append(i)
                                Trouve = 1                                      #Indique que l'on a trouvé une hypothèse
                                print(Hypotheses)
                                print(CasesHypotheses)
                                break
                    if Trouve == 1:
                        break
                if Trouve == 0:
                    print("AUCUN NOMBRE TESTE")
                    print(Nombres)
                print("Note :",Note)
                print("CasesHypotheses :",CasesHypotheses)
                print("CasesHypotheses[Note] :",CasesHypotheses[Note])
                print("SauvNombres[Note]",SauvNombres[Note])
                print("SauvNombres :",SauvNombres[Note][CasesHypotheses[Note]])

                if len(Hypotheses) == Note + 1:
                    print("Note est bien coordonné à Hypotheses")
                else:
                    break


                Nombres[CasesHypotheses[Note]] = Hypotheses[Note]               #On assigne à la case testée l'hypothèse choisie
                if Nombres == SauvNombres[Note]:
                    print("CA MARCHE PAS")

            Changement = 0                                                      #Réinitialise la variable "Changement"
            Boucle = Boucle + 1

        for i in range(9):
            for h in range(9):
                print("Colonne",i,"Ligne",h,":",Nombres[i+9*h])


        EffacerTurtle()                     #Effacer l'affichage actuel du Sudoku
        dessin_grille()                     #Redessiner le Sudoku

        for i in range(81):                 #Dessiner les chiffres trouvés pour le Sudoku
                dessinNb(i,Nombres[i])

#Fin des définitions de fonctions

dessin_grille()                 #dessine la grille de Sudoku
dessinBoutonTerminer()          #dessine le bouton Terminer
Nombres = [0] * 81              #définit Nombres  -->  Définit le Sudoku comme étant entièrement inconnu pour le moment
screen = turtle.Screen()
Debut,IsFilling = 1,0           #Debut : permet de dire à la fonction dessinNb qu'il faut aussi modifier la liste Nombres. IsFilling : Permet d'empêcher à l'utilisateur de demander à la tortue de remplir deux cases à la fois.
fond = turtle.Turtle()          #Nouvelle tortue qui s'occupe de remplir des zones (comme la sélection ou effacer)
fond.speed(0)                   #Retire les animations de tortue
fond.hideturtle()               #cache la tortue "fond"
turtle.hideturtle()             #cache la tortue "turtle"
CaseSelect = 0
SelectionCase(0)                #Sélectionne la case en haut à gauche
EntreeDesNombres()              #Démarre l'attente des events (clics et chiffres de 1 à 9)

#Fin du programme