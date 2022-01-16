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

    def __str__(self) -> str:
        print(self.issp, self.name, self.composer, self.charter, self.level, self.diff, self.bpm)
        return "-------------------------------------------------------";

def parseFumen(row, sp) -> fumen:
    rd = lambda n: [row[n], row[n + 5], row[n + 10]]
    name, comp = row[1], row[2]
    if not sp:
        charter, level, diff, dens = rd(12), rd(8), rd(9), rd(11)
    else:
        charter, level, diff, dens = [row[-1]], [row[-5]], [row[-4]], [row[-2]]
    bpm = row[5] if sp else row[4]
    return fumen(sp, name, comp, charter, level, diff, dens, bpm)

def loadAll(fs) -> None:
    with open('fumen.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        skip = 1;
        for row in reader:
            if skip > 0:
                skip -= 1
                continue
            fid = "500" + row[0]
            fs[fid] = parseFumen(row, False)
            if row[-1] != '-':
                fid = "500" + str(int(row[0]) + 1)
                fs[fid] = parseFumen(row, True)