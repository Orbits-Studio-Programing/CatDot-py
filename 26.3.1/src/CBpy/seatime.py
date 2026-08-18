def tick_cd(s,e,incs):
    if s < e:
        raise ValueError("Start time larger than end time")
    elif s > e and incs > 0:
        while s > e:
            print(s)
            s -= 1
        print(s)
    elif s > e and incs <= 0:
        while s > e:
            s -= 1
            print(s)

def smart_cd(s,e,lengs,incs):
    leng = lengs
    if s < e:
        raise ValueError("Start time larger than end time")
    elif s > e and incs > 0:
        while s > e:
            while lengs > 0:
                print(s)
                lengs -= 1
            s -= 1
            lengs = leng
        print(s)
    elif s > e and incs <= 0:
        while s > e:
            s -= 1
            lengs = leng
            while lengs > 0:
                print(s)
                lengs -= 1

def basic_cd(s,e,incs):
    smart_cd(s,e,14000,incs)

def time_rn():
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time


def time_send_inf():
    from datetime import datetime
    while True:
        from datetime import datetime
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(current_time)

  