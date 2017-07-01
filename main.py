from tkinter import *
from windows import desWindow, omotnicaWindow, potpisWindow, pecatWindow, rsaWindow, shaWindow

def main():

    mainWindow = Tk()

    Button(mainWindow, text='Omotnica', command=omotnicaWindow.omotnicaWindow, width=15).grid(row=1, column=1)
    Button(mainWindow, text='Potpis', command=potpisWindow.potpisWindow, width=15).grid(row=1, column=2)
    Button(mainWindow, text='Pecat', command=pecatWindow.pecatWindow, width=15).grid(row=1, column=3)

    Button(mainWindow, text='DES', command=desWindow.desWindow, width=15).grid(row=2, column=1)
    Button(mainWindow, text='RSA', command=rsaWindow.rsaWindow, width=15).grid(row=2, column=2)
    Button(mainWindow, text='SHA-1', command=shaWindow.shaWindow, width=15).grid(row=2, column=3)

    mainWindow.mainloop()

main()