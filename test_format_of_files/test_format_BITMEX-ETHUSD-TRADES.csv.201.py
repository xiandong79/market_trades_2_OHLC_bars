import pandas as pd
import glob
import os

# df = pd.read_csv('/home/ec2-user/data/raw/BITMEX-ETHUSD-TRADES.csv.2018-09-07.gz', 
#                 compression='gzip',
#                 )
# print(df.head())

#    1536278424973  1536278424819  e93cc9ef-5ee6-16a4-1ac2-4934650381de  BID   229.2  18.468586387434556
# 0  1536278429425  1536278428924  939ce395-ca38-203c-2126-adfde9ffdf7d  BID  229.20            1.343805
# 1  1536278432040  1536278431320  374b0cfb-1a91-df20-c888-15795a96288c  BID  229.20          228.621291
# 2  1536278432382  1536278431531  e85a20fb-f410-8767-381d-08f42876aed1  BID  229.20            6.212914
# 3  1536278433048  1536278431832  6d0a67d4-5424-5867-1d55-e95a0a91dd93  ASK  229.25            1.744820
# 4  1536278434608  1536278433167  eb0c3aeb-f67f-1a30-6c44-5bdfe50c75e7  ASK  229.25            0.043621

df = pd.read_csv('/home/ec2-user/data/raw/BITMEX-ETHUSD-TRADES.csv.2019-11-12.gz', 
                compression='gzip',
                )
print(df.head())