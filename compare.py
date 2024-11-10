from readfile import reader
from vocab import vocab
from vocabs import vocabs
def compare(d: list):
    with open (r"/run/media/harddisk/Documents/Dictionary/db", "r") as file:
        lines = file.readlines()
        db = []
        for line in lines:
            db.append(line[:-1])
    i = 0
    while i < len(db):
        if db[i] in d:
            d.remove(db[i])
        i = i + 1
    return d
man = reader()
l = man.read(r"/run/media/harddisk/Documents/Dictionary/etlex")
dic = vocabs(l)
d = dic.convert(l)
k = list(d.keys())
print(len(compare(k)))