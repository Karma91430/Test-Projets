# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 14:56:04 2017

@author: Arthur Delerue TS6
"""
from tkinter import*

#import des différentes bases
import random
import time
import winsound

def lancer_chrono():
    None

def stoper_chrono():
    None
def top_horloge():
    None
    
def TEST():
    """
    fonction qui permet de tester l'animation
    de fin si l'on arrive pas à finir le jeu 
    (utile dans un cadre pédagogique).
    """
    global Nbr
    Nbr = 0
    
def tempsJeu():
    """
    Cette fonction permet de retenir un temps 
    lorsque le joueur gagne une partie,
    ce temps va permettre d'afficher son temps total
    de jeu par la suite.
    """
    global FIN
    FIN = ((float(time.time())) - debut)


    
def grille():
    v = 0
    for x in range(1,11):
       x_0 = 0 + v
       y_0 = 0
       x_1 = 0 + v
       y_1 = 500
       v = v + 50
       canva.create_line(x_0,y_0,x_1,y_1,
                         width = 1,fill = 'black')
        
    w = 0
    for y in range(1,11):
        x_0 = 0
        y_0 = 0 + w
        x_1 = 500
        y_1 = 0 + w
        w = w + 50
        canva.create_line(x_0,y_0,x_1,y_1,
                          width = 1,fill = 'black') 
def proba():
    """
    Cette fonction permet de faire apparaitre autant de case 
    coloré que l'on souhaite (entre 1 et 100) selon la probabilité
    rentrée par l'utilisateur. Bien sur le coloriage des cases est
    totalement aleatoire.
    """
    global etat, Nbr, temps, debut
    temps = True
    debut = time.time()
    canva.delete(ALL)
    grille()
    
    etat = []
    for i in range(11):
        etat.append([0] * 11)
    
    NbrCase = MonEntree.get()
    Nbr = (float(NbrCase)) * 100
    textNbrCases.config(text= int(Nbr))
    NbrCaseRouge = 0
    while NbrCaseRouge != Nbr:
        #abscisse et l'ordonnée de chaque case est 
        # définies aléatoirement par la fonction 
        #random.randint les chiffres entre parenthèses 
        #signifiants l'intérvalle
        abscisse = (random.randint(0, 9)) 
        ordonnee = (random.randint(0, 9)) 
        if etat[abscisse][ordonnee] == 0:
            x_0 = abscisse * 50
            y_0 = ordonnee * 50
            x_1 = x_0 + 50
            y_1 = y_0 + 50
            canva.create_rectangle(x_0,y_0,x_1,y_1,
                                   width = 1, fill = 'red4')
            NbrCaseRouge = NbrCaseRouge + 1
            etat[abscisse][ordonnee] = 1
            
def clic(case):
    """
    Cette fonction paramètre le changement 
    de couleur de chaque case lorsque l'on clic dessus selon un 
    modèle en croix.
    """
    global etat, Nbr, FIN, temps
    if case.widget==canva:
        #Toute cette partie permet d'avoir des 
        #coordonnées entières pour chaque case ce qui va 
        #faciliter le changement de couleur par la suite 
        x = round(case.x / 50)
        y = round(case.y / 50)
        if round(case.x / 50) > (case.x / 50):
            x = round(case.x / 50) - 1
        if (case.y / 50) < round(case.y / 50):
            y = round(case.y / 50) - 1
            
        x1 = x * 50
        y1 = y * 50
        x2 = x1 + 50
        y2 = y1 + 50
        # si l'etat est égal à 1 alors la case est colorée
        #si etat est égal à 0 alors elle est neutre
        if etat[x][y] == 0:
            canva.create_rectangle(x1,y1,x2,y2,
                                   width = 1, fill = 'red4')
            etat[x][y] = 1
            Nbr = Nbr + 1        
        elif etat[x][y] == 1:
            canva.create_rectangle(x1,y1,x2,y2,
                                   width = 1, fill = 'grey')
            etat[x][y] = 0
            Nbr = Nbr - 1
            
    #Les quatres parties qui vont suivre permettre de 
    #gérer la comptage des cases colorées aux bornes du quadrillage 
    #surtout dans les angles.
    
 #######################################################
        if x1 <= 400: 
            if etat[x + 1][y] == 0:
                canva.create_rectangle(x1 + 50,y1,x2 + 50,y2,
                                       width = 1, fill = 'red4')
                etat[x + 1][y] = 1
                Nbr = Nbr + 1
            elif etat[x + 1][y] == 1:
                canva.create_rectangle(x1 + 50,y1,x2 + 50,y2,
                                       width = 1, fill = 'grey')
                etat[x + 1][y] = 0
                Nbr = Nbr - 1
########################################
        if x1 >= 50:
            if etat[x - 1][y] == 0:
                canva.create_rectangle(x1 - 50,y1,x2 - 50,y2,
                                       width = 1, fill = 'red4')
                etat[x - 1][y] = 1
                Nbr = Nbr + 1
            elif etat[x - 1][y] == 1:
                canva.create_rectangle(x1 - 50,y1,x2 - 50,y2,
                                       width = 1, fill = 'grey')
                etat[x - 1][y] = 0
                Nbr = Nbr - 1
#######################################
        if y1 <= 400:
            if etat[x][y + 1] == 0:
                canva.create_rectangle(x1,y1 + 50,x2,y2 + 50,
                                       width = 1, fill = 'red4')
                etat[x][y + 1] = 1
                Nbr = Nbr + 1
            elif etat[x][y + 1] == 1:
                canva.create_rectangle(x1,y1 + 50,x2,y2 + 50,
                                       width = 1, fill = 'grey')
                etat[x][y  + 1] = 0
                Nbr = Nbr - 1
##########################################
        if y1 >= 50:
            if etat[x][y - 1] == 0:
                canva.create_rectangle(x1,y1 - 50,x2,y2 - 50,
                                       width = 1, fill = 'red4')
                etat[x][y - 1] = 1
                Nbr = Nbr + 1
            elif etat[x][y - 1] == 1:
                canva.create_rectangle(x1,y1 - 50,x2,y2 - 50,
                                       width = 1, fill = 'grey')
                etat[x][y - 1] = 0
                Nbr = Nbr - 1
#############################################
    #condition pour que la partie soit gagné 
    #avec une animation sonore de fin 
    textNbrCases.config(text= int(Nbr))
    if Nbr == 0 and temps:
        canva.delete(ALL)
        tempsJeu()
        textReussite.place(x=20 ,y=200)
        winsound.Beep(550, 700)
        winsound.Beep(550, 700)
        winsound.Beep(550, 1000)
        FenetreTotal.after(5000,destruction)
        stoper_chrono()
        
def destruction():
    """
    Affiche d'une bombe sur l'écran.
    """
    textReussite.destroy()
    canva.delete(ALL)
    x_0 = 200
    y_0 = 250
    x_1 = 300
    y_1 = 350
    canva.create_oval(x_0,y_0,x_1,y_1,
                      width = 1,fill = 'black') 
    v = 0
    for loop in range(4):
        x_0 = 249
        y_0 = 240 - v
        x_1 = 251
        y_1 = 250 - v
        v = v + 5
        canva.create_rectangle(x_0,y_0,x_1,y_1,
                               width = 1, fill = 'black')
    x_0 = 249
    y_0 = 225
    x_1 = 251
    y_1 = 235
    canva.create_rectangle(x_0,y_0,x_1,y_1,
                           width = 1, fill = 'red4')
    temps = False
    compte5()
    """
    Les 5 fonctions qui suivent permettrent 
    simplement l'affichage d'un compte-rebours
    avant que la bombe n'explose.
    """
def compte5(): 
    textexplosion = Label(FenetreTotal, text="5",
                       fg='red4', bg='grey',
                       font=('Verdana', 25, 'bold'))  
    textexplosion.place(x=245, y=120)
    FenetreTotal.after(1000,compte4)
    
def compte4():
    canva.delete(ALL)
    destruction()
    textexplosion = Label(FenetreTotal, text="4",
                          fg='red4', bg='grey',
                          font=('Verdana', 25, 'bold'))  
    textexplosion.place(x=245, y=120)
    FenetreTotal.after(1000,compte3)
    
def compte3():
    canva.delete(ALL)
    destruction()
    textexplosion = Label(FenetreTotal, text="3",
                          fg='red4', bg='grey',
                          font=('Verdana', 25, 'bold'))  
    textexplosion.place(x=245, y=120)
    FenetreTotal.after(1000,compte2)
    
def compte2():
    canva.delete(ALL)
    destruction()
    textexplosion = Label(FenetreTotal, text="2",
                          fg='red4', bg='grey',
                          font=('Verdana', 25, 'bold'))  
    textexplosion.place(x=245, y=120)
    FenetreTotal.after(1000,compte1)
    
def compte1():
    canva.delete(ALL)
    destruction()
    textexplosion = Label(FenetreTotal, text="1",
                          fg='red4', bg='grey',
                          font=('Verdana', 25, 'bold'))  
    textexplosion.place(x=245, y=120)
    FenetreTotal.after(1000,FinJeu)
    
def FinJeu():
    """
    Petite fenêtre pop-up qui informe l'utilisateur 
    qu'il a gagné au cas où la bombe n'aurait pas été clair.
    """
    FenetreTotal.destroy()
    FenetreFin = Tk()
    FenetreFin.geometry("400x300")
    FenetreFin.title("Fin du programme")
    FenetreFin.resizable(width=True , height=True) 
    texteFin = Label(FenetreFin, text="BOUMMMMMMM",
                          fg='red4', bg='white',
                          font=('Verdana', 25, 'bold'))  
    texteFin.place(x=30, y=150)  
    winsound.Beep(300, 1100)
    
###############################################
FenetreTotal = Tk()
FenetreTotal.geometry("800x600")
FenetreTotal.title("Projet 2")
FenetreTotal.resizable(width=True , height=True)

canva = Canvas(FenetreTotal,width = 500,
               height = 500, bg = "grey")
canva.place(x=0,y=0)

MonEntree = Entry(FenetreTotal)
MonEntree.place(x = 600, y = 250)
MonEntree.focus()

textHorscanva = Label(FenetreTotal, text="Clic en dehors du canva !",
                       fg='white', bg='black',
                       font=('Verdana', 12, 'bold'))
text = Label(FenetreTotal, width = 22, text="Nombre de cases présentes :",
             fg = 'white',bg='black', anchor="w")
text.place(x=600, y=10)
textNbrCases = Label(FenetreTotal, width = 5, text="",
                     fg = 'white',bg='black', anchor="w")
textNbrCases.place(x=600, y=50)

#le programme va afficher le temps de jeu arrondi a deux 
#chiffres après la virgule
global debut, temps, minutes, secondes 

message = ""
textReussite = Label(FenetreTotal, width = 43,
                     text= message,
                     font = ('Courier',13,'bold underline'),
                     fg = 'white', bg='grey', anchor='w')


BoutonStart = Button(FenetreTotal, text='VALIDER', width=10,
                     height=1,fg = 'white',bg = 'black',
                     command = proba)
BoutonStart.place(x =600,y = 300 )
Boutontest = Button(FenetreTotal, text='test', width=10,
                     height=1,fg = 'black',bg = 'red4',
                     command = TEST)
Boutontest.place(x =600,y = 480 )
textProba = Label(FenetreTotal, width = 10, text="Probabilitée :",
                     fg = 'white',bg='black', anchor="w")
textProba.place(x=600, y=200)
#deux lignes qui permettent de capter le clic de la souris
FenetreTotal.bind("<ButtonPress-1>", clic)
FenetreTotal.bind("<ButtonPress-3>", clic)
temps = False

grille()
lancer_chrono()
FenetreTotal.mainloop() 