"""
Направити GUI који реализује чување бројева телефона у датотеку test.txt. На GUI-у треба да су приказани бројеви
0,1,2,3,4,5,6,7,8,9 на које може да се кликне и приликом клика на неки број, тај број треба да се прикаже на Text елементу.
Поред Text елемента треба да постоји и Button елемент на који кад се кликне, сачува се број из Text у датотеку test.txt. 

"""

#popravi grid bro

import tkinter as tk

window = tk.Tk()

brojici = []

m = 0

tekst = tk.Text(window, width=20,height=2)
tekst.grid(row = m, column=0)

def sejv():
    with open("test.txt", "w") as f:
        f.write(tekst.get("1.0", tk.END))

sd = tk.Button(window, text="sacuvaj", command=sejv)
sd.grid(row = m, column=1)


def salji(i):
    tekst.insert(tk.INSERT, i)


brojici.append(tk.Button(window, text=0,  height=2, width=4, command= lambda x = 0: salji(x) ))


k = 1
for i in range(2,5):
    for j in range(2,5):
        brojici.append(tk.Button(window, text=k, height=2, width=4, command=lambda x = k: salji(x)))
        brojici[k].grid(column = j, row = i)
        k+=1

brojici[0].grid(row = i+1, column=0, columnspan=3)

window.mainloop()