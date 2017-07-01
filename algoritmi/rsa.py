import Constants as cs
from Crypto import Random
from Crypto.PublicKey import RSA
import fileHelper as fh

class rsa:

    def __init__(self):
        self.rsa_javni = cs.RSA_JAVNI_PATH
        self.rsa_tajni = cs.RSA_TAJNI_PATH

    def generiraj_rsa(self, keySize):

        random_generator = Random.new().read
        kljuc = RSA.generate(keySize, random_generator)

        privatni_kljuc = str(kljuc.exportKey('DER').hex()).upper()
        javni_kljuc = str(kljuc.publickey().exportKey('DER').hex()).upper()

        keyLen = "0400"
        if keySize == 2048:
            keyLen = "0800"

        if keySize == 4096:
            keyLen = "1000"

        fh.writeRSA(self.rsa_javni, "Public key", "RSA", keyLen, javni_kljuc)
        fh.writeRSA(self.rsa_tajni, "Private key", "RSA", keyLen, privatni_kljuc)

