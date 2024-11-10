class vocab:
    def __init__(self, eentry, thai1, thai2) -> None:
        self.eentry_sub = eentry
        self.thai1_sub = thai1
        self.thai2_sub = thai2
        self.strip()
    def strip(self):
        try:
            self.eentry_sub = self.eentry_sub[8:]
            self.eentry_sub = self.eentry_sub[:-10]
            self.thai1_sub = self.thai1_sub[8:]
            self.thai1_sub = self.thai1_sub[:-10]
            self.thai2_sub = self.thai2_sub[7:]
            self.thai2_sub = self.thai2_sub[:-9]
        except Exception as e:
            print(e)
word = vocab("<eentry>abandon</eentry>", "<tentry>ทิ้ง</tentry>", "<ethai>''</ethai>")
print(word)