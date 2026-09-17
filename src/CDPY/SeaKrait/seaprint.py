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

def reverb(EchoedQuote):
    print(EchoedQuote)
    return


def input_reverb(prompt):
    rinput = input(prompt)
    print(f"{prompt}{rinput}")
    return

def input_reverb_np(prompt):
    rinput = input(prompt)
    print(rinput)
    return


def s_input_reverb(c,prompt):
    rinput = input(prompt)
    while c >= 1:
        print(f"{prompt}{rinput}")
        c -= 1
    return

def s_input_reverb(c,prompt):
    rinput = input(prompt)
    while c >= 1:
        print(rinput)
        c -= 1
    return


