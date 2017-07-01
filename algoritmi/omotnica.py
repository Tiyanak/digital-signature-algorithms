import Constants as cs
import fileHelper as fh
import os
from Crypto.Cipher import DES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random

class Omotnica:

    def __init__(self):
        self.ulaz_path = cs.ULAZ_PATH
        self.rsa_b_javni = cs.RSA_B_JAVNI_PATH
        self.rsa_b_tajni = cs.RSA_B_TAJNI_PATH
        self.izlaz_path = cs.IZLAZ_PATH
        self.omotnica_path = cs.OMOTNICA_PATH
        self.iv = Random.new().read(DES.block_size)

    def generiraj_omotnicu(self):

        ulaz_items = fh.load(self.ulaz_path)
        data = fh.concatList(fh.get_items('Data', ulaz_items))

        rsa_b_javni_items = fh.load(self.rsa_b_javni)
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

    def otvori_omotnicu(self):

        envelope_data_items = fh.load(self.omotnica_path)
        envelope_data = bytes.fromhex(fh.concatList(fh.get_items("Envelope data", envelope_data_items)))

        envelope_crypt_key = fh.concatList(fh.get_items("Envelope crypt key", envelope_data_items))
        envelope_crypt_key = bytes.fromhex(envelope_crypt_key)

        rsa_b_tajni_items = fh.load(self.rsa_b_tajni)
        rsa_b_tajni_key = fh.concatList(fh.get_items("Secret key", rsa_b_tajni_items))
        rsa_b_tajni_key = bytes.fromhex(rsa_b_tajni_key)

        RSAkey = RSA.importKey(rsa_b_tajni_key)
        cipher = PKCS1_OAEP.new(RSAkey)
        desKey = cipher.decrypt(envelope_crypt_key)

        DESdekripter = DES.new(desKey, DES.MODE_OFB, self.iv)
        data = DESdekripter.decrypt(envelope_data)
        data = data.decode('utf-8', 'ignore')

        fh.writeIzlaz(self.izlaz_path, "Dekriptirana omotnica", "DES\n\tRSA", data)



