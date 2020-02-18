import glob
import os

# test whether glob gives sorted files
file_list = list(glob.glob('/home/ec2-user/data/raw/BITMEX-ETHUSD-TRADES.csv.201*'))

print(sorted(file_list))