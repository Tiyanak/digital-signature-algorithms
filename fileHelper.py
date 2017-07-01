import os
import subprocess as sp
from tkinter import filedialog
import binascii


def openWithNotepad(filename):
    programName = "notepad.exe"

    sp.Popen([programName, filename])


def writeRSA(path, desc, method, keylen, key):
    file = open(path, 'w')

    file.write("---BEGIN OS2 CRYPTO DATA---\n")
    file.write("Description:\n")
    file.write("\t" + desc + "\n\n")
    file.write("Method:\n")
    file.write("\t" + method + "\n\n")
    file.write("Key length:\n")
    file.write("\t" + keylen + "\n\n")
    file.write("Key:\n\t")
    i = 0
    j = 0
    while j < len(key):
        if i == 59:
            file.write(key[j] + "\n\t")
            i = 0
        else:
            file.write(key[j])
            i += 1

        j += 1

    file.write("\n\n---END OS2 CRYPTO DATA---")

    file.close()


def writePotpis(path, desc, method, keylen, signature):
    file = open(path, 'w')

    file.write("---BEGIN OS2 CRYPTO DATA---\n")
    file.write("Description:\n")
    file.write("\t" + desc + "\n\n")
    file.write("File name:\n")
    file.write("\t" + path + "\n\n")
    file.write("Method:\n")
    file.write("\t" + method + "\n\n")
    file.write("Key length:\n")
    file.write("\t" + keylen + "\n\n")
    file.write("Signature:\n\t")
    i = 0
    j = 0
    while j < len(signature):
        if i == 59:
            file.write(signature[j] + "\n\t")
            i = 0
        else:
            file.write(signature[j])
            i += 1

        j += 1

    file.write("\n\n---END OS2 CRYPTO DATA---")

    file.close()


def writeOmotnica(path, desc, method, keylen, data, key):
    file = open(path, 'w')

    file.write("---BEGIN OS2 CRYPTO DATA---\n")
    file.write("Description:\n")
    file.write("\t" + desc + "\n\n")
    file.write("File name:\n")
    file.write("\t" + path + "\n\n")
    file.write("Method:\n")
    file.write("\t" + method + "\n\n")
    file.write("Key length:\n")
    file.write("\t" + keylen + "\n\n")
    file.write("Envelope data:\n\t")
    i = 0
    j = 0
    while j < len(data):
        if i == 59:
            file.write(data[j] + "\n\t")
            i = 0
        else:
            file.write(data[j])
            i += 1

        j += 1

    file.write("\n\nEnvelope crypt key:\n\t")

    i = 0
    j = 0
    while j < len(key):
        if i == 59:
            file.write(key[j] + "\n\t")
            i = 0
        else:
            file.write(key[j])
            i += 1

        j += 1

    file.write("\n\n---END OS2 CRYPTO DATA---")

    file.close()


def writeIzlaz(path, desc, method, data):
    file = open(path, 'w')

    file.write("---BEGIN OS2 CRYPTO DATA---\n")
    file.write("Description:\n")
    file.write("\t" + desc + "\n\n")
    file.write("File name:\n")
    file.write("\t" + path + "\n\n")
    file.write("Method:\n")
    file.write("\t" + method + "\n\n")
    file.write("Data:\n\t")
    i = 0
    j = 0
    while j < len(data):
        if i == 59:
            file.write(data[j] + "\n\t")
            i = 0
        else:
            file.write(data[j])
            i += 1

        j += 1

    file.write("\n\n---END OS2 CRYPTO DATA---")

    file.close()


def writeSha1(path, desc, method, data):
    file = open(path, 'w')

    file.write("---BEGIN OS2 CRYPTO DATA---\n")
    file.write("Description:\n")
    file.write("\t" + desc + "\n\n")
    file.write("File name:\n")
    file.write("\t" + path + "\n\n")
    file.write("Method:\n")
    file.write("\t" + method + "\n\n")
    file.write("Digest:\n\t")
    i = 0
    j = 0
    while j < len(data):
        if i == 59:
            file.write(data[j] + "\n\t")
            i = 0
        else:
            file.write(data[j])
            i += 1

        j += 1

    file.write("\n\n---END OS2 CRYPTO DATA---")

    file.close()


def writeDES(path, desc, method, data):
    file = open(path, 'w')

    file.write("---BEGIN OS2 CRYPTO DATA---\n")
    file.write("Description:\n")
    file.write("\t" + desc + "\n\n")
    file.write("File name:\n")
    file.write("\t" + path + "\n\n")
    file.write("Method:\n")
    file.write("\t" + method + "\n\n")
    file.write("Data:\n\t")
    i = 0
    j = 0
    while j < len(data):
        if i == 59:
            file.write(data[j] + "\n\t")
            i = 0
        else:
            file.write(data[j])
            i += 1

        j += 1

    file.write("\n\n---END OS2 CRYPTO DATA---")

    file.close()


def writeDESKey(path, desc, method, key):
    file = open(path, 'w')

    file.write("---BEGIN OS2 CRYPTO DATA---\n")
    file.write("Description:\n")
    file.write("\t" + desc + "\n\n")
    file.write("Method:\n")
    file.write("\t" + method + "\n\n")
    file.write("Secret key:\n\t")
    i = 0
    j = 0
    while j < len(key):
        if i == 59:
            file.write(key[j] + "\n\t")
            i = 0
        else:
            file.write(key[j])
            i += 1

        j += 1

    file.write("\n\n---END OS2 CRYPTO DATA---")

    file.close()


def load(path):
    ## Loads the data from the input file in a dictionary.
    fp = open(path, 'r')

    data = []
    while True:
        line = fp.readline()
        if line == '':
            break
        line = line.strip()
        if line != '':
            data.append(line)
    keywords = ['Description', 'File name', 'Method', 'Key length',
                'Secret key', 'Key', 'Exponent',
                'Signature', 'Data', 'Envelope data', 'Envelope crypt key', 'Digest']
    beginning = '---BEGIN OS2 CRYPTO DATA---'
    ending = '---END OS2 CRYPTO DATA---'
    while data[0] != beginning:
        data.pop(0)
    while data[len(data) - 1] != ending:
        data.pop()
    items = {}
    i = 0
    while True:
        if data[i] == ending:
            break
        elif data[i] == beginning:
            i += 1
            continue
        elif data[i][len(data[i]) - 1] == ':' and data[i][0:len(data[i]) - 1] in keywords:
            activeKeyword = data[i][0:len(data[i]) - 1]
            items[activeKeyword] = []
            i += 1
        else:
            items[activeKeyword].append(data[i])
            i += 1
    return items


def get_items(name, keydata):
    ### Returns the data associated with the given key (or name).
    if name in keydata:
        return keydata[name]
    else:
        return None


def get_n_value(name, No, keydata):
    ## Used for retrieving key lengths. Returns the length in the decimal base
    ## of either the first or the second key, depending on No.
    if name not in keydata:
        return None
    hval = keydata[name][No]
    return int(hval, 16)


def get_hexc_value(name, keydata):
    ## Used for retrieving various data. Returns all of the data associated
    ## with the key (or name), but merged in a single string.
    if name not in keydata:
        return None
    return ''.join(keydata[name])


def get_hex8_value(name, keydata):
    ## Used for retriving various data that represents hexadecimal numbers.
    ## Returns a list of positive decimal numbers that correspond to 2-digit
    ## hexadecimal numbers.
    if name not in keydata:
        return None
    data = get_hexc_value(name, keydata)
    length = len(data)
    if length % 2 != 0:
        data = data.zfill(length + 1)
    position = 0
    bit8 = []
    while position < len(data):
        bit8.append(int(data[position:position + 2], 16))
        position += 2
    return bit8


def get_hex16_value(name, keydata):
    ## Used for retriving various data that represents hexadecimal numbers.
    ## Returns a list of positive decimal numbers that correspond to 4-digit
    ## hexadecimal numbers.
    if name not in keydata:
        return None
    data = get_hexc_value(name, keydata)
    length = len(data)
    if length % 4 != 0:
        data = data.zfill(length + 4 - length % 4)
    position = 0
    bit16 = []
    while position < len(data):
        bit16.append(int(data[position:position + 4], 16))
        position += 4
    return bit16


def get_hex32_value(name, keydata):
    ## Used for retriving various data that represents hexadecimal numbers.
    ## Returns a list of positive decimal numbers that correspond to 8-digit
    ## hexadecimal numbers.
    if name not in keydata:
        return None
    data = get_hexc_value(name, keydata)
    length = len(data)
    if length % 8 != 0:
        data = data.zfill(length + 8 - length % 8)
    position = 0
    bit32 = []
    while position < len(data):
        bit32.append(int(data[position:position + 8], 16))
        position += 8
    return bit32


def get_b64_u8_value(name, keydata):
    ## Used for retrieving data written in Base64. Returns a string.
    if name not in keydata:
        return None
    from base64 import b64decode
    return b64decode(get_hexc_value(name, keydata))


def get_b64_u16_value(name, keydata):
    ## Used for retrieving data written in Base64. Returns a list of short
    ## integers.
    if name not in keydata:
        return None
    from base64 import b64decode
    data = b64decode(get_hexc_value(name, keydata))
    length = len(data)
    retval = []

    for i in range(0, length, 2):
        retval.append((ord(data[i]) << 8) + ord(data[i + 1]))

    if length % 2 != 0:
        retval.append(ord(data[i]) << 8)
    return retval


def get_b64_u32_value(name, keydata):
    ## Used for retrieving data written in Base64. Returns a list of integers.
    if name not in keydata:
        return None
    from base64 import b64decode
    data = b64decode(get_hexc_value(name, keydata))
    length = len(data)
    retval = []

    for i in range(0, length, 4):
        retval.append((ord(data[i]) << 24) + (ord(data[i + 1]) << 16) + (ord(data[i + 2]) << 8) + ord(data[i + 3]))

    maximum = max(range(0, length, 4))
    dif = length - maximum

    if dif == 1:
        retval.append(ord(data[length - 1]) << 24)
    elif dif == 2:
        retval.append((ord(data[length - 2]) << 24) + ord(data[length - 1]) << 16)
    elif dif == 3:
        retval.append((ord(data[length - 3]) << 24) + ord(data[length - 2]) << 16 + ord(data[length - 1]) << 8)

    return retval


def put_header(mesg, fp):
    ## Writes a message (comment) and the file header in the output file.
    try:
        fp.writelines(mesg + '\n')
        fp.write('---BEGIN OS2 CRYPTO DATA---\n')
        return 1
    except:
        return 0


def put_footer(mesg, fp):
    ## Writes the file footer and a message(comment) in the output file.
    try:
        fp.write('---END OS2 CRYPTO DATA---\n')
        fp.writelines(mesg + '\n')
        return 1
    except:
        return 0


def put_data_d(name, value1, value2, fp):
    ## Used for writing keys in the output file.
    try:
        fp.write(name + ':\n')
        value = str(hex(value1))[2:]
        if value[len(value) - 1] == 'L':
            value = value[:len(value) - 1]
        if len(value) % 2 != 0:
            value = value.zfill(len(value) + 1)
        fp.write('    ' + value + '\n')
        if value2 != -1:
            value = str(hex(value2))[2:]
            if value[len(value) - 1] == 'L':
                value = value[:len(value) - 1]
            if len(value) % 2 != 0:
                value = value.zfill(len(value) + 1)
            fp.write('    ' + value + '\n')
        fp.write('\n')
        return 1
    except:
        return 0


def put_data_s(name, value1, value2, fp):
    ## Used for writing simple, textual data.
    try:
        fp.write(name + ':\n')
        fp.write('    ' + value1 + '\n')
        if value2 != None:
            fp.write('    ' + value2 + '\n')
        fp.write('\n')
        return 1
    except:
        return 0


def put_data_hexu8(name, value, length, fp):
    ## Used for writing various hexadecimal data (stored in a string).
    try:
        fp.write(name + ':\n')
        if length % 2 != 0:
            value = str(value).zfill(length + 1)
            length += 1
        position = 0
        while position < length:
            if position + 60 < length:
                fp.write('    ' + value[position:position + 60] + '\n')
            else:
                fp.write('    ' + value[position:length] + '\n')
            position += 60
        fp.write('\n')
        return 1
    except:
        return 0


def put_data_hexu16(name, value, length, fp):
    ## Used for writing various hexadecimal data (stored in a list of short
    ## integers).
    s = ''
    for i in value:
        s += chr(i >> 8 & 255)
        s += chr(i & 255)
    return put_data_hexu8(name, s, len(s), fp)


def put_data_hexu32(name, value, length, fp):
    ## Used for writing various hexadecimal data (stored in a list of
    ## integers).
    s = ''
    for i in value:
        s += chr(i >> 24)
        s += chr(i >> 16 & 255)
        s += chr(i >> 8 & 255)
        s += chr(i & 255)
    return put_data_hexu8(name, s, len(s), fp)


def put_data_b64u8(name, value, length, fp):
    ## Used for writing data (stored in a string) in Base64 encoding.
    try:
        fp.write(name + ':\n')
        from base64 import b64encode
        data = b64encode(value)
        position = 0
        while position < len(data):
            if position + 60 < len(data):
                fp.write('    ' + data[position:position + 60] + '\n')
            else:
                fp.write('    ' + data[position:len(data)] + '\n')
            position += 60
        fp.write('\n')
        return 1
    except:
        return 0


def put_data_b64u16(name, value, length, fp):
    ## Used for writing data (stored in a list of short integers) in Base64
    ## encoding.
    s = ''
    for i in value:
        s += chr(i >> 8 & 255)
        s += chr(i & 255)
    return put_data_b64u16(name, s, len(s), fp)


def put_data_b64u32(name, value, length, fp):
    ## Used for writing data (stored in a list of integers) in Base64 encoding.
    s = ''
    for i in value:
        s += chr(i >> 24)
        s += chr(i >> 16 & 255)
        s += chr(i >> 8 & 255)
        s += chr(i & 255)
    return put_data_b64u8(name, s, len(s), fp)


def concatList(list):
    return ''.join(list).strip()

def hextranslate(s):
    res = ""
    for i in range(int(len(s) / 2)):
        realIdx = i * 2
        res = res + chr(int(s[realIdx:realIdx + 2], 16))
    return res

def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        try:
            initializer = next(it)
        except StopIteration:
            raise TypeError('reduce() of empty sequence with no initial value')
    accum_value = initializer
    for x in it:
        accum_value = function(accum_value, x)
    return accum_value

# convert string to hex
def toHex(s):
    lst = []
    for ch in s:
        hv = hex(ord(ch)).replace('0x', '')
        if len(hv) == 1:
            hv = '0' + hv
        lst.append(hv)

    return reduce(lambda x, y: x + y, lst)


# convert hex repr to string
def toStr(s):
    return s and chr(int(s[:2], base=16)) + toStr(s[2:]) or ''
