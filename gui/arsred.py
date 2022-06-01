"""
Направити програм који од корисника захтијева унос бројева све док се не унесе нула. Након што се унесу бројеви,
потребно је да се прикаже GUI на коме се налазе дугмади на којима пишу бројеви који су унијети са тастатуре.
Дугмади треба да буду приказана у матричном (квадратна матрица) облику. Матрица треба да буде најмањег формата
тако да сва дугмади на њу стану. Уколико остане празних мјеста у матрици, њих треба попунити дугмадима на којима пише “-1”.
Када се кликне на дугме, његова вриједност треба да се промјени у аритметичку средину бројева на дугмадима.

"""
import tkinter as tk
from functools import reduce



brojevi = []

while True:
    a = int(input("unesite br... (0 za prekid) "))
    if a == 0:
        break
    brojevi.append(a)


br = len(brojevi)

org = []
for l in brojevi:
    org.append(l)

i = 1
while True:
    if i**2 >= br:
        break
    i+=1
    
format = i 
    
br_e = i**2

while len(brojevi) != br_e:
    brojevi.append(-1)


suma = reduce(lambda x,y: x+y, org)
ars = round((suma / len(org)), 2)

def ar(i):
    dugmici[i]["text"] = f"{ars}"

dugmici = []

window = tk.Tk()
i = 0
for j in range(format):
    for k in range(format):
        dugmici.append(tk.Button(window, text=brojevi[i], command= lambda x = i: ar(x)))
        dugmici[i].grid(row=j, column=k)
        i+=1

window.mainloop()
