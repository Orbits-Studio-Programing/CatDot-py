def CONST_GROUP(type):

    CONST_HELLO = "Hello, World!"
    CONST_GOODBYE = "Goodbye, World!"
    CONST_FAREWELL = "Farewell, World!"
    CONST_END = "The End."

    if type == "greeting":
        return CONST_HELLO
    elif type == "farewell":
        return CONST_GOODBYE
    elif type == "parting":
        return CONST_FAREWELL
    elif type == "end":
        return CONST_END
    else:
        return " "

def hi(capyn):
    if capyn > 0:
        return "Hi"
    if capyn < 0:
        return "hi"
    else:
        return " "

def hi_p(capyn):
        if capyn > 0:
            print("Hi")
        if capyn < 0:
            print("hi")
        else:
            print(" ")

greet = ["hi","hello","good morning", "good afternoon", "Hi","Hello","Good morning", "Good afternoon", "Good Morning", "Good Afternoon", 
"hi!","hello!","good morning!", "good afternoon!", "Hi!","Hello!","Good morning!", "Good afternoon!", "Good Morning!", "Good Afternoon!"]

passing = ["bye", "good bye", "see you later", "Bye", "Good bye", "See you later", "Good Bye", "See You later", "See You Later", 
"bye!", "good bye!", "see you later!", "Bye!", "Good bye!", "See you later!", "Good Bye!", "See You later!", "See You Later!", ]
