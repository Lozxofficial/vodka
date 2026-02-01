import json
from fileinput import close
from manim import *
import matplotlib
import numpy
import tkinter as tk

root = tk.Tk()
container = tk.Frame(root)
container.grid(row=0, column=1, sticky="nsew")

nav = tk.Frame(root, borderwidth=2, relief="sunken", padx=10, pady=10)
nav.grid(row=0, column=0, sticky="nw")

pages = {}

open("stats.json","w")
close()

def ui_initializer():
    root.title("Vodka")
    root.geometry("700x480")
    root.resizable(False, False)


    tk.Button(nav, text="Num encrypt", command=lambda: pages["numen"].tkraise()).grid(row=1, column=0, sticky="ew", pady=2)
    tk.Button(nav, text="Num decrypt", command=lambda: pages["info"].tkraise()).grid(row=2, column=0, sticky="ew", pady=2)
    tk.Button(nav, text='Quit', command=ui_quit).grid(row=3, column=0, sticky="ew", pady=2)

    #start
    Home = tk.Frame(container)
    frame = tk.Frame(Home)
    frame.grid()
    vodka2 = tk.Label(Home, text="Vodka", font=("Arial", 80, "bold"), foreground="#0893cf", relief="raised")
    vodka3 = tk.Label(Home, text="idk why i called it this", font=("Arial", 10, "bold"), foreground="#0893cf" , relief="sunken")
    vodka2.grid(row=0, column=0, padx=100, pady=1)
    vodka3.grid(row=1, column=0, padx=1, pady=1)

    pages["Home"] = Home
    #end

    #start
    numen = tk.Frame(container)
    frame = tk.Frame(numen)
    frame.pack()
    tk.Label(numen, text="Num Encrypt Page", font=("Segoe UI", 16, "bold")).pack(pady=20)

    tk.Label(numen, text="Username:").pack()
    stufftoencrypt = tk.StringVar()
    tk.Entry(numen, textvariable=stufftoencrypt).pack()
    password1 = tk.StringVar()
    tk.Entry(numen, textvariable=password1).pack()
    password2 = tk.StringVar()
    tk.Entry(numen, textvariable=password2).pack()

    def submit():
        ste = int(stufftoencrypt.get())
        p1 = int(password1.get())
        p2 = int(password2.get())
        print(ste + p1 * p2)

    tk.Button(numen, text="Login", command=submit).pack()
    pages["numen"] = numen
    #end

    info = tk.Frame(container)
    frame = tk.Frame(info)
    frame.pack()
    tk.Label(info, text="Num Encrypt Pagei", font=("Segoe UI", 16, "bold")).pack(pady=20)
    numen = tk.Frame(container)
    frame = tk.Frame(numen)
    frame.pack()
    tk.Label(numen, text="Num Encrypt Page", font=("Segoe UI", 16, "bold")).pack(pady=20)

    tk.Label(numen, text="Username:").pack()
    stufftoendcrypt = tk.StringVar()
    tk.Entry(numen, textvariable=stufftoendcrypt).pack()
    passwordd1 = tk.StringVar()
    tk.Entry(numen, textvariable=passwordd1).pack()
    passwordd2 = tk.StringVar()
    tk.Entry(numen, textvariable=passwordd2).pack()

    def submit():
        stdc = int(stufftoendcrypt.get())
        pd1 = int(password1.get())
        pd2 = int(password2.get())
        print(stdc - pd1 * pd2)

    tk.Button(numen, text="Login", command=submit).pack()
    pages["info"] = info

    for p in pages.values():
        p.grid(row=0, column=0, sticky="nsew")

    vodka = tk.Label(nav, text="Vodka", font=("Arial", 20, "bold"), foreground="#0893cf", relief="raised")
    vodka.grid(row=0, column=0, padx=10, pady=10)
    pages["Home"].tkraise()
def ui_start():
    root.mainloop()

def ui_quit():
    root.quit()

def num_encrypt():
    print()

ui_initializer()
ui_start()
