def full_file(exec_func, target, towa=None):
    if exec_func=="w":
        with open(target, "w") as file:
            if towa==None:
                raise ValueError("inappropriate string for exec_func " + '"' + "w" + '"')
            else:
                return file.write(towa)
    if exec_func=="a":
        with open(target, "a") as file:
            if towa==None:
                raise ValueError("inappropriate string for exec_func " + '"' + "a" + '"')
            else:
                return file.write(towa)
    if exec_func=="r":
        with open(target, "r") as file:
            if towa!=None:
                raise ValueError("string not accepted for exec_func " + '"' + "r" + '"')
            else:
                return file.read(towa)
    else:
        raise ValueError("Invalid exec_func")

full_file("a","py.py","we")

e = full_file("r","py.py")
print(e)


EasyRead_VER = "26.1.0"