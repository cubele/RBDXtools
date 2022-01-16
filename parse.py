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
from fumen import fumen, loadAll
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

from analyzer import analyze
analyze(fumens)