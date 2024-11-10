from readfile import reader
from vocab import vocab
class vocabs:
    def __init__(self, list: list[vocab]) -> None:
        self.list = list
        pass
    def convert(self, list: list[vocab]):
        dic = {}
        try:
            i = 0
            while i < len(list):
                eng = list[i].eentry_sub.lower()
                numbers = ["0", "1", "2", "3", "4" , "5"]
                string_list = []
                k = 0
                while k < len(eng):
                    if eng[k] not in numbers:
                        string_list.append(eng[k])
                    k = k + 1
                new_eng = ''.join(string_list)
                if list[i].thai2_sub != '':
                    temp = list[i].thai1_sub +  ', ' + list[i].thai2_sub
                else: temp = list[i].thai1_sub
                if new_eng in dic.keys():
                    temp = dic.get(new_eng)
                    if list[i].thai2_sub != '':
                        temp = temp + ', ' + list[i].thai1_sub +  ', ' + list[i].thai2_sub
                        dic.update({new_eng: temp})
                    else:
                        temp = temp + ', ' + list[i].thai1_sub
                        dic.update({new_eng: temp})
                else: dic.update({new_eng: temp})
                i = i + 1
        except Exception as e:
            print(e)
        return dic
l = reader()
a = vocabs(r"/run/media/harddisk/Documents/Dictionary/etlex")
print(a.convert(l.read(r"/run/media/harddisk/Documents/Dictionary/etlex")))