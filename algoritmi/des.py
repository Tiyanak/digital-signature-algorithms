import Constants as cs
import fileHelper as fh
import os
from Crypto.Cipher import DES
from Crypto import Random

class des:

    def __init__(self):
        self.des_kljuc_path = cs.DES_KLJUC_PATH
        self.des_ulaz_path = cs.DES_ULAZ_PATH
        self.des_izlaz_path = cs.DES_IZLAZ_PATH
        self.iv = Random.new().read(DES.block_size)

    def generiraj_des(self):

        key = os.urandom(8).hex().upper()

        fh.writeDESKey(self.des_kljuc_path, "Secret key", "DES", key)

    def kriptiraj_des(self):

        des_kljuc_items = fh.load(self.des_kljuc_path)
        des_key = str(fh.concatList(fh.get_items("Secret key", des_kljuc_items)))
        des_key = bytes.fromhex(des_key)

        ulaz_items = fh.load(self.des_ulaz_path)
        data = str(fh.concatList(fh.get_items("Data", ulaz_items)))

        if len(data) % 16 != 0:
            data += ' ' * (16 - len(data) % 16)

        self.iv = Random.new().read(DES.block_size)
        des_enkriptor = DES.new(des_key, DES.MODE_OFB, self.iv)
        kriptirano = str(des_enkriptor.encrypt(data).hex()).upper()

        fh.writeDES(self.des_izlaz_path, "DES kriptiranje", "DES", kriptirano)

    def dekriptiraj_des(self):

        des_kljuc_items = fh.load(self.des_kljuc_path)
        des_key = str(fh.concatList(fh.get_items("Secret key", des_kljuc_items)))
        des_key = bytes.fromhex(des_key)

        ulaz_items = fh.load(self.des_izlaz_path)
        data = str(fh.concatList(fh.get_items("Data", ulaz_items)))
        data = bytes.fromhex(data)

        dekripter = DES.new(des_key, DES.MODE_OFB, self.iv)
        dekriptirano = dekripter.decrypt(data)
        dekriptirano = dekriptirano.decode('utf-8', 'ignore')

        fh.writeDES(self.des_ulaz_path, "DES dekriptiranje", "DES", dekriptirano)