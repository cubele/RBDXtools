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

from playlist import createList, printList

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

import re
def toint(mstr) -> int:
    m = re.search(r"([0-9]+)\.([0-9]+)", mstr)
    return int(m.group(1)) * 100 + int(m.group(2))

print("请确保score目录下已经放置了ScoreData文件")
from analyzer import analyze, tostr
while True:
    instr = input("""输入希望分析的数据区间，格式：最小AR 最小档位 最大档位。
用空格隔开并以换行结尾，例如96.0 11.6 12.6
输入jiquan结束分析。
""")
    if instr == "jiquan":
        break
    print("analyzing...")
    ainfo = instr.split()
    if len(ainfo) != 3:
        print("输入格式有误")
        continue
    minar, rankl, rankr = float(ainfo[0]), toint(ainfo[1]), toint(ainfo[2])
    name = "minar{}_rank[{},{}]".format(minar, rankl, rankr)
    analyze(fumens, minar, rankl, rankr, name)

arl, arr, diffl, diffr = [], [], [], []
while True:
    instr = input("""输入希望创建playlist的数据区间，格式：最小AR 最大AR 最小档位 最大档位。
以换行结尾，例如0 98.0 11.2 14.1
输入jiquan结束输入并生成包含所有输入区间的playlist。
""")
    if instr == "jiquan":
        break
    pinfo = instr.split()
    if len(pinfo) != 4:
        print("输入格式有误")
        continue
    arl.append(float(pinfo[0])), arr.append(float(pinfo[1]))
    diffl.append(toint(pinfo[2])), diffr.append(toint(pinfo[3]))

from playlist import createList, printList
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
print("生成完毕！结果存放在在output目录下")