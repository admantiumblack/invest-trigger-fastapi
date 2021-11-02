### Package Import ###
from binance.client import Client
import os
import pandas as pd
import numpy as np
### AppCode Import ###
from Server.Model.TriggerModel import get_all_triggers
import Server.Controller.IndicatorController as indicator
from Server.ScheduledJobs.EmailSender import EmailSender
###############################################################################
def calculate_indicator(indicator_type, pair, parameter, indicatorDict, priceDict):
    if indicatorDict.get(pair + indicator_type + str(parameter)) is not None:
        return indicatorDict.get(pair + indicator_type + str(parameter))
    return getattr(indicator, indicator_type)(priceDict[pair], parameter, 2)
    
###############################################################################
def get_price(pair, timeframe, client, priceDict):
    if priceDict.get(pair) is not None:
        return priceDict.get(pair)  

    prices = client.get_klines(symbol = pair, interval=timeframe, limit=300)
    prices = [i[4] for i in prices]
    priceDf = pd.DataFrame({'prices':prices}, dtype='float32')
    return priceDf
###############################################################################
def compare(param1, comparator, param2, idx = 0, limit = 1):
    print(param1, param2)
    if comparator == '>':
        return param1[idx] > param2[idx] and \
            not (param1[idx+1:idx+1+limit] > param2[idx+1:idx+1+limit]).any()
    elif comparator == '<':
        return param1[idx] < param2[idx] and \
            not (param1[idx+1:idx+1+limit] < param2[idx+1:idx+1+limit]).any()
    elif comparator == '>=':
        return param1[idx] >= param2[idx] and \
            not (param1[idx+1:idx+1+limit] >= param2[idx+1:idx+1+limit]).any()
    elif comparator == '<=':
        return param1[idx] <= param2[idx] and \
            not (param1[idx+1:idx+1+limit] <= param2[idx+1:idx+1+limit]).any()
###############################################################################
def check_trigger():
    apiKey = os.environ.get('API_KEY')
    apiSecret = os.environ.get('API_SECRET')
    res = get_all_triggers()
    indicatorRes = {}
    pairPrice = {}
    emailClient = EmailSender()
    client = Client(apiKey, apiSecret, {"verify": False, "timeout": 20})
    for i in res:
        flag = False
        var1 = None
        var2 = None
        email = i[0]
        pair = i[1]
        timeframe = i[2]
        indicator1 = i[3]
        indicatorVar1 = i[4]
        comparator = i[5]
        indicator2 = i[6]
        indicatorVar2 = i[7]
        pairPrice[pair] = get_price(pair, timeframe, client, pairPrice)
        if indicator1 == 'price' and indicator2 not in [None, 'price']:
            print(indicator1, indicator2)
            indicatorRes[pair + indicator2 + str(indicatorVar2)] = calculate_indicator(
                indicator2, pair, indicatorVar2, indicatorRes, pairPrice)
            print(indicatorRes[pair + indicator2 + str(indicatorVar2)])
            print(pair + indicator2 + str(indicatorVar2))
            var1 = pairPrice[pair].iloc[-2:, 0].to_numpy()
            var2 = indicatorRes[pair + indicator2 + str(indicatorVar2)]

        elif indicator1 == 'price' and indicator2 is None:
            # pairPrice[pair].iloc[-1, 0]
            var1 = np.full(shape=2, fill_value=indicatorVar2)
            var2 = pairPrice[pair].iloc[-2:, 0].to_numpy()
        else:
            indicatorRes[pair + indicator1 + str(indicatorVar1)] = \
                calculate_indicator(indicator1, pair, indicatorVar1, indicatorRes, 
                pairPrice)
            indicatorRes[pair + indicator2 + str(indicatorVar2)] = \
                calculate_indicator(indicator2, pair, indicatorVar2, indicatorRes, 
                pairPrice)
            
            var1 = indicatorRes[pair + indicator1 + str(indicatorVar1)]
            var2 = indicatorRes[pair + indicator1 + str(indicatorVar1)]
        flag = compare(var1, comparator, var2, limit=2)
        if flag:
            emailClient.send_email(email, pair, timeframe, 
            f'{indicator1}-{indicatorVar1}', comparator, 
            f'{indicator2}-{indicatorVar2}')
        
