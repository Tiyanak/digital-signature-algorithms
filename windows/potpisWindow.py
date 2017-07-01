from tkinter import *
import Constants
import fileHelper as fh
from tkinter import filedialog
from algoritmi import potpis

def potpisWindow():

    Potpis = potpis.potpis()

    def chooseFile(var):

        chosen = filedialog.askopenfilename(initialdir=Constants.DOKUMENTI_PATH)

        if var == "ulaz":
            ulazPath.set(chosen)
            Potpis.ulaz_path = chosen
        elif var == "tajniKljuc":
            tajniKljucPath.set(chosen)
            Potpis.rsa_a_tajni_path = chosen
        elif var == "potpis":
            potpisPath.set(chosen)
            Potpis.potpis_path = chosen
        elif var == "javniKljuc":
            javniKljucPath.set(chosen)
            Potpis.rsa_a_javni_path = chosen
        elif var == "sazetak":
            sazetakPath.set(chosen)
            Potpis.sazetak_path = chosen

    window = Toplevel()

    # prvi redak

    Label(window, text=Constants.ULAZNA_DATOTEKA).grid(row=1, column=1)
    ulazPath = StringVar()
    ulazEntry = Entry(window, textvariable=ulazPath, width=75).grid(row=1, column=2)
    ulazPath.set(Constants.ULAZ_PATH)
    Button(window, text=Constants.ODABERI, command=lambda : chooseFile("ulaz")).grid(row=1, column=3)
    Button(window, text=Constants.PREGLEDAJ, command=lambda : fh.openWithNotepad(ulazPath.get())).grid(row=1, column=4)

    # drugi redak

    Label(window, text=Constants.TAJNI_KLJUC_POSILJATELJA).grid(row=2, column=1)
    tajniKljucPath = StringVar()
    tajniKljucEntry = Entry(window, textvariable=tajniKljucPath, width=75).grid(row=2, column=2)
    tajniKljucPath.set(Constants.RSA_A_TAJNI_PATH)
    Button(window, text=Constants.ODABERI,command=lambda : chooseFile("tajniKljuc")).grid(row=2, column=3)
    Button(window, text=Constants.PREGLEDAJ, command=lambda : fh.openWithNotepad(tajniKljucPath.get())).grid(row=2, column=4)

    # treci redak

    Label(window, text=Constants.JAVNI_KLJUC_POSILJATELJA).grid(row=3, column=1)
    javniKljucPath = StringVar()
    javniKljucEntry = Entry(window, textvariable=javniKljucPath, width=75).grid(row=3, column=2)
    javniKljucPath.set(Constants.RSA_A_JAVNI_PATH)
    Button(window, text=Constants.ODABERI, command=lambda: chooseFile("javniKljuc")).grid(row=3, column=3)
    Button(window, text=Constants.PREGLEDAJ, command=lambda: fh.openWithNotepad(javniKljucPath.get())).grid(row=3,column=4)

    # cetvrti redak

    Label(window, text=Constants.DIGITALNI_POTPIS).grid(row=4, column=1)
    potpisPath = StringVar()
    potpisEntry = Entry(window, textvariable=potpisPath, width=75).grid(row=4, column=2)
    potpisPath.set(Constants.POTPIS_PATH)
    Button(window, text=Constants.ODABERI, command=lambda: chooseFile("potpis")).grid(row=4, column=3)
    Button(window, text=Constants.PREGLEDAJ, command=lambda: fh.openWithNotepad(potpisPath.get())).grid(row=4, column=4)

    # peti redak

    Label(window, text=Constants.SAZETAK).grid(row=5, column=1)
    sazetakPath = StringVar()
    sazetakEntry = Entry(window, textvariable=sazetakPath, width=75).grid(row=5, column=2)
    sazetakPath.set(Constants.SAZETAK_PATH)
    Button(window, text=Constants.ODABERI, command=lambda: chooseFile("sazetak")).grid(row=5, column=3)
    Button(window, text=Constants.PREGLEDAJ, command=lambda: fh.openWithNotepad(sazetakPath.get())).grid(row=5,column=4)

    # sesti redak

    Button(window, text=Constants.GENERIRAJ_DIGITALNI_POTPIS, command=Potpis.generiraj_potpis, width=25).grid(row=6, column=2)
    Button(window, text=Constants.PROVJERI_DIGITALNI_POTPIS, command=Potpis.provjeri_potpis, width=25).grid(row=6, column=3)

    # sedmi redak

    Button(window, text=Constants.GENERIRAJ_DIGITALNI_POTPIS + ' - MOJ SHA-1', command=Potpis.generiraj_moj_potpis, width=25).grid(row=7,column=2)
    Button(window, text=Constants.PROVJERI_DIGITALNI_POTPIS + '- MOJ SHA-1', command=Potpis.provjeri_moj_potpis, width=25).grid(row=7,column=3)

    # osmi redak

    Label(window, text=Constants.VLASNIK).grid(row=8, column=4)

