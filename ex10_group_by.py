
from collections import defaultdict


def group_by(f,args):

    result = list(map(f,args))

    d=defaultdict(list)
    for i in args:
        d[f(i)].append(i)

    return dict(d)

#-------------Testing Code--------------
print(group_by(len, ["hi", "bye", "yo", "try","hello"]))
