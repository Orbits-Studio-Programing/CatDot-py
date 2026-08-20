def print_sb(ip):
    print(str(ip))

def print_hw():
    print("Hello, world!")

def printer(msg,c):
    while c > 0:
        print(msg)
        c -= 1

def bit_printer_aut(msg,c,car):
    while c > 0:
        print(msg[int(car-1)])
        c -= 1

def bit_printer_man(msg,c,car):
    while c > 0:
        print(msg[int(car)])
        c -= 1
