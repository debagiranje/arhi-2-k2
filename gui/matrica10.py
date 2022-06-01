"""
Isprogramirati rad grafičkog korisničkog interfejsa tako da se prvo od prvog argumenta programa uzme cio broj “n”, 
a potom napravi matrica chechbutton-a formata nxn. Nakon toga kreirati i matricu label-a ispod matrice checkbutton-a
iste dimnezije (nxn), gdje je text od label-a jednak “0”. U programu realizovati sljedeće: kada se checkbutton označi(deoznači)
na poziciji “i”,”j”, tada se label-a na poziciji “i”,”j” postavi na “1”(“0”).

"""

import tkinter as tk

n = int(input("unesite n... "))

checkie = []
labelie = []

k = 0
l = 0

window = tk.Tk()


var = []

def stanje(i):
    if var[i].get() == 1:
        labelie[i]["text"] = "1"
    elif var[i].get() == 0:
        labelie[i]["text"] = "0"



for i in range(n):
    for j in range(n):
        var.append(tk.IntVar())
        checkie.append(tk.Checkbutton(window, variable = var[k], onvalue=1, offvalue=0, command= lambda x = k: stanje(x)) )
        checkie[k].grid(row = i, column = j)
        k+=1

for i in range(n+2, n+n+2):
    for j in range(n):
        labelie.append(tk.Label(window, text="0") )
        labelie[l].grid(row = i, column = j)
        l+=1

window.mainloop()