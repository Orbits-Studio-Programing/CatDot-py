def atbash_uno(text):
    atb_keydict = {
        "a": "z",
        "b": "y",
        "c": "x",
        "d": "w",
        "e": "v",
        "f": "u",
        "g": "t",
        "h": "s",
        "i": "r",
        "j": "q",
        "k": "p",
        "l": "o",
        "m": "n",
        "n": "m",
        "o": "l",
        "p": "k",
        "q": "j",
        "r": "i",
        "s": "h",
        "t": "g",
        "u": "f",
        "v": "e",
        "w": "d",
        "x": "c",
        "y": "b",
        "z": "a",
        "A": "Z",
        "B": "Y",
        "C": "X",
        "D": "W",
        "E": "V",
        "F": "U",
        "G": "T",
        "H": "S",
        "I": "R",
        "J": "Q",
        "K": "P",
        "L": "O",
        "M": "N",
        "N": "M",
        "O": "L",
        "P": "K",
        "Q": "J",
        "R": "I",
        "S": "H",
        "T": "G",
        "U": "F",
        "V": "E",
        "W": "D",
        "X": "C",
        "Y": "B",
        "Z": "A"
    }
    s = ""
    for i in text:
        if i in atb_keydict:
            s += atb_keydict[i]
        else:
            s += i
    return s

def encrypt_int(i):
    return (((i * 12332) / 34) * 23) - 2345 + 34

def unencrypt_int(ei):
    uenc = ei - 34 + 2345
    return ((uenc / 23) * 34) / 12332


def full_scram(i, k):
    if i == 0:
        raise ValueError("The 'i' parameter cannot be zero due to division operations.")
        
    if k == "r":
        import random
        r = random.randint(1, 1000000)
        part = r / i
        return (i * r) - part
    else:
        k_num = float(k) 
        kpart = k_num / i
        return (i * k_num) - kpart





