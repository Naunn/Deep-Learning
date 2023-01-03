import tkinter as tk
from tkinter import ttk

import random

window = tk.Tk()
window.title('programik')

window.rowconfigure(0, weight=1, minsize=50)
window.rowconfigure(1, weight=1, minsize=50)
window.rowconfigure(2, weight=1, minsize=50)
window.rowconfigure(3, weight=1, minsize=50)
window.rowconfigure(4, weight=1, minsize=50)

window.columnconfigure(0, weight = 1, minsize = 200)
window.columnconfigure(1, weight = 1, minsize = 90)
window.columnconfigure(2, weight = 1, minsize = 90)

PlayerMoneyLabel = ttk.Label(text = 'Liczba monet gracza: ', master = window)
PlayerMoneyLabel.grid(row = 0, column = 0)

EnemyMoneyLabel = ttk.Label(text = 'Liczba monet przeciwnika: ', master = window).grid(row = 1, column = 0)

PoolMoneyLabel = ttk.Label(text = 'Obecna pula: ', master = window).grid(row = 2, column = 0)

SummaryLabel = ttk.Label(text = 'Podsumowanie: ', master = window).grid(row = 4, column = 0)

ttk.Label(text = 'Aktualna liczba: ', master = window).grid(row = 1, column = 2)

P_value = ttk.Label(text = 'None', master = window)
P_value.grid(row = 2, column = 2)

def increment():
    P_value.config(text = random.uniform(0, 1))

ttk.Button(master = window, text="Play", command=increment).grid(column=1, row=3)
ttk.Button(master = window, text="Pass", command=window.destroy).grid(column=2, row=3)

window.mainloop()