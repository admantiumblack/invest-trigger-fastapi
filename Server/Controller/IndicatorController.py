import pandas_ta as pdt


def moving_average(prices, period, limit):
    res = pdt.sma(prices['prices'], period)
    return res.iloc[-limit:].to_numpy()


def exponential_moving_average(prices, period):
    pass