import pandas as pd
import glob
import os

# df = pd.read_csv('/home/ec2-user/data/raw/OKEX-BTC-THIS-WEEK-TRADES.csv.2018-09-07.gz', 
#                 compression='gzip',
#                 )
# print(df.head())

#    1536278411140  0  1411803432779778  BID  6484.75    6.0
# 0  1536278417993  0  1411803879014401  ASK  6482.30   28.0
# 1  1536278425862  0  1411804380364826  BID  6483.06   10.0
# 2  1536278425862  0  1411804394520587  ASK  6482.30  156.0
# 3  1536278426345  0  1411804436398086  ASK  6480.83   16.0
# 4  1536278426345  0  1411804436398088  ASK  6480.82   18.0

# df = pd.read_csv('/home/ec2-user/data/raw/OKEX-BTC-THIS-WEEK-TRADES.csv.2019-02-08.gz', 
#                 compression='gzip',
#                 )
# print(df.head())

#    1549584036205  0  2283800873500675  BID  3361.99  16.0
# 0  1549584057687  0  2283802292944917  ASK  3361.98   4.0
# 1  1549584057687  0  2283802292944919  ASK  3361.98   4.0
# 2  1549584057688  0  2283802292944921  ASK  3361.88   2.0
# 3  1549584057688  0  2283802292944923  ASK  3361.88   2.0
# 4  1549584057688  0  2283802292944925  ASK  3361.87   4.0

# df = pd.read_csv('/home/ec2-user/data/raw/OKEX-BTC-THIS-WEEK-TRADES.csv.2019-05-19.gz', 
#                 compression='gzip',
#                 )
# print(df.head())

#    1558224001087  0  2850029620264967  BID  7274.08   5.0
# 0  1558224001087  0  2850029620264969  BID  7274.08  10.0
# 1  1558224001087  0  2850029620264971  BID  7274.08   5.0
# 2  1558224001379  0  2850029631078410  BID  7274.08  10.0
# 3  1558224001379  0  2850029631078412  BID  7274.08  20.0
# 4  1558224001379  0  2850029645234183  ASK  7274.07  45.0

# df = pd.read_csv('/home/ec2-user/data/raw/OKEX-BTC-THIS-WEEK-TRADES.csv.2019-11-16.gz', 
#                 compression='gzip',
#                 )
# print(df.head())

#    1573862401104  0  363196  BID  8478.53  0.22409545050851973
# 0  1573862401689  0  363197  BID  8478.54             0.672286
# 1  1573862401708  0  363198  BID  8478.54             1.167654
# 2  1573862401708  0  363199  BID  8478.54             0.837408
# 3  1573862402225  0  363200  ASK  8478.79             0.106147
# 4  1573862402260  0  363201  ASK  8478.79             0.070765