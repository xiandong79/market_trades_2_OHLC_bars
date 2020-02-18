import pandas as pd
import glob
import os

store_freq_dict = {
    'M': ['15min', '30min', '60min'],
    'W': ['1min', '3min', '5min'],
    # 'one_file': ['4h', '12h', '1D']
}

exchange_contract_types = {
    'OKEX': ['THIS-WEEK', 'QUARTER', 'SWAP'],
    'BITMEX': ['default']
}

global_start = '2018-01-01'
global_end = '2020-01-01'

for store_freq, freq_list in store_freq_dict.items():
    if store_freq in ['M', 'W']:
        date_list = pd.date_range(start=global_start, end=global_end, freq=store_freq, closed=None).to_list()
        paired_date_list = list(zip(date_list, date_list[1:]))
    else:
        # store the data from global_start to global_end into 'one_file'
        paired_date_list = [(pd.to_datetime(global_start), pd.to_datetime(global_end))]

    for exchange in ['OKEX', 'BITMEX']:
        for coin in ['BTC', 'ETH', 'LTC', 'EOS', 'XRP', 'BCH', 'XBTUSD', 'ETHUSD']:
            for contract in exchange_contract_types.get(exchange, []):
                for start_date, end_date in paired_date_list:
                    if exchange == 'OKEX':
                        input_file_pattern = f"/home/ec2-user/data/raw/{exchange}-{coin}-{contract}-TRADES.csv.201*.gz"
                    else:
                        input_file_pattern = f"/home/ec2-user/data/raw/{exchange}-{coin}-TRADES.csv.201*.gz"
                    # print(f"checking: input_file_pattern: {input_file_pattern.split('/')[-1]}, start_date: {start_date}")

                    df_list = []
                    for input_file in sorted(glob.glob(input_file_pattern)):
                        # change 2019-10-31 from str to date.date
                        file_date = input_file.split('.')[-2]
                        if pd.to_datetime(file_date) >= start_date and pd.to_datetime(file_date) < end_date:
                            df = pd.read_csv(input_file, 
                                            compression='gzip',
                                            names=['time', 'not_known', 'order_id', 'direction', 'price', 'volume'], 
                                            )
                            df['date'] = pd.to_datetime(df['time'], unit='ms')
                            df = df[['date', 'price']]
                            df_list.append(df)

                    if df_list:
                        concat_df = pd.concat(df_list)
                        concat_df = concat_df.set_index('date')
                        # print(concat_df.head())

                        for freq in freq_list:
                            data_ohlc = concat_df['price'].resample(freq).ohlc()
                            print(data_ohlc.head())
                            output_file_type = input_file.split('.')[0].split('/')[-1]
                            output_file_name = f"/home/ec2-user/data/ohlc_data/{output_file_type}_{freq}_{start_date.strftime('%Y-%m-%d')}.csv"
                            print(f"storing: {output_file_name.split('/')[-1]}")
                            data_ohlc.to_csv(output_file_name)