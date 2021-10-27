### Package Import ###
from fastapi import Request
### AppCode Import ###
from Server.Schema.TriggerSchema import TriggerSchemaDTO
import Server.Model.TriggerModel as tm
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
            'timeFrame': i[2],
            'indicator1': i[3],
            'indicatorVar1':i[4],
            'comparator': i[5],
            'indicator2': i[6],
            'indivatorVar2': i[7]
        }
        triggerList.append(trigger)
    return triggerList
