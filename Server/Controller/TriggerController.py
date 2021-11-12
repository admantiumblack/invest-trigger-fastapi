### Package Import ###
from fastapi import Request
### AppCode Import ###
from Server.Schema.TriggerSchema import TriggerSchemaDTO
import Server.Model.TriggerModel as tm
import Server.Controller.IndicatorController as indicator
########################################################
def get_triggers(request: Request):
    try:
        if request.cookies.get('Authorization') is None:
            return 'login to get user triggers'
    except:
        return 'login to get user triggers'
    
    resultSet = None
    try:
        resultSet =  tm.get_user_triggers(
            request.cookies.get('Authorization'))
    except:
        return 'request failed'
    triggerList = []
    for i in resultSet:
        trigger = {
            'signalId': i[0],
            'pair': i[2],
            'timeFrame': i[3],
            'indicator1': i[4],
            'indicatorVar1':i[5],
            'comparator': i[6],
            'indicator2': i[7],
            'indicatorVar2': i[8]
        }
        triggerList.append(trigger)
    return triggerList
########################################################
def delete_triggers(request:Request, triggerId):
    userId = request.cookies.get('Authorization')
    try:
        if userId is None:
            return 'login to delete user triggers'
    except:
        return 'login to delete user triggers'

    res = ''
    try:
        res = tm.delete_trigger(userId, triggerId)
    except:
        return 'delete failed'
    return res
########################################################
def validate_trigger(trigger:TriggerSchemaDTO):
    if trigger.indicator1 == 'price' \
        and trigger.indicatorVar1 is not None \
        and trigger.indicatorVar2 is None:
        return False
    
    isNotIndicator1 = (not hasattr(indicator, trigger.indicator1)
    and trigger.indicator1 != 'price')

    isNotIndicator2 = (trigger.indicator2 is not None 
    and not hasattr(indicator, trigger.indicator2))

    if isNotIndicator1 and isNotIndicator2:
        return False

    if trigger.comparator not in ['>', '<', '<=', '>=', '=']:
        return False
    if trigger.timeframe not in ['30m', '1h', '2h', '4h', '6h', '8h', '12h']:
        return False
    return True
    
def insert_triggers(request:Request, trigger:TriggerSchemaDTO):
    userId = request.cookies.get('Authorization')
    try:
        if userId is None:
            return 'login to delete user triggers'
    except:
        return 'login to delete user triggers'

    isValidTrigger = validate_trigger(trigger)
    if not isValidTrigger:
        return 'trigger not valid'

    triggerDict = vars(trigger)
    triggerDict['userId'] = userId

    try:
        triggerDict = {k: v for k, v in triggerDict.items() if v is not None}
        print(triggerDict)
        tm.insert_trigger(triggerDict)
    except:
        return 'insert failed'
    return 'insert success'
##############################################################################
