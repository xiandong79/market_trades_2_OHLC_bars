import pandas as pd
import os

data_frame = pd.read_csv('/Users/dong/Desktop/NBP/trades_2_OHLC_prices/data_examples/BITMEX-ETHUSD-TRADES.csv', 
                        names=['time', 'ex_time', 'order_id', 'direction', 'price', 'volume', 'not_known', 'date'], 
                        index_col=7,
                        parse_dates=True)

data_frame = data_frame[['price']]

print(data_frame.head())

freq_list = ['1min', '3min', '5min', '15min', '30min', '60min']
for freq in freq_list:
    data_ohlc = data_frame['price'].resample(freq).ohlc()
    print(data_ohlc.head())
    data_ohlc.to_csv(os.getcwd()+f"/example_file_{freq}.csv")