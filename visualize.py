import pandas as pd
import sys

assignment_file = "/Users/takedakiyoshi/lab/kline/KLINE/4月のミーティング向けの資料/exp_assignment.xlsx"
leftrt_file = "/Users/takedakiyoshi/lab/kline/KLINE/4月のミーティング向けの資料/exp_leftRT.xlsx"

assignment = pd.read_excel(assignment_file)
Ldict = {}
for row in assignment.itertuples():
    if row[1] not in Ldict:
        Ldict[row[1]] = {}
        Ldict[row[1]][row[6]] = float(row[8])
    else:
        if row[6] in Ldict[row[1]]:
            Ldict[row[1]][row[6]] += float(row[8])
        else:
            Ldict[row[1]][row[6]] = float(row[8])

leftRT = pd.read_excel(leftrt_file)
for row in leftRT.itertuples():
    if row[1] in Ldict:
        Ldict[row[1]]["left"] = row[2]
    else:
        Ldict[row[1]] = {}
        Ldict[row[1]]["left"] = row[2]

for k, v in Ldict.items():
    # print(k, v)
    tmpDict = v
