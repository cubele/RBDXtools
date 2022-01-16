RBDX score analyzer

## 使用方式
新建文件夹score，将三个ScoreData文件（从RB中导出）放到score目录下，运行`python parse.py`。

## 参数
默认画11级以上，AR >= 96.9%的数据，可以通过更改`analyzer.py`改变。

## SPECIAL铺面
大多数SPECIAL谱面编号为原谱面+1，但特殊方式解锁或SPECIAL PACK中的谱面可能不是，需要在网站上查询后手动写入编号。

已经写入了除了ouroboros -twin stroke of the end-的SP谱面以外（因为我没解锁😭）的所有编号。
## fumen.csv
如果需要更新谱面列表，需要对下载的csv作以下修改（这里的版本已经修改完毕）：

为了顺利读入csv数据，所有曲名与曲师名中含有字符","的需要替换为中文"，"。

732行曲目Megaera的SP谱面处写了谱师，但这歌没SP谱。

774行曲目The star in eclipse黄谱等级少了一个"-"。