def repl(strk, **kwargs):
    for k in kwargs.keys():
        strk = strk.replace(k, kwargs[k])
    return strk


s = repl('replace my val abc', my='s1', abc='fff')
print(s)
