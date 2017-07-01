import Constants as cs
import fileHelper as fh
import os
from Crypto.Cipher import DES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random
import hashlib
from algoritmi import moj_sha1

class pecat:

    def __init__(self):
        self.ulaz_path = cs.ULAZ_PATH
        self.rsa_a_javni_path = cs.RSA_A_JAVNI_PATH
        self.rsa_b_tajni_path = cs.RSA_B_TAJNI_PATH
        self.omotnica_path = cs.OMOTNICA_PATH
        self.pecat_path = cs.PECAT_PATH
        self.rsa_b_javni_path = cs.RSA_B_JAVNI_PATH
        self.rsa_a_tajni_path = cs.RSA_A_TAJNI_PATH
        self.izlaz_path = cs.IZLAZ_PATH
        self.potpis_path = cs.POTPIS_PATH
        self.iv = Random.new().read(DES.block_size)
        self.sazetak_path = cs.SAZETAK_PATH

    def generiraj_pecat(self):

        ulaz_items = fh.load(self.ulaz_path)
        data = fh.concatList(fh.get_items('Data', ulaz_items))

        rsa_b_javni_items = fh.load(self.rsa_b_javni_path)
        rsa_b_javni_kljuc = bytes.fromhex(fh.concatList(fh.get_items('Secret key', rsa_b_javni_items)))

        if len(data) % 16 != 0:
            data += ' ' * (16 - len(data) % 16)

        desKey = os.urandom(8)

        self.iv = Random.new().read(DES.block_size)
        des_enkriptor = DES.new(desKey, DES.MODE_OFB, self.iv)
        kriptirano = str(des_enkriptor.encrypt(data).hex()).upper()

        RSAenkripter = RSA.importKey(rsa_b_javni_kljuc)
        enkripter = PKCS1_OAEP.new(RSAenkripter)
        desKeyKriptirano = enkripter.encrypt(desKey).hex().upper()

        keylen = len(fh.get_items("Secret key", rsa_b_javni_items))
        if keylen == 10:
            keylen = '0800'
        elif keylen == 19:
            keylen = '1000'
        else:
            keylen = '0400'

        fh.writeOmotnica(self.omotnica_path, 'Envelope', 'DES\n\tRSA', '0010\n\t' + keylen, kriptirano, desKeyKriptirano)

        rsa_a_tajni_items = fh.load(self.rsa_a_tajni_path)

        kriptirano = kriptirano.encode()
        sha1 = hashlib.sha1(kriptirano)
        sazetak = str(sha1.hexdigest()).upper()

        fh.writeSha1(self.sazetak_path, "Data hash", "SHA-1", sazetak)

        sazetak = bytes.fromhex(sazetak)

        rsa_a_tajni_kljuc = bytes.fromhex(fh.concatList(fh.get_items("Secret key", rsa_a_tajni_items)))

        RSAenkripter = RSA.importKey(rsa_a_tajni_kljuc)
        potpis = str(RSAenkripter.sign(sazetak, '')[0])

        fh.writePotpis(self.potpis_path, "Signature", "SHA-1\n\tRSA", "0080", potpis)

    def otvori_pecat(self):

        omotnica_items = fh.load(self.omotnica_path)
        rsa_a_javni_items = fh.load(self.rsa_a_javni_path)
        potpis_items = fh.load(self.potpis_path)

        data = fh.concatList(fh.get_items("Envelope data", omotnica_items))

        rsa_a_javni_kljuc = bytes.fromhex(fh.concatList(fh.get_items("Secret key", rsa_a_javni_items)))
        potpis = str(fh.concatList(fh.get_items("Signature", potpis_items)))

        data = data.encode()
        sha1 = hashlib.sha1(data)
        sazetak = bytes.fromhex(str(sha1.hexdigest()).upper())

        RSAenkriptor = RSA.importKey(rsa_a_javni_kljuc)

        if RSAenkriptor.verify(sazetak, (int(potpis), '')):
            print("PORUKA JE AUTENTICNA")
        else:
            print("PORUKA NIJE AUTENTICNA")

        envelope_data_items = fh.load(self.omotnica_path)
        envelope_data = bytes.fromhex(fh.concatList(fh.get_items("Envelope data", envelope_data_items)))

        envelope_crypt_key = fh.concatList(fh.get_items("Envelope crypt key", envelope_data_items))
        envelope_crypt_key = bytes.fromhex(envelope_crypt_key)

        rsa_b_tajni_items = fh.load(self.rsa_b_tajni_path)
        rsa_b_tajni_key = fh.concatList(fh.get_items("Secret key", rsa_b_tajni_items))
        rsa_b_tajni_key = bytes.fromhex(rsa_b_tajni_key)

        RSAkey = RSA.importKey(rsa_b_tajni_key)
        cipher = PKCS1_OAEP.new(RSAkey)
        desKey = cipher.decrypt(envelope_crypt_key)

        DESdekripter = DES.new(desKey, DES.MODE_OFB, self.iv)
        data = DESdekripter.decrypt(envelope_data)
        data = data.decode('utf-8', 'ignore')

        fh.writeIzlaz(self.izlaz_path, "Dekriptirana omotnica", "DES\n\tRSA", data)

    def generiraj_moj_pecat(self):

        ulaz_items = fh.load(self.ulaz_path)
        data = fh.concatList(fh.get_items('Data', ulaz_items))

        rsa_b_javni_items = fh.load(self.rsa_b_javni_path)
        rsa_b_javni_kljuc = bytes.fromhex(fh.concatList(fh.get_items('Secret key', rsa_b_javni_items)))

        if len(data) % 16 != 0:
            data += ' ' * (16 - len(data) % 16)

        desKey = os.urandom(8)

        self.iv = Random.new().read(DES.block_size)
        des_enkriptor = DES.new(desKey, DES.MODE_OFB, self.iv)
        kriptirano = str(des_enkriptor.encrypt(data).hex()).upper()

        RSAenkripter = RSA.importKey(rsa_b_javni_kljuc)
        enkripter = PKCS1_OAEP.new(RSAenkripter)
        desKeyKriptirano = enkripter.encrypt(desKey).hex().upper()

        keylen = len(fh.get_items("Secret key", rsa_b_javni_items))
        if keylen == 10:
            keylen = '0800'
        elif keylen == 19:
            keylen = '1000'
        else:
            keylen = '0400'

        fh.writeOmotnica(self.omotnica_path, 'Envelope', 'DES\n\tRSA', '0010\n\t' + keylen, kriptirano, desKeyKriptirano)

        rsa_a_tajni_items = fh.load(self.rsa_a_tajni_path)

        kriptirano = fh.toHex(kriptirano)
        sha1 = moj_sha1.mojSha1(kriptirano)
        sazetak = str(sha1.digest()).upper()

        fh.writeSha1(self.sazetak_path, "Data hash", "MOJ SHA-1", sazetak)

        sazetak = bytes.fromhex(sazetak)

        rsa_a_tajni_kljuc = bytes.fromhex(fh.concatList(fh.get_items("Secret key", rsa_a_tajni_items)))

        RSAenkripter = RSA.importKey(rsa_a_tajni_kljuc)
        potpis = str(RSAenkripter.sign(sazetak, '')[0])

        fh.writePotpis(self.potpis_path, "Signature", "SHA-1\n\tRSA", "0080", potpis)

    def otvori_moj_pecat(self):

        omotnica_items = fh.load(self.omotnica_path)
        rsa_a_javni_items = fh.load(self.rsa_a_javni_path)
        potpis_items = fh.load(self.potpis_path)

        data = fh.concatList(fh.get_items("Envelope data", omotnica_items))
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

        envelope_data_items = fh.load(self.omotnica_path)
        envelope_data = bytes.fromhex(fh.concatList(fh.get_items("Envelope data", envelope_data_items)))

        envelope_crypt_key = fh.concatList(fh.get_items("Envelope crypt key", envelope_data_items))
        envelope_crypt_key = bytes.fromhex(envelope_crypt_key)

        rsa_b_tajni_items = fh.load(self.rsa_b_tajni_path)
        rsa_b_tajni_key = fh.concatList(fh.get_items("Secret key", rsa_b_tajni_items))
        rsa_b_tajni_key = bytes.fromhex(rsa_b_tajni_key)

        RSAkey = RSA.importKey(rsa_b_tajni_key)
        cipher = PKCS1_OAEP.new(RSAkey)
        desKey = cipher.decrypt(envelope_crypt_key)

        DESdekripter = DES.new(desKey, DES.MODE_OFB, self.iv)
        data = DESdekripter.decrypt(envelope_data)
        data = data.decode('utf-8', 'ignore')

        fh.writeIzlaz(self.izlaz_path, "Dekriptirana omotnica", "DES\n\tRSA", data)