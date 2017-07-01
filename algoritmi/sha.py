import Constants as cs
import fileHelper as fh
import hashlib
from algoritmi import moj_sha1

class sha:

    def __init__(self):
        self.ulaz_path = cs.ULAZ_PATH
        self.sazetak_path = cs.SAZETAK_PATH

    def generiraj_sha1(self):

        ulaz_items = fh.load(self.ulaz_path)
        data = str(fh.concatList(fh.get_items("Data", ulaz_items)))

        data = data.encode('utf-8')

        sha1 = hashlib.sha1(data)
        sazetak = str(sha1.hexdigest()).upper()


        fh.writeSha1(self.sazetak_path, "Data hash", "SHA-1", sazetak)

    def generiraj_moj_sha1(self):

        ulaz_items = fh.load(self.ulaz_path)
        data = str(fh.concatList(fh.get_items("Data", ulaz_items)))

        data = fh.toHex(data)

        sha1 = moj_sha1.mojSha1(data)
        sazetak = str(sha1.digest()).upper()

        fh.writeSha1(self.sazetak_path, "Data hash", "MOJ SHA-1", sazetak)