class Fibonacci:
    def __init__(self, inputString):
        self.inputString = inputString
        self.inputString = self.inputString.split(" ")
        self.Nnum = self.inputString[0]
        self.Nnum = int(self.Nnum)
        self.Sstring = self.inputString[1]
        self.F = ["A", "B"]

    def getFk(self):
            self.i = 2
            while self.i < self.Nnum:
                self.F.append(self.F[self.i-1] + self.F[self.i-2])
                self.i += 1
            return self.F[self.i-1]

    # #Count theo số lần xuất hiện của chuỗi
    # def countSstring2(self):
    #     return self.F[self.i-1].count(self.Sstring)

    # Count theo đề bài
    def countSstring(self, Fstring):
        self.S_count = 0
        self.Fstring = Fstring
        self.Fstring_cut = ""
        while len(self.Fstring) >= len(self.Sstring):
            self.Fstring_cut = self.Fstring[0:len(self.Sstring)]
            if self.Sstring == self.Fstring_cut:
                self.S_count += 1
            self.Fstring = self.Fstring[1:]
        return self.S_count
