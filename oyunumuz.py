import tkinter as tk
from tkinter import *

pencere = tk.Tk()

pencere.geometry("400x400")
pencere.configure(background="#4d8dc6")
def tas():
    import random
    makine=random.randint(1,3)
    if makine==1:
        print("BERABERE")
    elif makine==2:
        print("KAYBETTİN")
    else:
        print("KAZANDIN")

def kagıt():
    import random
    makine=random.randint(1,3)
    if makine==2:
        print("BERABERE")
    elif makine==3:
        print("KAYBETTİN")
    else:
        print("KAZANDIN")

def makas():
    import random
    makine=random.randint(1,3)
    if makine==3:
        print("BERABERE")
    elif makine==1:
        print("KAYBETTİN")
    else:
        print("KAZANDIN")

etiket = tk.Label(text='******  TAŞ-KAĞIT-MAKAS  ******\n\nTARAFINI SEÇ',width=40,height=5)
etiket.pack()

düğme1 = tk.Button(text='TAŞ', command=tas,fg="red",width=18,height=10)
düğme1.pack(side=LEFT)
düğme2 = tk.Button(text='KAĞIT', command=kagıt,fg="blue",width=18,height=10)
düğme2.pack(side=LEFT)
düğme3 = tk.Button(text='MAKAS', command=makas,fg="green",width=18,height=10)
düğme3.pack(side=LEFT)

pencere.mainloop()

