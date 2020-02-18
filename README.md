# trades_2_OHLC_prices


ec2-user@34.248.41.122, yes.

thats where the data that need to be reformatted is, you can take a look at a few of the TRADE files, I will need those converted into 1min timestamps of the price, and probably other timeframes too, for OKex Quarterly and others. Dont do too much yet just maybe see if you can do it for one file and Ill let you know which ones I need it for


this is an example file

thats tick by tick data, but I need to have the price recorded for each 1min interval instead. There is also occasionaly stale data in those files I believe. Anyway ill give you more detailed instructions a bit later

## Ok so I need the following: 

for OKex: 
OKEX-BTC-THIS-WEEK 
OKEX-BTC-QUARTER 
OKEX-BTC-SWAP 

same for ETH, LTC, EOS, XRP, BCH 

For Bitmex: 

XBTUSD, ETHUSD 

The TRADES files converted from tick-data to: 

1min OHLC 
3min OHLC 
5min OHLC
15min OHLC 
30min OHLC 
1h OHLC 
4h OHLC 
12h OHLC 
1D OHLC  

Ideally as far back as we have data for. 
Id like for the 1min up to 5min files to be split into 1 excel file per week 
15min to 1H into 1 excel file per month 
4H+ into one single file 

One instrument per file 

Please make the format uniform so I can VLOOKUP for values to other files in excel 

im not sure how long this takes and which tasks are longer than others so please give me an estimate and if any requests take too long let me know so i can change the specifications. Please send me an example file once you have one ready so we can make sure it seems fine before doing everything else