from readfile import reader
from vocab import vocab
from vocabs import vocabs
def count(l: list):
    i = 0
    pairs = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0,
     "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0} 
    while i < len(l):
        if l[i][0] == "a":
            pairs.update({'a': pairs.get("a") + 1})
        elif l[i][0] == "b":
            pairs.update({'b': pairs.get("b") + 1})
        elif l[i][0] == "c":
            pairs.update({'c': pairs.get("c") + 1})
        elif l[i][0] == "d":
            pairs.update({'d': pairs.get("d") + 1})
        elif l[i][0] == "e":
            pairs.update({'e': pairs.get("e") + 1})
        elif l[i][0] == "f":
            pairs.update({'f': pairs.get("f") + 1})
        elif l[i][0] == "g":
            pairs.update({'g': pairs.get("g") + 1})
        elif l[i][0] == "h":
            pairs.update({'h': pairs.get("h") + 1})
        elif l[i][0] == "i":
            pairs.update({'i': pairs.get("i") + 1})
        elif l[i][0] == "j":
            pairs.update({'j': pairs.get("j") + 1})
        elif l[i][0] == "k":
            pairs.update({'k': pairs.get("k") + 1})
        elif l[i][0] == "l":
            pairs.update({'l': pairs.get("l") + 1})
        elif l[i][0] == "m":
            pairs.update({'m': pairs.get("m") + 1})
        elif l[i][0] == "n":
            pairs.update({'n': pairs.get("n") + 1})
        elif l[i][0] == "o":
            pairs.update({'o': pairs.get("o") + 1})
        elif l[i][0] == "p":
            pairs.update({'p': pairs.get("p") + 1})
        elif l[i][0] == "q":
            pairs.update({'q': pairs.get("q") + 1})
        elif l[i][0] == "r":
            pairs.update({'r': pairs.get("r") + 1})
        elif l[i][0] == "s":
            pairs.update({'s': pairs.get("s") + 1})
        elif l[i][0] == "t":
            pairs.update({'t': pairs.get("t") + 1})
        elif l[i][0] == "u":
            pairs.update({'u': pairs.get("u") + 1})
        elif l[i][0] == "v":
            pairs.update({'v': pairs.get("v") + 1})
        elif l[i][0] == "w":
            pairs.update({'w': pairs.get("w") + 1})
        elif l[i][0] == "x":
            pairs.update({'x': pairs.get("x") + 1})
        elif l[i][0] == "y":
            pairs.update({'y': pairs.get("y") + 1})
        elif l[i][0] == "z":
            pairs.update({'z': pairs.get("z") + 1})
        i = i + 1
    return pairs
man = reader()
l = man.read(r"/run/media/harddisk/Documents/Dictionary/etlex")
dic = vocabs(l)
d = dic.convert(l)
k = list(d.keys())
print(count(k))