from tkinter import *
import Constants
import fileHelper as fh
from tkinter import filedialog
from algoritmi import rsa

def rsaWindow():

    RSA = rsa.rsa()

    def chooseFile(var):

        chosen = filedialog.askopenfilename(initialdir=Constants.DOKUMENTI_PATH)

        if var == "kljucTajni":
            kljucTajniPath.set(chosen)
            RSA.rsa_tajni = chosen
        elif var == "kljucJavni":
            kljucJavniPath.set(chosen)
            RSA.rsa_javni = chosen

    window = Toplevel()

    # prvi red

    Label(window, text=Constants.TAJNI_KLJUC).grid(row=1, column=1)
    kljucTajniPath = StringVar()
    kljucTajniEntry = Entry(window, textvariable=kljucTajniPath, width=75).grid(row=1, column=2)
    kljucTajniPath.set(Constants.RSA_TAJNI_PATH)
    Button(window, text=Constants.ODABERI, command=lambda : chooseFile("kljucTajni")).grid(row=1, column=3)
    Button(window, text=Constants.PREGLEDAJ, command=lambda : fh.openWithNotepad(kljucTajniPath.get())).grid(row=1, column=4)

    # drugi red

    Label(window, text=Constants.JAVNI_KLJUC).grid(row=2, column=1)
    kljucJavniPath = StringVar()
    kljucJavniEntry = Entry(window, textvariable=kljucJavniPath, width=75).grid(row=2, column=2)
    kljucJavniPath.set(Constants.RSA_JAVNI_PATH)
    Button(window, text=Constants.ODABERI, command=lambda : chooseFile("kljucJavni")).grid(row=2, column=3)
    Button(window, text=Constants.PREGLEDAJ, command=lambda : fh.openWithNotepad(kljucJavniPath.get())).grid(row=2, column=4)

    # treci

    keySizeRSA = IntVar()
    Radiobutton(window, text=Constants.RSA_1024_T, value=Constants.RSA_1024,
                variable=keySizeRSA).grid(row=3, column=3)
    Radiobutton(window, text=Constants.RSA_2048_T, value=Constants.RSA_2048,
                variable=keySizeRSA).grid(row=3, column=4)
    Radiobutton(window, text=Constants.RSA_4096_T, value=Constants.RSA_4096,
                variable=keySizeRSA).grid(row=3, column=5)
    keySizeRSA.set(1024)

    # cetvrti

    Button(window, text=Constants.GENERIRAJ_KLJUCEVE, command=lambda : RSA.generiraj_rsa(keySizeRSA.get())).grid(row=4, column=2)

    # sesto
    Label(window, text=Constants.VLASNIK).grid(row=6, column=5)