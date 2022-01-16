from fumen import fumen

def tostr(val:int) -> str:
    return str(val // 100) + '.' + str(val % 100)

def analyze(dat) -> None:
    ranks, ars = [], []
    for id in dat:
        nf:fumen = dat[id]
        for i, rank, ar in zip(nf.pc, nf.rank, nf.ar):
            if i == 0:
                continue
            ranks.append(tostr(rank))
            ars.append(ar)
    import matplotlib.pyplot as plt
    plt.plot(ranks, ars)
    plt.show()