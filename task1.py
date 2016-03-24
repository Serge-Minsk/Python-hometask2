def diction(key, value):
    c={}
    if len(key) >= len(value):
        for i in range(0,len(value)):
            c[key[i]] = value[i]
        for i in range(len(value),len(key)):
            c[key[i]] = None
    else:
        for i in range(0, len(key)):
            c[key[i]] = value[i]
    print c
    return c

k = diction(['a','b','c'],[1])
