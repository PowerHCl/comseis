import pandas as pd
from month2Day import calcDay
import os
import numpy as np
f = pd.read_csv('../comseis.csv')
for i in range(len(f)):
    dateTime = f['time'][i].split('T')[0]
    Day = calcDay(int(dateTime.split('-')[0]), int(dateTime.split('-')[1]), int(dateTime.split('-')[2]))
    pairId = str(dateTime.split('-')[0]) + str(f'{Day:03d}')
    magnitude = f[' magnitude'][i]
    if i%2 == 0:
        tmpPairId = pairId
        tmpMagnitude = magnitude
        continue
    print(f"{tmpPairId+'_'+pairId}, {(tmpMagnitude - magnitude):0.1f}")
    
    