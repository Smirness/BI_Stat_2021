#### 1
from zipfile import ZipFile
import pandas as pd

file = "C:/Users/Viktor/BI_Stat_2022/olimpic_games/data/athlete_events.zip"
# # opening the zip file in READ mode
# with ZipFile(file, 'r') as zip:
#     for i in range(12):
#         if i < 10:
#             i = '0' + str(i)
#             with zip.open("athlete_events%s.csv" % str(i)) as file_i:
#                 # read the dataset
#                 file_i = pd.read_csv(file_i)
#                 print(file_i.shape)
#         else:
#             with zip.open("athlete_events%s.csv" % str(i)) as file_i:
#                 # read the dataset
#                 file_i = pd.read_csv(file_i)
#                 print(file_i.shape)

# 22836 + 22587 + 22558 + 22660 + 22602 + 22643 + 22665 + 22782 + 22517 +22410 + 22464 + 22391


file = "C:/Users/Viktor/BI_Stat_2021/olimpic_games/data/athlete_events.zip"
# opening the zip file in READ mode
with ZipFile(file, 'r') as zip:
    print(zip)
### 2
# zipfile = "C:/Users/Viktor/BI_Stat_2021/olimpic_games/data/athlete_events.zip"
# path = zipfile.split(sep="/")
# path = '/'.join(map(str, path[:-1]))
# print(path)
