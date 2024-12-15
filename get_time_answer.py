import numpy as np
import os
import pandas as pd
file_path = "pair_data_u"
filenames = os.listdir(file_path)
k = 2
datalst = [] #save end data
for filename in filenames:
    data_o = pd.read_csv(os.path.join(file_path,filename),header=None)
    data = data_o.iloc[:,1]
    if (data.shape[0] == 1):
        datalst.append(abs(data.mean()))
        continue
    mean_value = data.mean()
    std_dev = data.std()
    data_select = data[(data >= (mean_value - k * std_dev)) & (data <= (mean_value + k * std_dev))]
    datalst.append(abs(data_select.mean()))
print(len(datalst))
# np.savetxt("ans.txt",datalst)


# data_o = pd.read_csv(os.path.join(file_path,"data_1991_11_17__2014_01_16.txt"),header = None)
# data = data_o.iloc[:,1]
# mean_value = data.mean()
# std_dev = data.std()
# print(std_dev)
# data_select = data[(data >= (mean_value - k * std_dev)) & (data <= (mean_value + k * std_dev))]
# datalst.append(abs(data_select.mean()))
# print(abs(data_select.mean()))