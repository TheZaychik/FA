import csv
import re


def v3(file1, file2):
    data = []
    with open(file1, 'r') as f:
        srt = f.readline()
    slist = re.findall(r'\w*:', srt)
    dlist = re.split(r'\w*:', srt)
    dlist.pop(0)
    for i in range(len(dlist)):
        dlist[i] = dlist[i].split(',')
    print(dlist)
    for i in range(len(dlist[0])):
        buff = []
        for j in range(len(dlist)):
            buff.append(dlist[j][i])
        data.append(buff)
    data.insert(0, slist)
    print(data)
    with open(file2, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(data)


v3('text.txt', 'output.csv')
