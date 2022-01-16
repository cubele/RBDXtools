import csv

class fumen:
    def __init__(self, sp, name, comp, charter, level, diff, dens, bpm) -> None:
        self.issp = sp
        self.name = name
        self.composer = comp
        self.charter = charter
        self.level = level
        self.diff = diff
        self.density = dens
        self.bpm = bpm
        self.ar = []
        self.score = []
        self.fc = []
        self.pc = []
        self.rank = []
        for l, d in zip(level, diff):
            if l == '-':
                l = 0
            l = int(l)
            if d == '-':
                self.rank.append(l * 100)
            else:
                if d == "4?":
                    d = "4"
                if d == "?":
                    d = "0"
                self.rank.append(l * 100 + int(d))

    def __str__(self) -> str:
        print(self.issp, self.name, self.composer, self.charter, self.level, self.diff, self.bpm)
        print(self.ar, self.score, self.fc, self.pc)
        return "-------------------------------------------------------"

def parseFumen(row, sp) -> fumen:
    rd = lambda n: [row[n], row[n + 5], row[n + 10]]
    name, comp = row[1], row[2]
    if not sp:
        charter, level, diff, dens = rd(12), rd(8), rd(9), rd(11)
    else:
        charter, level, diff, dens = [row[-1]], [row[-5]], [row[-4]], [row[-2]]
    bpm = row[5] if sp else row[4]
    return fumen(sp, name, comp, charter, level, diff, dens, bpm)

specials = {100006: 100595,
            100020: 100710,
            100033: 100929,
            100044: 100708,
            100052: 100928,
            100053: 100515,
            100122: 100513,
            100161: 100257,
            100162: 100512,
            100163: 100622,
            100225: 100514,
            100237: 100709,
            100276: 100931,
            100465: 100930,
            100683: 100685,
            100703: 100705,
            100704: 100706,
            100770: 100773,
            100905: 100910,
            215530: 100707
            }

def loadAll(fs) -> None:
    with open('fumen.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        skip = 1;
        for row in reader:
            if skip > 0:
                skip -= 1
                continue
            fid = int("500" + row[0])
            fs[fid] = parseFumen(row, False)
            if row[-1] != '-' and row[-2] != '-':
                if int(row[0]) in specials:
                    fid = int("500" + str(specials[int(row[0])]))
                else:
                    fid = int("500" + str(int(row[0]) + 1))
                fs[fid] = parseFumen(row, True)