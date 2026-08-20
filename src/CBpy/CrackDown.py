atr = aiter
al = all
bol = bool
cal = callable
cm = classmethod
dlar = delattr
div = divmod
dct = dict
dr = dir
enm = enumerate
flr = filter
flt = float
fmt = format
fs = frozenset
ga = getattr
ha = hasattr
hsh = hash
hlp = help
ipt = input


def ant(i, *args): 
    return anext(i, *args)

def ay(*args): 
    if len(args) == 1:
        return any(args[0])
    return any(args)

def aci(obj): 
    return ascii(obj)

def bp(*args, **kwargs): 
    return breakpoint(*args, **kwargs)

def ba(*args, **kwargs): 
    return bytearray(*args, **kwargs)

def bys(*args, **kwargs): 
    return bytes(*args, **kwargs)

def cp(*args, **kwargs): 
    return compile(*args, **kwargs)

def cpx(*args, **kwargs): 
    return complex(*args, **kwargs)

def evl(*args, **kwargs): 
    return eval(*args, **kwargs)

def exc(*args, **kwargs): 
    return exec(*args, **kwargs)

CrackDown_VER = "26.2.0"