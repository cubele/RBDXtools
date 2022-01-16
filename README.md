# RBDXtools

## 功能
分数统计：可以对指定难度，AR区间的谱面作图显示AR分布，平均值与FC等信息。

Playlist生成：可以将指定难度区间的所有谱面根据本地最高AR所在区间进行划分，并为划分出的谱面生成一个可导入RBDX使用的playlist。

## 使用方式
在本目录下新建文件夹score与output，将三个ScoreData文件（从RB中导出ScoreData.sqlite, ScoreData.sqlite-shm, ScoreData.sqlite-wal）放到score目录下，安装python，进入本目录从命令行运行
```bash
pip install --user -r requirements.txt
python parse.py -a -p
```
即可用默认参数运行，更改参数的方法见下一节。

所有文件会输出到output文件夹中，分数统计以图片的方式输出，绿色点表示fc过的谱面。playlist输出为playlist文件，可以直接导入至RBDX进行覆盖。

注意生成的playlist中只包含你提供的参数对应数量的playlist，覆盖后原有的playlist会消失。如果要保留原来的playlist，请备份原来的playlist文件并手动操作playlist文件进行合并。

也可以直接在群里下载打包好的版本，在命令行中进入目录后直接运行
```bash
.\RBDXtools.exe -a -p
```
即可，修改参数的方式是一样的。

## 参数
格式为
```bash
python parse.py -a -ainfo minar rankl rankr -p -pinfo ar_l ar_r rank_l rank_r
```
`-ainfo minar rankl rankr`表示绘制$ar \ge minar, rank \in [rankl, rankr]$之间的所有数据。

`-pinfo ar_l ar_r rank_l rank_r`表示将$ar \in [ar_l, ar_r], rank \in [rank_l, rank_r]$之间的所有谱面放入一个playlist中。

ar的格式为一个$[0,100]$之间的浮点数，rank表示谱面档位，形式为等级.打架档位。这里?档与未打架完毕的谱面被处理为0档。

这两个参数都可以接受多组数据，例如运行
```bash
python parse.py -a -ainfo 98.0 11.3 12.5 95.0 10.0 11.1 -p -pinfo 0 98.0 11.3 11.7 98.0 100 11.9 12.7
```
表示绘制参数为`98.0 11.3 12.5`与`95.0 10.0 11.1`的两张图片，创建参数为`0 98.0 11.3 11.7`与`98.0 100 11.9 12.7`的两个playlist。

# 更新谱面列表时的注意事项
## SPECIAL谱面
大多数SPECIAL谱面编号为原谱面+1，但特殊方式解锁或SPECIAL PACK中的谱面可能不是，需要在网站上查询后手动写入编号。

已经写入了除了ouroboros -twin stroke of the end-的SP谱面以外（因为我没解锁😭）的所有编号。在更新时可能需要写入新的sp编号。
## fumen.csv
对csv作了以下修改：

为了顺利读入csv数据，所有曲名与曲师名中含有字符","的需要替换为中文"，"。

732行曲目Megaera的SP谱面处写了谱师，但这歌没SP谱。

774行曲目The star in eclipse黄谱等级少了一个"-"。