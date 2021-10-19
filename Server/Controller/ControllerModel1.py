### Package Import ###
import time
import numpy as np
from Server.Model.BaseModel import BaseModelDTO
### AppCode Import ###


###############################################################################

async def Model1Predict(parameter:BaseModelDTO):
    ## preprocess, predict, insert
    
    print(parameter.Parameter1)
    print(parameter.Parameter4)
    
    return f'the data is inserted'

###############################################################################



###############################################################################