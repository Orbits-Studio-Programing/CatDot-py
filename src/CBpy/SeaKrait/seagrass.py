def graphvertex_2(k,h):
    ans0 = k+h
    vertex = ans0/2
    return vertex

def graphxintersept_2(k,h):
    ans1 = 0-k
    ans2 = 0-h
    xintersept = [ans1, ans2]
    return xintersept

def graphxintersept_2_wa(k,h):
    ans1 = 0-k
    ans2 = 0-h
    ans3 = 0
    xintersept = [ans1, ans2, ans3]
    return xintersept

def graphpattern_0t_basic(pat):
    diff = pat[1]-pat[0]
    zerot = pat[0] - diff
    return zerot

def graphpattern_0t_2(pat):
    diff1 = pat[1]-pat[0]
    diff1alt = pat[2]-pat[1]
    if diff1 == diff1alt:
        raise ValueError("Non-Quadratic")
    else:
        diff2 = diff1alt-diff1
        diff0 = diff1-diff2
        zerot = pat[0]-diff0
        return zerot

def graphpattern_0t_smart(pat):
    diff1 = pat[1]-pat[0]
    diff1alt = pat[2]-pat[1]
    if diff1 == diff1alt:
        graphpattern_0t_basic(pat)
    else:
        diff2 = diff1alt-diff1
        diff0 = diff1-diff2
        zerot = pat[0]-diff0
        return zerot


