from re import L
from fumen import fumen

def tostr(val:int) -> str:
    return str(val // 100) + '.' + str(val % 100)

def analyze(dat, minar, rankl, rankr, name) -> None:
    dats = []
    for id in dat:
        nf:fumen = dat[id]
        for i, rank, ar, fc in zip(nf.pc, nf.rank, nf.ar, nf.fc):
            if i == 0:
                continue
            if ar * 100 < minar or rank < rankl or rank > rankr:
                continue
            dats.append((rank, ar * 100, fc))
    dats = sorted(dats, key=lambda x: (x[0]))
    print("analyzed {} scores".format(len(dats)))
    ranks, ars, fcs = [], [], []
    cnt, sar = {}, {}
    difs, aar = [], []
#    a98, a985, a99 = [], [], []
    for i in dats:
        ranks.append(tostr(i[0]))
        ars.append(i[1])
        fcs.append(i[2])
        if not tostr(i[0]) in cnt:
            cnt[tostr(i[0])] = 0
            sar[tostr(i[0])] = 0
        cnt[tostr(i[0])] += 1
        sar[tostr(i[0])] += i[1]
    for dif in cnt:
        sar[dif] /= cnt[dif]
        difs.append(dif)
        aar.append(sar[dif])
#        a98.append(98), a99.append(99), a985.append(98.5)
    import matplotlib.pyplot as plt
    plt.figure(figsize=(18, 12), dpi = 1080)
    plt.scatter(ranks, ars, marker='x', c=fcs, cmap="brg")
    plt.plot(difs, aar, marker = 'o', color = 'r', label = "avg")
#    plt.plot(difs, a98, color = 'y', label = "98%")
#    plt.plot(difs, a985, color = 'c', label = "98.5%")
#    plt.plot(difs, a99, color = 'm', label = "99%")
    plt.legend(loc="upper left")
    plt.title("ScoreData")
    plt.xlabel("difficulty")
    plt.ylabel("AR")
    plt.savefig('./output/{}.png'.format(name), bbox_inches = 'tight')