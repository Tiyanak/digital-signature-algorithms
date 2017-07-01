from tkinter import *
import Constants
import fileHelper as fh
from tkinter import filedialog
from algoritmi import sha

def shaWindow():

    sha1 = sha.sha()

    def chooseFile(var):

        chosen = filedialog.askopenfilename(initialdir=Constants.DOKUMENTI_PATH)

        if var == "ulaz":
            ulazPath.set(chosen)
            sha1.ulazPath = chosen
        elif var == "sazetak":
            sazetakPath.set(chosen)
            sha1.sazetak_path = chosen

    window = Toplevel()

    # prvi red

    Label(window, text=Constants.ULAZNA_DATOTEKA).grid(row=1, column=1)
    ulazPath = StringVar()
    ulazEntry = Entry(window, textvariable=ulazPath, width=75).grid(row=1, column=2)
    ulazPath.set(Constants.ULAZ_PATH)
    Button(window, text=Constants.ODABERI, command=lambda : chooseFile("ulaz")).grid(row=1, column=3)
    Button(window, text=Constants.PREGLEDAJ, command=lambda : fh.openWithNotepad(ulazPath.get())).grid(row=1, column=4)

    # drugi red

    Label(window, text=Constants.SAZETAK).grid(row=2, column=1)
    sazetakPath = StringVar()
    sazetakEntry = Entry(window, textvariable=sazetakPath, width=75).grid(row=2, column=2)
    sazetakPath.set(Constants.SAZETAK_PATH)
    Button(window, text=Constants.ODABERI, command=lambda : chooseFile("sazetak")).grid(row=2, column=3)
    Button(window, text=Constants.PREGLEDAJ, command=lambda : fh.openWithNotepad(sazetakPath.get())).grid(row=2, column=4)

    # treci

    Button(window, text=Constants.GENERIRAJ_SAZETAK, command=sha1.generiraj_sha1).grid(row=3, column=2)
    Button(window, text=Constants.GENERIRAJ_SAZETAK + ' - MOJ SHA-1', command=sha1.generiraj_moj_sha1).grid(row=3, column=3)


    # peti
    Label(window, text=Constants.VLASNIK).grid(row=4, column=4)