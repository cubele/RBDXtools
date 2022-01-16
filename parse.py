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

db = sqlite3.connect('./ScoreData.sqlite')
df = pd.read_sql_query("SELECT * FROM ZSCOREDATA", con=db)
flist = []
for i in df["ZTUNEID"]:
    flist.append(i)
flist.sort()
print(flist)

#for every fumen in csv query in db