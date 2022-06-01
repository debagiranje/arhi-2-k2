"""
Isprogramirati rad grafičkog korisničkog interfejsa tako da se od korisnika zahtijeva unos neparnog broja n
(interfejs se pokazuje tek kada korisnik ispravno unese broj), a potom se na osnovu datog broja formira matrica
od nxn dugmadi. Brojevi na dugmadima rastu odozdo na gore u prvoj koloni, u drugoj odozgo na dolje, u trećoj opet na gore,
i tako dalje. Dugmadima sa neparnim brojevima treba pridružiti jedan isti događaj - prekid rada aplikacije.
Što se tiče ostalih dugmadi, po kliku treba da se broj na dugmetu smanji za jedan i da mu se promijeni događaj,
jer će neparni broj zamijeniti parni. 

"""
from tkinter import *

n=int(input("n= "))
while n%2==0:
    n=int(input("n= "))

okno=Tk()

list_button=[]

def promjena(i,lista):
    lista[i]["text"]=str(i+2)
    lista[i]["command"]=ugasi

def ugasi():
    okno.destroy()

for i in range(n):
    for j in range(n):
        if (n*i+j)%2==0:
            list_button.append(Button(okno, text=str(i*n+j+1),command=lambda x=i*n+j:promjena(x,list_button)))
        else:
            list_button.append(Button(okno, text=str(i*n+j+1),command=ugasi))
        if i%2==0:
            list_button[i*n+j].grid(row=j,column=i)
        else:
            list_button[i*n+j].grid(row=n-j-1,column=i)

okno.mainloop()