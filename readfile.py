from vocab import vocab
class reader:
    def read(self, path):
        with open (path, "r") as f:
            lines = f.readlines()
            list = []
            eentry = ''
            translation1 = ''
            translation2 = ''
            first = True
            for line in lines:
                try:
                    if line[:8] == '<eentry>':
                        if first == False:
                            list.append(vocab(eentry, translation1, translation2))
                            eentry = ''
                            translation1 = ''
                            translation2 = ''
                        eentry = line
                        first = False
                    elif line[:8] == '<tentry>':
                        translation1 = line
                    elif line[:7] == '<ethai>':
                        translation2 = line
                except Exception as e:
                    print(e)
        return list