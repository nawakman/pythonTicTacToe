"""
-----------------------------------------------------------------------------------
Projet TicTacToe
-----------------------------------------------------------------------------------
Les fonctions ci-dessous proposent des solutions de scripts permettant de
programmer un jeu de morpion. On vous demande de prendre en main ces fonctions
puis de compléter le programme afin de pouvoir faire intervenir 2 joueurs sur
ce jeu.

a) Modifier le programme principal afin de faire jouer alternativement le joueur 1
et le joueur 2.

b) Compléter la fonction valider(grille) puis l'insérer dans le jeu après chaque coup joué afin de savoir
si une partie est gagnée. Précisez le numéro du joueur qui a gagné la partie.

c) Faire en sorte que les "1" et les "2" soient remplacés par les caractères "X" et "O" dans l'affichage
de la grille.

d) Créer une fonction capable de vérifier si le coup tenté par un joueur a déjà
été proposé. Insérer cette fonction dans le jeu pour l'afficher au joueur afin qu'il change sa proposition.

e) Bonus : Proposer une version sous Tkinter de votre programme.


"""
player1=["Player 1","♀"]
player2=["Player 2","O"]

def affiche(grille):
    print("---------")
    for i in range (3):
        print( grille[i][0], '|', grille[i][1], '|', grille[i][2])
        print("---------")
    print('\n')
    
def jouer(grille, player):
    print(player[0]," -> position to tick x,y :")
    jeu = input()
    jeu = jeu.split(",") #avec la methode split jeu est devenue une variable de type list
    if grille[int(jeu[0])-1][int(jeu[1])-1] == " ": #cannot overwrite other player move
        grille[int(jeu[0])-1][int(jeu[1])-1]=player[1] #modifie l'élément de la grille
    else:
        print("cannot play, other player already used this  position")
        jouer(grille, player)

    return grille
   
def valider (grille, player):#not a lot of possible combinations, we can manually verify
    if (#joueur 1
        grille[0]==[player[1],player[1],player[1]]#ligne 1
        or grille[1]==[player[1],player[1],player[1]]#ligne 2
        or grille[2]==[player[1],player[1],player[1]]#ligne 3
        or (grille[0][0]==player[1] and grille[1][0]==player[1] and grille[2][0]==player[1])#colonne 1
        or (grille[0][1]==player[1] and grille[1][1]==player[1] and grille[2][1]==player[1])#colonne 2
        or (grille[0][2]==player[1] and grille[1][2]==player[1] and grille[2][2]==player[1])#colonne 2
        or (grille[0][0]==player[1] and grille[1][1]==player[1] and grille[2][2]==player[1])#diagonale 1
        or (grille[0][2]==player[1] and grille[1][1]==player[1] and grille[2][0]==player[1])#diagonale 1
    ):
        return player[0]#return player name
    else:
        if end_game(grille) == True:
            return "end"
        return " "

def start_game():
    grille=[[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]] # create empty new grid
    affiche(grille)#print the grid for the first time
    winner=" "
    while winner==" " :#game loop
        jouer(grille, player1)
        winner=valider(grille, player1)
        affiche(grille)
        if winner!=" ":#player 1 can win before player 2 play
            break
        jouer(grille, player2)
        winner=valider(grille, player2)
        affiche(grille)
    if winner == player1[0] or winner == player2[0]:
        print(winner," won !!!")
        restart()
    elif winner == "end":
        print("no winner")
        restart()    

def end_game (grille):
    counter=0
    for i  in range(3):
        for j in range(3):
            if grille[i][j] != " ":
                counter+=1
    if counter == 9:
        return True
    else:
        return False

def restart ():
    if input("Restart Y/N")=="y":
        start_game()
    else:
        return

player1[0]=input("player 1, choose youe name...")
player1[1]=input(player1[0] + ", choose your symbol...")
player2[0]=input("Player 2, choose your name...")
player2[1]=input(player2[0] + ", choose your symbol...")
start_game()