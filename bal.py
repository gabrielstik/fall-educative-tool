# Simulateur de chute *** Créé par Gabriel Stik et Maxime Couette *** 2016

# -*- coding:utf-8 -*-
from tkinter import *
import time

# Initialisation des variables de base

hauteur = 10
lastParam_hauteur = 10
coef_gravite = 9.8
lastParam_gravite = coef_gravite # Permet de conserver le dernier paramètre de gravité à la réinitisation
vitesse = 0
rebond = 0
trouNoir = False
rayon = 0
y = 40
t = 0
hauteur_impact = 0
vitesse_impact = 0
rebondBool = True
t_impact = 0
deletedForTrouNoir = False

# Def lorsqu'on change la hauteur

def setEarth():
	global coef_gravite, bg_color, lastParam_gravite, trouNoir
	coef_gravite = 9.8
	lastParam_gravite = coef_gravite
	leftContainer.configure(bg="#006699")
	labelLieu.configure(text="Terre")
	trouNoir = False  # Mystère...
	reset() # On réinitialise la balle et les statistiques lorsqu'on change de milieu

def setMoon():
	global coef_gravite, bg_color, lastParam_gravite, trouNoir
	coef_gravite = 1.6
	lastParam_gravite = coef_gravite
	leftContainer.configure(bg="#a0a0a0") # On modifie la couleur du fond
	labelLieu.configure(text="la Lune")
	trouNoir = False
	reset()

def setMars():
	global coef_gravite, bg_color, lastParam_gravite, trouNoir
	coef_gravite = 3.7
	lastParam_gravite = coef_gravite
	leftContainer.configure(bg="#993300")
	labelLieu.configure(text="Mars")
	trouNoir = False
	reset()

def setNeptune():
	global coef_gravite, bg_color, lastParam_gravite, trouNoir
	coef_gravite = 11.6
	lastParam_gravite = coef_gravite
	leftContainer.configure(bg="#663366")
	labelLieu.configure(text="Neptune")
	trouNoir = False
	reset()

def setJupiter():
	global coef_gravite, bg_color, lastParam_gravite, trouNoir
	coef_gravite = 24.8
	lastParam_gravite = coef_gravite
	leftContainer.configure(bg="#cc9966")
	labelLieu.configure(text="Jupiter")
	trouNoir = False
	reset()

def setSun():
	global coef_gravite, bg_color, lastParam_gravite, trouNoir
	coef_gravite = 274.1
	lastParam_gravite = coef_gravite
	leftContainer.configure(bg="#cc9933")
	labelLieu.configure(text="le Soleil")
	trouNoir = False
	reset()

def setTatooine():
	global coef_gravite, bg_color, lastParam_gravite, trouNoir
	coef_gravite = 10
	lastParam_gravite = coef_gravite
	leftContainer.configure(bg="#996600")
	labelLieu.configure(text="Tatooine")
	trouNoir = False
	reset()

def setSing():  # De la pesanteur dans un trou noir ?...
	global coef_gravite, bg_color, trouNoir
	leftContainer.configure(bg="black")
	labelLieu.configure(text="#!@%/§")
	trouNoir = True
	if y == 40:
		singularite = leftContainer.create_oval(90, 20, 110, 40, fill="white")
	reset()

# Def lorsqu'on change le milieu

def setHauteur():
	global hauteur, lastParam_hauteur
	strHauteur = entree_hauteur.get() # On récupère le texte écrit dans l'Entry
	if strHauteur != "":
		hauteur = float(strHauteur)
		lastParam_hauteur = hauteur
		entryHauteur.delete(0, END)  # On efface le contenu de l'Entry
		labelHauteur.configure(text=str(round(hauteur,1))+" m")
		reset()

def setBurj():
	global hauteur, lastParam_hauteur
	hauteur = 830
	lastParam_hauteur = hauteur
	labelHauteur.configure(text=str(round(hauteur,1))+" m")
	reset()

def setEiffel():
	global hauteur, lastParam_hauteur
	hauteur = 324
	lastParam_hauteur = hauteur
	labelHauteur.configure(text=str(round(hauteur,1))+" m")
	reset()

def setAvion():
	global hauteur, lastParam_hauteur
	hauteur = 11890
	lastParam_hauteur = hauteur
	labelHauteur.configure(text=str(round(hauteur,1))+" m")
	reset()

def setInCity():
	global hauteur, lastParam_hauteur
	hauteur = 202
	lastParam_hauteur = hauteur
	labelHauteur.configure(text=str(round(hauteur,1))+" m")
	reset()


def rebondSwitch(): # Activer/Désactiver le rebond
	global rebondBool, buttonRebond
	if rebondBool == True:
		rebondBool = False
		buttonRebond.configure(text="Activer rebond")
	elif rebondBool == False:
		rebondBool = True
		buttonRebond.configure(text="Désactiver rebond")

def explosion():  # Œuf de Pâques
	global y, fin, singularite, rayon, leftContainer, singularite, deletedForTrouNoir
	if deletedForTrouNoir == False:
		leftContainer.delete(ground)
		leftContainer.delete(item)
		deletedForTrouNoir = True
	if y < 300:
		y += 5
		fin.coords(singularite, 287, y-20, 307, y)
		root.after(10, explosion)
	if y >= 300:
		rayon += 10
		fin.coords(singularite, 287-rayon, y-20-rayon, 328+rayon, y+rayon)
		if rayon < 1000:
			root.after(10, explosion)
		if rayon >= 1000:
			root.quit()
			
def reset(): # Permet de tout réinitialiser
	global vitesse, hauteur, hauteur_pixel, y, t, coef_gravite, rebond
	hauteur = lastParam_hauteur
	coef_gravite = lastParam_gravite
	vitesse = 0
	rebond = 0
	t = 0
	hauteur_pixel = hauteur/500
	y = 40
	hauteur_impact = 0
	vitesse_impact = 0
	t_impact = 0
	leftContainer.coords(item, 90, y-20, 110, y)
	labelHauteur.configure(text=str(round(hauteur,1))+" m")
	labelVitesseMs.configure(text=str(round(vitesse+.01,1))+" m/s")
	labelVitesseKmh.configure(text=str(round(vitesse*3.6,1))+" km/h")
	labelTemps.configure(text=str(round(t+.01,1))+" s")
	stats.configure(text="Hauteur : "+str(round(hauteur_impact+.01,1))+" m\nVitesse d'impact : "+str(round(vitesse_impact+.01,1))+" m/s\nou "+str(round(3.6*vitesse_impact+.01,1))+" km/h\nMoment de l'impact : "+str(round(t_impact+.01,1))+" s")

def arreter():
	global hauteur, vitesse, y
	hauteur = 0
	vitesse = 0
	y = 542

def go():
	global hauteur, hauteur_pixel, trouNoir, fin, singularite, hauteur_impact, vitesse_impact, t_impact
	hauteur_impact = hauteur
	hauteur_pixel = hauteur/500
	if trouNoir == True:
		root.configure(background="black")
		leftContainer.grid_forget()
		rightContainer.grid_forget()
		secondRightContainer.grid_forget()
		thirdRightContainer.grid_forget()
		fin = Canvas(root, bg="black", highlightthickness=0, width=953, height=600)
		fin.pack()
		singularite = fin.create_oval(287, 20, 307, 40, fill="white")
		explosion()
	if hauteur != 0 and trouNoir == False:
		buttonGo.configure(command=arreter, text="Arrêter")
		fall()

def rebondir():
	global vitesse, hauteur, hauteur_pixel, y, t, coef_gravite, vitesse_pixel, rebond
	t += .01
	vitesse -= coef_gravite/50
	hauteur += vitesse/100
	vitesse_pixel = vitesse/hauteur_pixel
	y -= vitesse_pixel/100
	if vitesse > 0:
		root.after(10,rebondir)
	if vitesse <= 0:
		fall()
	leftContainer.coords(item, 90, y-20, 110, y)
	labelHauteur.configure(text=str(round(hauteur+.01,1))+" m")
	labelVitesseMs.configure(text=str(round(vitesse+.01,1))+" m/s")
	labelVitesseKmh.configure(text=str(round((vitesse+.01)*3.6,1))+" km/h")
	labelTemps.configure(text=str(round(t+.01,1))+" s")

def fall():
	global vitesse, hauteur, hauteur_pixel, y, t, coef_gravite, vitesse_pixel, rebond, hauteur_impact, vitesse_impact, t_impact, rebondBool
	t += .01
	vitesse += coef_gravite/100
	hauteur -= vitesse/100
	vitesse_pixel = vitesse/hauteur_pixel
	y += vitesse_pixel/100
	if hauteur > 0:
		root.after(10,fall)
	if hauteur <= 0:
		hauteur = 0
		if rebond < 10:
			if rebond < 1:
				vitesse_impact = vitesse
				t_impact = t
				if rebondBool == False:
					hauteur = 0
					vitesse = 0
					labelHauteur.configure(text=str(round(hauteur,1))+" m")
					labelVitesseMs.configure(text=str(round(vitesse+.01,1))+" m/s")
					labelVitesseKmh.configure(text=str(round(vitesse*3.6,1))+" km/h")
					buttonGo.configure(command=go, text="Lâcher")
				stats.configure(text="Hauteur : "+str(round(hauteur_impact+.01,1))+" m\nVitesse d'impact : "+str(round(vitesse_impact+.01,1))+" m/s\nou "+str(round(3.6*vitesse_impact+.01,1))+" km/h\nMoment de l'impact : "+str(round(t_impact+.01,1))+" s")
			rebond += 1
			if rebondBool == True:
				rebondir()
		if rebond >= 10:
			vitesse = 0
			hauteur = 0
			buttonGo.configure(command=go, text="Lâcher")
	if y > 542:
		y = 542
	leftContainer.coords(item, 90, y-20, 110, y)
	labelHauteur.configure(text=str(round(hauteur+.01,1))+" m")
	labelVitesseMs.configure(text=str(round(vitesse+.01,1))+" m/s")
	labelVitesseKmh.configure(text=str(round((vitesse+.01)*3.6,1))+" km/h")
	labelTemps.configure(text=str(round(t+.01,1))+" s")

root = Tk()
root.title("")

leftContainer = Canvas(root, width=200, height=600, bg="#99ccff", highlightthickness=0)
leftContainer.grid(column=3, row=1)
rightContainer = Canvas(root, width=300, height=600, highlightthickness=0)
rightContainer.grid(column=2, row=1)
secondRightContainer = Canvas(root, width=300, height=600, highlightthickness=0)
secondRightContainer.grid(column=4, row=1, sticky="N")
thirdRightContainer = Canvas(root, width=300, height=600, highlightthickness=0)
thirdRightContainer.grid(column=5, row=1, sticky="N")
entree_hauteur = StringVar()

labelParamHauteur = Label(thirdRightContainer, font=(("Arial"),36), width=14, text="Hauteur")
labelParamHauteur.pack(pady=(20,50))
buttonAvion = Button(thirdRightContainer, text="Airbus A380", command=setAvion, font=(("Arial"),14), width=10)
buttonAvion.pack()
buttonBurj = Button(thirdRightContainer, text="Burj Khalifa", command=setBurj, font=(("Arial"),14), width=10)
buttonBurj.pack()
buttonEiffel = Button(thirdRightContainer, text="Tour Eiffel", command=setEiffel, font=(("Arial"),14), width=10)
buttonEiffel.pack()
buttonInCity = Button(thirdRightContainer, text="Tour InCity", command=setInCity, font=(("Arial"),14), width=10)
buttonInCity.pack()
labelAutre = Label(thirdRightContainer, font=(("Arial"),18), width=10, text="Autre")
labelAutre.pack(pady=(20,0))
entryHauteur = Entry(thirdRightContainer, font=(("Arial"),36), width=5, justify=CENTER, textvariable=entree_hauteur)
entryHauteur.pack(pady=(0,10))
buttonSetHauteur = Button(thirdRightContainer, text="OK", command=setHauteur, font=(("Arial"),14))
buttonSetHauteur.pack(pady=(0,10))

labelParamLieu = Label(secondRightContainer, font=(("Arial"),36), width=14, text="Lieu")
labelParamLieu.pack(pady=(20,50))
buttonEarth = Button(secondRightContainer, text="Terre", command=setEarth, font=(("Arial"),14), width=10)
buttonEarth.pack()
buttonMoon = Button(secondRightContainer, text="Lune", command=setMoon, font=(("Arial"),14), width=10)
buttonMoon.pack()
buttonJupiter = Button(secondRightContainer, text="Jupiter", command=setJupiter, font=(("Arial"),14), width=10)
buttonJupiter.pack()
buttonMars = Button(secondRightContainer, text="Mars", command=setMars, font=(("Arial"),14), width=10)
buttonMars.pack()
buttonNeptune = Button(secondRightContainer, text="Neptune", command=setNeptune, font=(("Arial"),14), width=10)
buttonNeptune.pack()
buttonSun = Button(secondRightContainer, text="Soleil", command=setSun, font=(("Arial"),14), width=10)
buttonSun.pack()
buttonTatooine = Button(secondRightContainer, text="Tatooine", command=setTatooine, font=(("Arial"),14), width=10)
buttonTatooine.pack()
buttonSing = Button(secondRightContainer, text="Trou noir", command=setSing, font=(("Arial"),14), width=10)
buttonSing.pack()

labelIntro = Label(rightContainer, font=(("Arial"),18), width=16, text="Si vous étiez sur")
labelIntro.pack()
labelLieu = Label(rightContainer, font=(("Arial"),36), width=10, text="Terre")
labelLieu.pack(pady=(0,50))
labelHauteur = Label(rightContainer, font=(("Courier"),36), width=10, text=str(round(hauteur+.01,1))+" m")
labelHauteur.pack()
labelVitesseMs = Label(rightContainer, font=(("Courier"),36), width=10, text=str(round(vitesse+.01,1))+" m/s")
labelVitesseMs.pack()
labelVitesseKmh = Label(rightContainer, font=(("Courier"),36), width=10, text=str(round(vitesse+.01*3.6,1))+" km/h")
labelVitesseKmh.pack()
labelTemps = Label(rightContainer, font=(("Courier"),36), width=10, text=str(round(t+.01,1))+" s")
labelTemps.pack()

item = leftContainer.create_oval(90, 20, 110, 40, fill="white")
ground = leftContainer.create_line(0, 542, 200, 542, fill="white")

buttonGo = Button(rightContainer, text="Lâcher", command=go, font=(("Arial"),14))
buttonGo.pack(pady=(50,0))
buttonReset = Button(rightContainer, text="Réinitialiser", command=reset, font=(("Arial"),14))
buttonReset.pack()

credit = Label(thirdRightContainer, font=(("Arial"),14), text="Les forces autres que la pesanteur\nsont négligées.\nL'objet rebondit à une hauteur maximale\négale à la moitié de la hauteur maximale\ndu rebond précedent.\n\n\nCréé par\nMaxime Couette et Gabriel Stik")
credit.pack(padx=(20,20), pady=(35,0))

stats = Label(secondRightContainer, font=(("Arial"),16), text="Hauteur : "+str(round(hauteur_impact+.01,1))+" m\nVitesse d'impact : "+str(round(vitesse_impact+.01,1))+" m/s\nou "+str(round(3.6*vitesse_impact+.01,1))+" km/h\nMoment de l'impact : "+str(round(t_impact+.01,1))+" s")
stats.pack(padx=(20,20), pady=(75,0))

buttonRebond = Button(secondRightContainer, width=14, font=(("Arial"),14), text="Désactiver rebond", command=rebondSwitch)
buttonRebond.pack(pady=(50,0))

 # Configuration du style complémentaire

root.configure(bg="#181818")
leftContainer.configure(bg="#006699")
rightContainer.configure(bg="#181818")
secondRightContainer.configure(bg="#181818")
thirdRightContainer.configure(bg="#181818")
labelParamLieu.configure(bg="#181818", fg="white")
labelParamHauteur.configure(bg="#181818", fg="white")
labelHauteur.configure(bg="#181818", fg="white")
labelTemps.configure(bg="#181818", fg="white")
labelLieu.configure(bg="#181818", fg="white")
labelVitesseKmh.configure(bg="#181818", fg="white")
labelVitesseMs.configure(bg="#181818", fg="white")
labelIntro.configure(bg="#181818", fg="white")
labelAutre.configure(bg="#181818", fg="white")
credit.configure(bg="#181818", fg="white")
stats.configure(bg="#181818", fg="white")
buttonGo.configure(highlightbackground="#181818")
buttonRebond.configure(highlightbackground="#181818")
buttonReset.configure(highlightbackground="#181818")
buttonSing.configure(highlightbackground="#181818")
buttonTatooine.configure(highlightbackground="#181818")
buttonMars.configure(highlightbackground="#181818")
buttonNeptune.configure(highlightbackground="#181818")
buttonSun.configure(highlightbackground="#181818")
buttonJupiter.configure(highlightbackground="#181818")
buttonMoon.configure(highlightbackground="#181818")
buttonEarth.configure(highlightbackground="#181818")
buttonBurj.configure(highlightbackground="#181818")
buttonEiffel.configure(highlightbackground="#181818")
buttonInCity.configure(highlightbackground="#181818")
buttonAvion.configure(highlightbackground="#181818")
buttonSetHauteur.configure(highlightbackground="#181818")
entryHauteur.configure(highlightbackground="#181818")
root.mainloop()