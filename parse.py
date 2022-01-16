#tables： ZSCOREDATA    Z_METADATA    Z_MODELCACHE  Z_PRIMARYKEY
'''
Z_PK               int64
Z_ENT              int64
Z_OPT              int64

ZFCBAS             int64
ZFCHAR             int64
ZFCMED             int64

playcount
ZPCBAS             int64
ZPCHAR             int64
ZPCMED             int64

???
ZRABAS             int64
ZRAHAR             int64
ZRAMED             int64

score
ZSCOBAS            int64
ZSCOHAR            int64
ZSCOMED            int64

fumenid
ZTUNEID            int64

AR
ZARBAS           float64
ZARHAR           float64
ZARMED           float64

ZLASTPLAYDATE    float64
ZCHKSCO           object
'''
import pandas as pd
import sqlite3

db = sqlite3.connect('./score/ScoreData.sqlite')
'''
allstore = pd.read_sql_query("SELECT * FROM ZSCOREDATA", con=db)
for index, i in allstore.iterrows():
    print(i["ZTUNEID"], i["ZARBAS"], i["ZARMED"], i["ZARHAR"])
'''

from fumen import loadAll, fumen
fumens = {}
loadAll(fumens)
for fid in fumens:
    df = pd.read_sql_query("SELECT * FROM ZSCOREDATA where ZTUNEID = " + str(fid), con=db)
    nf:fumen = fumens[fid]
    if (df.empty):
        nf.pc = [0, 0, 0]
        continue
    rd = lambda s: [df['Z' + s + "BAS"].item(), df['Z' + s + "MED"].item(), df['Z' + s + "HAR"].item()]
    if nf.issp:
        nf.pc, nf.ar, nf.score, nf.fc = [df["ZPCBAS"].item()], [df["ZARBAS"].item()], [df["ZSCOBAS"].item()], [df["ZFCBAS"].item()]
    else:
        nf.pc, nf.ar, nf.score, nf.fc = rd("PC"), rd("AR"), rd("SCO"), rd("FC")

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-a", "--analyze", help="analyze scoredata", action="store_true", default=False)
parser.add_argument("-p", "--playlist", help="generate playlist", action="store_true", default=False)

parser.add_argument("-ainfo", "--analyze_info", dest="ainfo", nargs='+', type=str,
                    help="""info for analyzing. format:minar rankl rankr. can accept multiple sets.
                    example:98.0 11.3 12.5 95.0 10.0 11.1""",
                    default=["98.0", "11.3", "12.5", "95.0", "10.0", "11.1"])

parser.add_argument("-pinfo", "--playlist_info", dest="pinfo", nargs='+', type = str,
                    help="""playlist info. format:ar_l ar_r rank_l rank_r. can accept multiple sets.
                    example:0 98.0 11.3 11.7 98.0 100 11.9 12.7""",
                    default=["0", "98.0", "11.3", "11.7", "98.0", "100", "11.9", "12.7"])
args = parser.parse_args()

import re
def toint(mstr) -> int:
    m = re.search(r"([0-9]+)\.([0-9]+)", mstr)
    return int(m.group(1)) * 100 + int(m.group(2))

if args.analyze:
    from analyzer import analyze, tostr
    n = len(args.ainfo)
    assert n % 3 == 0, "wrong number of args in ainfo"
    for i in range(0, n - 1, 3):
        minar, rankl, rankr = float(args.ainfo[i]), toint(args.ainfo[i + 1]), toint(args.ainfo[i + 2])
        name = "minar{}_rank[{},{}]".format(minar, rankl, rankr)
        analyze(fumens, minar, rankl, rankr, name)

if args.playlist:
    from playlist import createList, printList
    n = len(args.pinfo)
    assert n % 4 == 0, "wrong number of args in pinfo"
    diffl, diffr, arl, arr = [], [], [], []
    for i in range(0, n - 1, 4):
        arl.append(float(args.pinfo[i])), arr.append(float(args.pinfo[i + 1]))
        diffl.append(toint(args.pinfo[i + 2])), diffr.append(toint(args.pinfo[i + 3]))

    content = ""
    for l, r, lar, rar in zip(diffl, diffr, arl, arr):
        idlist = []
        for fid in fumens:
            nf:fumen = fumens[fid]
            for i, rank, ar in zip(nf.pc, nf.rank, nf.ar):
                if rank >= l and rank <= r and ar * 100 >= lar and ar * 100 <= rar:
                    idlist.append(fid)
        name = "diff[{},{}] AR[{},{}]".format(tostr(l), tostr(r), lar, rar)
        content = createList(name, idlist, content)
    printList(content)