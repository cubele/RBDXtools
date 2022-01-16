from re import L
from fumen import fumen

def tostr(val:int) -> str:
    return str(val // 100) + '.' + str(val % 100)

def analyze(dat) -> None:
    dats = []
    for id in dat:
        nf:fumen = dat[id]
        for i, rank, ar in zip(nf.pc, nf.rank, nf.ar):
            if i == 0:
                continue
            if ar < 0.969 or rank < 1100:
                continue
            dats.append((rank, ar * 100))
    dats = sorted(dats, key=lambda x: (x[0]))
    ranks, ars = [], []
    cnt, sar = {}, {}
    difs, aar = [], []
    for i in dats:
        ranks.append(tostr(i[0]))
        ars.append(i[1])
        if not tostr(i[0]) in cnt:
            cnt[tostr(i[0])] = 0
            sar[tostr(i[0])] = 0
        cnt[tostr(i[0])] += 1
        sar[tostr(i[0])] += i[1]
    for dif in cnt:
        sar[dif] /= cnt[dif]
        difs.append(dif)
        aar.append(sar[dif])
    import matplotlib.pyplot as plt
    plt.plot(ranks, ars, 'x')
    plt.plot(difs, aar, marker = 'o', color = 'r')
    plt.show()