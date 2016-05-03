#!/usr/bin/python2.7
#-*- coding: utf-8 -*-


from Tkinter import *
from PIL import Image, ImageTk
import tkFont, time, threading


def affichetemps():
    global L
    while True:
        date = time.strftime('%d/%m/%y',time.localtime())
        temps = time.strftime('%H:%M:%S',time.localtime())
        L.config(text=date)
        Te.config(text=temps)
        time.sleep(0.01) 


class Boutons :


	def __init__(self, master):

		self.Button_ON = Button(root,image=photo_ON, borderwidth=0, command=self.arret)
		self.Button_ON.grid(row=0, column=0, rowspan=2, sticky=N+W, padx=10, pady=10)

		self.blanco = Label(root, text="")
		self.blanco.grid(row=0,column=1, padx=50)
		self.tempe1 = Label(root, text="Temperature ", font=police, anchor=E)
		self.tempe1.grid(row=0, column=2, padx=20, sticky=S+E)
		self.tempe2 = Label(root, text="actuelle :", font=police, anchor=E)
		self.tempe2.grid(row=1, column=2,padx=20, sticky=N+E)
		self.tempe3 = Label(root, text="26°C", font=policeTempe)
		self.tempe3.grid(row=0, column=3,rowspan=2, sticky=W+E+N+S)
		self.blanco2 = Label(root, text="")
		self.blanco2.grid(row=0,column=4, padx=65)

		self.reglages = Button(root, text="Reglages", anchor=W, font=policeBouton, width=12)
		self.reglages.grid(row=4, column=5, padx=0, sticky=E)
		self.Luminosite = Button(root, text="Luminosite", anchor=W, font=policeBouton, width=12)
		self.Luminosite.grid(row=3, column=5, padx=0, sticky=E)
		self.Temperature = Button(root, text="Temperature", anchor=W, font=policeBouton, width=12)
		self.Temperature.grid(row=2, column=5, padx=0, sticky=E)

	def marche(self):
		self.Button_ON = Button(root,image=photo_ON, borderwidth=0, command=self.arret)
		self.Button_ON.grid(row=0, column=0, rowspan=2, sticky=N+W, padx=10, pady=10)		

	def arret(self):
		self.Button_OFF = Button(root,image=photo_OFF, borderwidth=0, command=self.marche)
		self.Button_OFF.grid(row=0, column=0, rowspan=2, sticky=N+W, padx=10, pady=10)




root = Tk()
root.grid_bbox(0,0,1,1)
root.geometry("800x480+0+0")
root.resizable(width=False,height=False)
police=tkFont.Font(root, size=16, family='Courier')
policeBouton=tkFont.Font(root, size=14, family='Courier')
policeTempe=tkFont.Font(root, size=26, family='Courier')


ON = Image.open("img/ON.png")
photo_ON = ImageTk.PhotoImage(ON)
OFF = Image.open("img/OFF.png")
photo_OFF = ImageTk.PhotoImage(OFF)

lol = Boutons(root)

L = Label(root, text = "", font=police)
Te = Label(root, text = "", font=police)
L.grid(row=0, column=5, sticky=S+E, padx=0)
Te.grid(row=1, column=5, sticky=N+E, padx=0)
T=threading.Thread(target=affichetemps)
T.setDaemon(True)
T.start()


root.mainloop()
