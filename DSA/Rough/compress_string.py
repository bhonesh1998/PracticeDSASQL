from itertools import groupby

string = input()

for k, g in groupby(string):
    print((len(list(g)), int(k)), end=" ")