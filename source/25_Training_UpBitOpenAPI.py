import pyupbit
print(pyupbit.Upbit)

Ticker_BitcoinKRW = "KRW-BTC"
Ticker_RippleKRW = "KRW-XRP"
Ticker_RippleBTC = "BTC-XRP"

# 티커 종류 불러오기
tickers = pyupbit.get_tickers()
print(tickers)



# 거래 시장 종류별로 티커 불러오기
# 거래 시장은 KRW = 원화, BTC, ETH, USDT등이 있음
tickers = pyupbit.get_tickers(fiat="KRW")
print(tickers)



# 현재가 조회
btcPrice = pyupbit.get_current_price(Ticker_BitcoinKRW)
print(btcPrice)

btcPrice = pyupbit.get_current_price([Ticker_RippleKRW, Ticker_RippleBTC])
print(btcPrice)



# 과거 데이터 조회
# 1일마다
btcPrice = pyupbit.get_ohlcv(Ticker_BitcoinKRW)
print(btcPrice)

# 1분마다
btcPrice = pyupbit.get_ohlcv(Ticker_BitcoinKRW, interval="minute1")
print(btcPrice)

# 최근 5일간의 데이터만
btcPrice = pyupbit.get_ohlcv(Ticker_BitcoinKRW, count = 5)
print(btcPrice)



# 10호가 조회
orderbook_KRWBTC = pyupbit.get_orderbook(Ticker_BitcoinKRW)
orderbookUnits = orderbook_KRWBTC["orderbook_units"]

# bid_price = 매수 호가
# ask_price = 매도 호가
for orderbookUnit in orderbookUnits:
    print("매수호가 : %d , 매도호가 : %d" % (orderbookUnit["bid_price"], orderbookUnit["ask_price"]))



# 잔고 조회
# access_key = ""
# secret_key = ""

# upbit = pyupbit.Upbit(access_key, secret_key)
# print(upbit.get_balances())