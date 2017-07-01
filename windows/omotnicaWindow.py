from tkinter import *
import Constants
import fileHelper as fh
from tkinter import filedialog
from algoritmi import omotnica

def omotnicaWindow():

    omotnica_instance = omotnica.Omotnica()

    def chooseFile(var):

        chosen = filedialog.askopenfilename(initialdir=Constants.DOKUMENTI_PATH)

        if var == "ulaz":
            ulazPath.set(chosen)
            omotnica_instance.ulaz_path = chosen
        elif var == "javniKljuc":
            javniKljucPath.set(chosen)
            omotnica_instance.rsa_b_javni = chosen
        elif var == "omotnica":
            omotnicaPath.set(chosen)
            omotnica_instance.omotnica_path = chosen
        elif var == "tajniKljuc":
            tajniKljucPath.set(chosen)
            omotnica_instance.rsa_b_tajni = chosen
        elif var == "izlaz":
            izlazPath.set(chosen)
            omotnica_instance.izlaz_path = chosen

    window = Toplevel()

    # prvi redak

    Label(window, text=Constants.ULAZNA_DATOTEKA).grid(row=1, column=1)
    ulazPath = StringVar()
    ulazEntry = Entry(window, textvariable=ulazPath, width=75).grid(row=1, column=2)
    ulazPath.set(Constants.ULAZ_PATH)
    Button(window, text=Constants.ODABERI, command=lambda : chooseFile("ulaz")).grid(row=1, column=3)
    Button(window, text=Constants.PREGLEDAJ, command=lambda : fh.openWithNotepad(ulazPath.get())).grid(row=1, column=4)

    # drugi redak

    Label(window, text=Constants.JAVNI_KLJUC_PRIMATELJA).grid(row=2, column=1)
    javniKljucPath = StringVar()
    javniKljucEntry = Entry(window, textvariable=javniKljucPath, width=75).grid(row=2, column=2)
    javniKljucPath.set(Constants.RSA_B_JAVNI_PATH)
    Button(window, text=Constants.ODABERI, command=lambda : chooseFile("javniKljuc")).grid(row=2, column=3)
    Button(window, text=Constants.PREGLEDAJ, command=lambda : fh.openWithNotepad(javniKljucPath.get())).grid(row=2, column=4)

    # treci redak

    Label(window, text=Constants.TAJNI_KLJUC_PRIMATELJA).grid(row=3, column=1)
    tajniKljucPath = StringVar()
    tajniKljucEntry = Entry(window, textvariable=tajniKljucPath, width=75).grid(row=3, column=2)
    tajniKljucPath.set(Constants.RSA_B_TAJNI_PATH)
    Button(window, text=Constants.ODABERI, command=lambda: chooseFile("tajniKljuc")).grid(row=3, column=3)
    Button(window, text=Constants.PREGLEDAJ, command=lambda: fh.openWithNotepad(tajniKljucPath.get())).grid(row=3, column=4)

    # cetvrti redak

    Label(window, text=Constants.DIGITALNA_OMOTNICA).grid(row=4, column=1)
    omotnicaPath = StringVar()
    omotnicaEntry = Entry(window, textvariable=omotnicaPath, width=75).grid(row=4, column=2)
    omotnicaPath.set(Constants.OMOTNICA_PATH)
    Button(window, text=Constants.ODABERI, command=lambda: chooseFile("omotnica")).grid(row=4, column=3)
    Button(window, text=Constants.PREGLEDAJ, command=lambda: fh.openWithNotepad(omotnicaPath.get())).grid(row=4, column=4)
    # peti redak

    Label(window, text=Constants.IZLAZNA_DATOTEKA).grid(row=5, column=1)
    izlazPath = StringVar()
    izlazEntry = Entry(window, textvariable=izlazPath, width=75).grid(row=5, column=2)
    izlazPath.set(Constants.IZLAZ_PATH)
    Button(window, text=Constants.ODABERI, command=lambda: chooseFile("izlaz")).grid(row=5, column=3)
    Button(window, text=Constants.PREGLEDAJ, command=lambda: fh.openWithNotepad(izlazPath.get())).grid(row=5, column=4)

    # sesti redak

    Button(window, text=Constants.GENERIRAJ_DIGITALNU_OMOTNICU, command=omotnica_instance.generiraj_omotnicu, width=25).grid(row=6, column=2)
    Button(window, text=Constants.OTVORI_DIGITALNU_OMOTNICU, command=omotnica_instance.otvori_omotnicu, width=25).grid(row=6, column=3)

    # osmi redak

    Label(window, text=Constants.VLASNIK).grid(row=7, column=4)