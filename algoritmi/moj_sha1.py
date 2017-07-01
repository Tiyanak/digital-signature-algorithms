class mojSha1:

    def __init__(self, data):
        self.data = str(data).upper()
        self.M = self.init_blocks()

    def hexAND(self, A, B):

        rez = int(A, 16) & int(B, 16)
        rez = str(hex(rez)).replace('0x', '').upper()

        dopuna_nula = 8 - len(rez)
        temp = '0' * dopuna_nula
        rez = '' + temp + rez

        return rez

    def hexOR(self, A, B):

        rez = int(A, 16) | int(B, 16)
        rez = str(hex(rez)).replace('0x', '').upper()

        dopuna_nula = 8 - len(rez)
        temp = '0' * dopuna_nula
        rez = '' + temp + rez

        return rez

    def hexXOR(self, A, B):

        rez = int(A, 16) ^ int(B, 16)
        rez = str(hex(rez)).replace('0x', '').upper()

        dopuna_nula = 8 - len(rez)
        temp = '0' * dopuna_nula
        rez = '' + temp + rez

        return rez

    def hexNOT(self, A):

        B = self.hexToBin(A)
        rez = ''
        for c in B:
            if c == '0':
                rez += '1';
            else:
                rez += '0'
        rez = self.binToHex(rez)

        dopuna_nula = 8 - len(rez)
        temp = '0' * dopuna_nula
        rez = '' + temp + rez

        return rez

    def sumMod(self, A, B):

        rez = (int(A, 16) + int(B, 16))
        wtf = 2 ** 32
        rez = rez % wtf
        rez = str(hex(rez)).replace('0x', '').upper()

        dopuna_nula = 8 - len(rez)
        temp = '0' * dopuna_nula
        rez = '' + temp + rez

        return rez

    def digest(self):

        H0 = '67452301'
        H1 = 'EFCDAB89'
        H2 = '98BADCFE'
        H3 = '10325476'
        H4 = 'C3D2E1F0'

        for i in range(0, len(self.M)):

            W = [None] * 80

            for j in range(0, 16):

                W[j] = self.M[i][j*8:(j+1)*8]

            for t in range(16, 80):

                W[t] = self.ROTL_1(self.hexXOR(self.hexXOR(self.hexXOR(W[t-3], W[t-8]), W[t-14]), W[t-16]))

            A = H0
            B = H1
            C = H2
            D = H3
            E = H4

            for t in range(0, 80):

                f_s = self.f(t, B, C, D)
                TEMP = self.sumMod(self.sumMod(self.sumMod(self.sumMod(self.ROTL_5(A), f_s), E), W[t]), self.K(t))
                E = D
                D = C
                C = self.ROTL_30(B)
                B = A
                A = TEMP

            H0 = self.sumMod(H0, A)
            H1 = self.sumMod(H1, B)
            H2 = self.sumMod(H2, C)
            H3 = self.sumMod(H3, D)
            H4 = self.sumMod(H4, E)

        return H0 + H1 + H2 + H3 + H4



    def init_blocks(self):

        blocks = []
        blok_string = ''

        for c in self.data:

            if len(blok_string) < 128:
                blok_string += c
            else:
                blocks.append(blok_string)
                blok_string = c

        blocks.append(blok_string)

        zadnji_blok = blocks[len(blocks)-1]

        if len(zadnji_blok) * 4 > 447:

            bonus_blok = '0' * 112
            data_len = len(self.data) * 4
            data_len = str(hex(data_len)).replace('0x', '').upper()
            dopuna_data_len = 16 - len(data_len)
            data_len_final = '0' * dopuna_data_len
            data_len_final += data_len

            bonus_blok += data_len

            zadnji_blok_len = len(zadnji_blok)
            if zadnji_blok_len == 127:
                zadnji_blok += '8'
            else:
                dopuna_len = 128 - zadnji_blok_len - 1
                zadnji_blok += '8'
                zadnji_blok += '0' * dopuna_len

            blocks[len(blocks)-1] = zadnji_blok
            blocks.append(bonus_blok)

        else:

            data_len = len(self.data) * 4
            data_len = str(hex(data_len)).replace('0x', '').upper()
            dopuna_data_len = 16 - len(data_len)
            data_len_final = '0' * dopuna_data_len
            data_len_final += data_len

            dopuna_nula = 128 - 1 - 16 - len(zadnji_blok)

            zadnji_blok += '8'
            zadnji_blok += '0' * dopuna_nula
            zadnji_blok += data_len_final

            blocks[len(blocks)-1] = zadnji_blok

        return blocks

    def hexToBin(self, hexChar):

        binarno = str(bin(int(hexChar, 16))).replace('0b', '')

        if len(binarno) == 1:
            binarno = '000' + binarno
        elif len(binarno) == 2:
            binarno = '00' + binarno
        elif len(binarno) == 3:
            binarno = '0' + binarno
        else:
            binarno = binarno

        return binarno

    def binToHex(self, niz_bitova):

        temp_bit = ''
        rez_bitovi = ''

        for bit in niz_bitova:

            if len(temp_bit) < 4:
                temp_bit += bit
            else:
                rez_bitovi += str(hex(int(temp_bit, 2))).replace('0x', '').upper()
                temp_bit = bit

        rez_bitovi += str(hex(int(temp_bit, 2))).replace('0x', '').upper()

        return rez_bitovi

    def ROTL_5(self, hexa):

        niz_bitova = ''

        for c in hexa:
            niz_bitova += self.hexToBin(c)

        prvih_5_bit = niz_bitova[0:5]
        niz_bitova = niz_bitova[5:]
        niz_bitova += prvih_5_bit

        return self.binToHex(niz_bitova)

    def ROTL_30(self, hexa):

        niz_bitova = ''

        for c in hexa:
            niz_bitova += self.hexToBin(c)

        prvih_30_bit = niz_bitova[0:30]
        niz_bitova = niz_bitova[30:]
        niz_bitova += prvih_30_bit

        return self.binToHex(niz_bitova)

    def ROTL_1(self, hexa):

        dopuna_nula = 8 - len(hexa)
        temp = '0' * dopuna_nula
        hexa = '' + temp + hexa

        niz_bitova = ''

        for c in hexa:

            niz_bitova += self.hexToBin(c)

        prvi_bit = niz_bitova[0]
        niz_bitova = niz_bitova[1:]
        niz_bitova += prvi_bit

        return self.binToHex(niz_bitova)

    def f1(self, B, C, D):

        rez_1 = self.hexXOR(C, D)
        rez_2 = self.hexAND(B, rez_1)
        f1_rez = self.hexXOR(D, rez_2)

        return f1_rez

    def f2(self, B, C, D):

        return self.hexXOR(self.hexXOR(B, C), D)

    def f3(self, B, C, D):

        return self.hexOR(self.hexOR(self.hexAND(B, C), self.hexAND(B, D)), self.hexAND(C, D))

    def f(self, t, B, C, D):

        if t >= 0 and t <= 19:
            return self.f1(B, C, D)
        elif t >= 20 and t <= 39:
            return self.f2(B, C, D)
        elif t >= 40 and t <= 59:
            return self.f3(B, C, D)
        else:
            return self.f2(B, C, D)

        return ''

    def K(self, t):

        if t >= 0 and t <= 19:
            return '5A827999'
        elif t >= 20 and t <= 39:
            return '6ED9EBA1'
        elif t >= 40 and t <= 59:
            return '8F1BBCDC'
        else:
            return 'CA62C1D6'