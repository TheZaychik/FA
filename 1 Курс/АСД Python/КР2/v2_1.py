def cummulate(*args, mul=False):
    dlist = []
    for i in range(len(args)):
        if i == 0:
            dlist.append(args[0])
            continue
        if mul:
            dlist.append(dlist[i - 1] * args[i])
        else:
            dlist.append(dlist[i - 1] + args[i])
    return dlist



