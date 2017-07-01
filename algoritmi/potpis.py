import Constants as cs
import fileHelper as fh
import hashlib
from Crypto.PublicKey import RSA
from base64 import b64encode
from Crypto.Cipher import PKCS1_OAEP
from algoritmi import moj_sha1

class potpis:

    def __init__(self):
        self.ulaz_path = cs.ULAZ_PATH
        self.rsa_a_tajni_path = cs.RSA_A_TAJNI_PATH
        self.potpis_path = cs.POTPIS_PATH
        self.rsa_a_javni_path = cs.RSA_A_JAVNI_PATH
        self.sazetak_path = cs.SAZETAK_PATH

    def generiraj_potpis(self):

        ulaz_items = fh.load(self.ulaz_path)
        rsa_a_tajni_items = fh.load(self.rsa_a_tajni_path)

        data = fh.concatList(fh.get_items("Data", ulaz_items))

        data = data.encode()

        sha1 = hashlib.sha1(data)
        sazetak = str(sha1.hexdigest()).upper()

        fh.writeSha1(self.sazetak_path, "Data hash", "SHA-1", sazetak)

        sazetak = bytes.fromhex(sazetak)

        rsa_a_tajni_kljuc = bytes.fromhex(fh.concatList(fh.get_items("Secret key", rsa_a_tajni_items)))

        RSAenkripter = RSA.importKey(rsa_a_tajni_kljuc)
        potpis = str(RSAenkripter.sign(sazetak, '')[0])

        fh.writePotpis(self.potpis_path, "Signature", "SHA-1\n\tRSA", "0080", potpis)

    def provjeri_potpis(self):

        ulaz_items = fh.load(self.ulaz_path)
        rsa_a_javni_items = fh.load(self.rsa_a_javni_path)
        potpis_items = fh.load(self.potpis_path)

        data = fh.concatList(fh.get_items("Data", ulaz_items))

        data = data.encode()

        rsa_a_javni_kljuc = bytes.fromhex(fh.concatList(fh.get_items("Secret key", rsa_a_javni_items)))
        potpis = str(fh.concatList(fh.get_items("Signature", potpis_items)))

        sha1 = hashlib.sha1(data)
        sazetak = bytes.fromhex(str(sha1.hexdigest()).upper())

        RSAenkriptor = RSA.importKey(rsa_a_javni_kljuc)

        if RSAenkriptor.verify(sazetak, (int(potpis), '')):
            print("PORUKA JE AUTENTICNA")
        else:
            print("PORUKA NIJE AUTENTICNA")

    def generiraj_moj_potpis(self):

        ulaz_items = fh.load(self.ulaz_path)
        rsa_a_tajni_items = fh.load(self.rsa_a_tajni_path)

        data = fh.concatList(fh.get_items("Data", ulaz_items))
        data = fh.toHex(data)

        sha1 = moj_sha1.mojSha1(data)
        sazetak = str(sha1.digest()).upper()

        fh.writeSha1(self.sazetak_path, "Data hash", "MOJ SHA-1", sazetak)

        sazetak = bytes.fromhex(sazetak)

        rsa_a_tajni_kljuc = bytes.fromhex(fh.concatList(fh.get_items("Secret key", rsa_a_tajni_items)))

        RSAenkripter = RSA.importKey(rsa_a_tajni_kljuc)
        potpis = str(RSAenkripter.sign(sazetak, '')[0])

        fh.writePotpis(self.potpis_path, "Signature", "MOJ SHA-1\n\tRSA", "0080", potpis)

    def provjeri_moj_potpis(self):

        ulaz_items = fh.load(self.ulaz_path)
        rsa_a_javni_items = fh.load(self.rsa_a_javni_path)
        potpis_items = fh.load(self.potpis_path)

        data = fh.concatList(fh.get_items("Data", ulaz_items))
        data = fh.toHex(data)

        rsa_a_javni_kljuc = bytes.fromhex(fh.concatList(fh.get_items("Secret key", rsa_a_javni_items)))
        potpis = str(fh.concatList(fh.get_items("Signature", potpis_items)))

        sha1 = moj_sha1.mojSha1(data)
        sazetak = bytes.fromhex(str(sha1.digest()).upper())

        RSAenkriptor = RSA.importKey(rsa_a_javni_kljuc)

        if RSAenkriptor.verify(sazetak, (int(potpis), '')):
            print("PORUKA JE AUTENTICNA")
        else:
            print("PORUKA NIJE AUTENTICNA")


