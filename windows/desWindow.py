from tkinter import *
import Constants
import fileHelper as fh
from tkinter import filedialog
from algoritmi import des

def desWindow():

    DES = des.des()

    def chooseFile(var):

        chosen = filedialog.askopenfilename(initialdir=Constants.DOKUMENTI_PATH)

        if var == "kljuc":
            kljucPath.set(chosen)
            DES.des_kljuc_path = chosen
        elif var == "ulazDes":
            ulazAesPath.set(chosen)
            DES.des_ulaz_path = chosen
        elif var == "izlazDes":
            izlazAesPath.set(chosen)
            DES.des_izlaz_path = chosen

    window = Toplevel()

    blokSize = IntVar()
    blokSize.set(Constants.BLOK_128)

    # prvi redak

    Label(window, text=Constants.KLJUC).grid(row=1, column=1)
    kljucPath = StringVar()
    kljucEntry = Entry(window, textvariable=kljucPath, width=75).grid(row=1, column=2)
    kljucPath.set(Constants.DES_KLJUC_PATH)
    Button(window, text=Constants.ODABERI, command=lambda : chooseFile("kljuc")).grid(row=1, column=3)
    Button(window, text=Constants.PREGLEDAJ, command=lambda : fh.openWithNotepad(kljucPath.get())).grid(row=1, column=4)
    Button(window, text=Constants.GENERIRAJ, command=lambda : DES.generiraj_des()).grid(row=1, column=5)

    # drugi redak

    Label(window, text=Constants.ULAZNA_DATOTEKA).grid(row=2, column=1)
    ulazAesPath = StringVar()
    ulazAesEntry = Entry(window, textvariable=ulazAesPath, width=75).grid(row=2, column=2)
    ulazAesPath.set(Constants.DES_ULAZ_PATH)
    Button(window, text=Constants.ODABERI, command=lambda : chooseFile("ulazDes")).grid(row=2, column=3)
    Button(window, text=Constants.PREGLEDAJ, command=lambda : fh.openWithNotepad(ulazAesPath.get())).grid(row=2, column=4)

    # treci redak

    Label(window, text=Constants.IZLAZNA_DATOTEKA).grid(row=3, column=1)
    izlazAesPath = StringVar()
    izlazAesEntry = Entry(window, textvariable=izlazAesPath, width=75).grid(row=3, column=2)
    izlazAesPath.set(Constants.DES_IZLAZ_PATH)
    Button(window, text=Constants.ODABERI, command=lambda : chooseFile("izlazDes")).grid(row=3, column=3)
    Button(window, text=Constants.PREGLEDAJ, command=lambda : fh.openWithNotepad(izlazAesPath.get())).grid(row=3, column=4)

    # peti redak

    Button(window, text=Constants.KRIPTIRAJ, command=lambda: DES.kriptiraj_des()).grid(row=5, column=2)
    Button(window, text=Constants.DEKRIPTIRAJ, command=lambda : DES.dekriptiraj_des()).grid(row=5, column=3)

    # sesti redak

    Label(window, text=Constants.VLASNIK).grid(row=6, column=5)