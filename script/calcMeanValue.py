import pandas as pd
from month2Day import calcDay
import os
import numpy as np
workdir  = '../pair_data_u_v2'
def calcMeanData(data):
    if (len(data) ==1):
        return data[0],0,1
    std = data.std()
    mean = data.mean()
    low_bound = mean - 3*std
    high_bound = mean + 3*std
    filtered_data = data[ (data >= low_bound) & (data <= high_bound)]
    if (len(filtered_data) < len(data)):
        return calcMeanData(filtered_data)
    else:
        return mean, std, len(data)

for filename in os.listdir(workdir):
    dateOne, dateTwo = filename.split('__')
    #获取日期
    dateOne = dateOne[-10:]
    dateTwo = dateTwo[0:10]
    #读取计算的数据
    column_names = ['data_file', 'delay_time', 'magnitude_rate', 'cc']
    f = pd.read_csv(os.path.join(workdir, filename), header=None, names=column_names)
    delay_time_data = f['delay_time']
    mag_rate_data = f['magnitude_rate']
    #去掉0值，0取对数为无穷
    mag_rate_data = mag_rate_data.replace(0.00, np.nan)
    mag_rate_data = mag_rate_data.dropna()
    #将比值转为对数比值
    mag_rate_data = np.log10(mag_rate_data)
    mean_time, std_time, num1 = calcMeanData(delay_time_data)
    mean_magRate, std_magRate, num2 = calcMeanData(mag_rate_data)
    #转换为PairID
    Day1 = calcDay(int(dateOne.split('_')[0]), int(dateOne.split('_')[1]), int(dateOne.split('_')[2]))
    Day2 = calcDay(int(dateTwo.split('_')[0]), int(dateTwo.split('_')[1]), int(dateTwo.split('_')[2]))
    pairId1 = str(dateOne.split('_')[0]) + str(f'{Day1:03d}')
    pairId2 = str(dateTwo.split('_')[0]) + str(f'{Day2:03d}')
    print(f"{pairId1+'_'+pairId2}, {mean_time:.3f},{std_time:.3f}, {num1}, {mean_magRate:.3f},{std_magRate:.3f}, {num2}")
