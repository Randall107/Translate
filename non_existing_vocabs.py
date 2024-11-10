from readfile import reader
from vocab import vocab
from vocabs import vocabs
def get_vocabs(d: dict):
    with open (r"/run/media/harddisk/Documents/Dictionary/db", "r") as file:
        lines = file.readlines()
        db = []
        for line in lines:
            db.append(line[:-1])
    i = 0
    while i < len(db):
        if db[i] in d:
            del d[db[i]]
        i = i + 1
    i = 0
    with open(r"/run/media/harddisk/Documents/Dictionary/non_existing", 'a') as file:
        for key, value in d.items():
            file.write(f"{key}: {value}\n")
    return d
man = reader()
l = man.read(r"/run/media/harddisk/Documents/Dictionary/etlex")
dic = vocabs(l)
d = dic.convert(l)
print(get_vocabs(d))