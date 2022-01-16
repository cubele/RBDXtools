RBDX score analyzer

## 使用方式
将ScoreData文件放到score目录下，运行`python parse.py`。
## SPECIAL铺面
大多数SPECIAL谱面编号为原谱面+1，但特殊方式解锁或SPECIAL PACK中的谱面可能不是，需要在网站上查询后手动写入编号。

已经写入了除了ouroboros -twin stroke of the end-的SP谱面以外（因为我没解锁😭）的所有编号。
## fumen.csv
如果需要更新谱面列表，需要对下载的csv作以下修改（这里的版本已经修改完毕）：

为了顺利读入csv数据，所有曲名与曲师名中含有字符","的需要替换为中文"，"。

732行曲目Megaera的SP谱面处写了谱师，但这歌没SP谱。

774行曲目The star in eclipse黄谱等级少了一个"-"。