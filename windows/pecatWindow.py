from tkinter import *
import Constants
import fileHelper as fh
from tkinter import filedialog
from algoritmi import pecat


def pecatWindow():

    Pecat = pecat.pecat()

    def chooseFile(var):

        chosen = filedialog.askopenfilename(initialdir=Constants.DOKUMENTI_PATH)

        if var == "ulaz":
            ulazPath.set(chosen)
            Pecat.ulaz_path = chosen
        elif var == "javniKljucPrimatelja":
            javniKljucPrimateljaPath.set(chosen)
            Pecat.rsa_b_javni_path = chosen
        elif var == "tajniKljucPosiljatelja":
            tajniKljucPosiljateljaPath.set(chosen)
            Pecat.rsa_a_tajni_path = chosen
        elif var == "omotnica":
            omotnicaPath.set(chosen)
            Pecat.omotnica_path = chosen
        elif var == "potpis":
            pecatPath.set(chosen)
            Pecat.potpis_path = chosen
        elif var == "javniKljucPosiljatelja":
            javniKljucPosiljateljaPath.set(chosen)
            Pecat.rsa_a_javni_path = chosen
        elif var == "tajniKljucPrimatelja":
            tajniKljucPrimateljaPath.set(chosen)
            Pecat.rsa_b_tajni_path = chosen
        elif var == "izlaz":
            izlazPath.set(chosen)
            Pecat.izlaz_path = chosen
        elif var == 'sazetak':
            sazetakPath.set(chosen)
            Pecat.sazetak = chosen

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
    javniKljucPrimateljaPath = StringVar()
    javniKljucPrimateljaEntry = Entry(window, textvariable=javniKljucPrimateljaPath, width=75).grid(row=2, column=2)
    javniKljucPrimateljaPath.set(Constants.RSA_B_JAVNI_PATH)
    Button(window, text=Constants.ODABERI, command=lambda : chooseFile("javniKljucPrimatelja")).grid(row=2, column=3)
    Button(window, text=Constants.PREGLEDAJ, command=lambda : fh.openWithNotepad(javniKljucPosiljateljaPath.get())).grid(row=2, column=4)

    # treci redak

    Label(window, text=Constants.TAJNI_KLJUC_PRIMATELJA).grid(row=3, column=1)
    tajniKljucPrimateljaPath = StringVar()
    tajniKljucPrimateljaEntry = Entry(window, textvariable=tajniKljucPrimateljaPath, width=75).grid(row=3, column=2)
    tajniKljucPrimateljaPath.set(Constants.RSA_B_TAJNI_PATH)
    Button(window, text=Constants.ODABERI, command=lambda: chooseFile("tajniKljucPrimatelja")).grid(row=3, column=3)
    Button(window, text=Constants.PREGLEDAJ, command=lambda: fh.openWithNotepad(tajniKljucPrimateljaPath.get())).grid(row=3, column=4)

    # cetvrti redak

    Label(window, text=Constants.JAVNI_KLJUC_POSILJATELJA).grid(row=4, column=1)
    javniKljucPosiljateljaPath = StringVar()
    javniKljucPosiljateljaEntry = Entry(window, textvariable=javniKljucPosiljateljaPath, width=75).grid(row=4, column=2)
    javniKljucPosiljateljaPath.set(Constants.RSA_A_JAVNI_PATH)
    Button(window, text=Constants.ODABERI, command=lambda: chooseFile("javniKljucPosiljatelja")).grid(row=4, column=3)
    Button(window, text=Constants.PREGLEDAJ, command=lambda: fh.openWithNotepad(javniKljucPosiljateljaPath.get())).grid(row=4, column=4)

    # peti redak

    Label(window, text=Constants.TAJNI_KLJUC_POSILJATELJA).grid(row=5, column=1)
    tajniKljucPosiljateljaPath = StringVar()
    tajniKljucPosiljateljaEntry = Entry(window, textvariable=tajniKljucPosiljateljaPath, width=75).grid(row=5, column=2)
    tajniKljucPosiljateljaPath.set(Constants.RSA_A_TAJNI_PATH)
    Button(window, text=Constants.ODABERI, command=lambda: chooseFile("tajniKljucPosiljatelja")).grid(row=5, column=3)
    Button(window, text=Constants.PREGLEDAJ, command=lambda: fh.openWithNotepad(tajniKljucPosiljateljaPath.get())).grid(row=5, column=4)

    # sesti redak

    Label(window, text=Constants.DIGITALNA_OMOTNICA).grid(row=6, column=1)
    omotnicaPath = StringVar()
    omotnicaEntry = Entry(window, textvariable=omotnicaPath, width=75).grid(row=6, column=2)
    omotnicaPath.set(Constants.OMOTNICA_PATH)
    Button(window, text=Constants.ODABERI, command=lambda: chooseFile("omotnica")).grid(row=6, column=3)
    Button(window, text=Constants.PREGLEDAJ, command=lambda: fh.openWithNotepad(omotnicaPath.get())).grid(row=6, column=4)

    # sedmi redak

    Label(window, text=Constants.DIGITALNI_POTPIS).grid(row=7, column=1)
    pecatPath = StringVar()
    pecatEntry = Entry(window, textvariable=pecatPath, width=75).grid(row=7, column=2)
    pecatPath.set(Constants.POTPIS_PATH)
    Button(window, text=Constants.ODABERI, command=lambda: chooseFile("potpis")).grid(row=7, column=3)
    Button(window, text=Constants.PREGLEDAJ, command=lambda: fh.openWithNotepad(pecatPath.get())).grid(row=7, column=4)

    # osmi redak

    Label(window, text=Constants.IZLAZNA_DATOTEKA).grid(row=8, column=1)
    izlazPath = StringVar()
    izlazEntry = Entry(window, textvariable=izlazPath, width=75).grid(row=8, column=2)
    izlazPath.set(Constants.IZLAZ_PATH)
    Button(window, text=Constants.ODABERI, command=lambda: chooseFile("izlaz")).grid(row=8, column=3)
    Button(window, text=Constants.PREGLEDAJ, command=lambda: fh.openWithNotepad(izlazPath.get())).grid(row=8, column=4)

    # peti redak

    Label(window, text=Constants.SAZETAK).grid(row=9, column=1)
    sazetakPath = StringVar()
    sazetakEntry = Entry(window, textvariable=sazetakPath, width=75).grid(row=9, column=2)
    sazetakPath.set(Constants.SAZETAK_PATH)
    Button(window, text=Constants.ODABERI, command=lambda: chooseFile("sazetak")).grid(row=9, column=3)
    Button(window, text=Constants.PREGLEDAJ, command=lambda: fh.openWithNotepad(sazetakPath.get())).grid(row=9,column=4)

    # sesti redak

    Button(window, text=Constants.GENERIRAJ_DIGITALNI_POTPIS, command=Pecat.generiraj_pecat, width=25).grid(row=10,column=2)
    Button(window, text=Constants.PROVJERI_DIGITALNI_POTPIS, command=Pecat.otvori_pecat, width=25).grid(row=10,column=3)

    # sedmi redak

    Button(window, text=Constants.GENERIRAJ_DIGITALNI_POTPIS + ' - MOJ SHA-1', command=Pecat.generiraj_moj_pecat,width=25).grid(row=11, column=2)
    Button(window, text=Constants.PROVJERI_DIGITALNI_POTPIS + '- MOJ SHA-1', command=Pecat.otvori_moj_pecat,width=25).grid(row=11, column=3)

    # osmi redak

    Label(window, text=Constants.VLASNIK).grid(row=12, column=4)