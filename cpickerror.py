from obspy import read
import numpy as np
from scipy.signal import find_peaks
import sys
import matplotlib.pyplot as plt
def signalsearch(data1,data2):
    y1=np.linalg.norm(data1,2)
    y2=np.linalg.norm(data2,2)
    return y2/y1
args=sys.argv[1:]
    
f=args[0]
t=args[-1]
st=read(f)[0]
delta=st.stats.sac.delta
b=st.stats.sac.b
if t=='t0':
    tp=st.stats.sac.t0
elif t=='t1':
    tp=st.stats.sac.t1
elif t=='t2':
    tp=st.stats.sac.t2
elif t=='t3':
    tp=st.stats.sac.t3
elif t=='t4':
    tp=st.stats.sac.t4
elif t=='t5':
    tp=st.stats.sac.t5
elif t=='t6':
    tp=st.stats.sac.t6
elif t=='t7':
    tp=st.stats.sac.t7
elif t=='t8':
    tp=st.stats.sac.t8
elif t=='t9':
    tp=st.stats.sac.t9
else :
    print('parameter wrong!')
    exit()

delta=round(delta,3)
tpN=round((tp-b)/delta)

#we use 2 second for search segment
L=round(2/delta)
#full length (10s)
fL=round(10/delta)
#errors 
le=round(0.5/delta)
#test
# data1=st.data[tpN-L:tpN]
# data2=st.data[tpN:tpN+L]
# print(signalsearch(data1,data2))

# data1=st.data[tpN+le-L:tpN+le]
# data2=st.data[tpN+le:tpN+L+le]
# print(signalsearch(data1,data2))

# data=st.data[tpN-fL:tpN+fL]
# plt.show()
# data1=st.data[tpN-L+1:tpN+1]
# plt.plot(data1)
# plt.show()
# data2=st.data[tpN+1:tpN+L+1]
# plt.plot(data2)
# plt.show()
# print(signalsearch(data1,data2))


lst1=[]
if (tpN-fL-L)<0:
    for i in range(L,tpN+fL+le,le):
        data1=st.data[i-L+1:i+1]
        data2=st.data[i+1:i+L+1]
        lst1.append(signalsearch(data1,data2))

    tmp,_ =find_peaks(np.array(lst1),height=max(np.array(lst1))*0.6)
    if (len(tmp)!=0):
        num=tmp[-1]
    else:
        num=1
    dT=(L+1+num*le-tpN)*delta
elif (tpN+fL+L)>len(st.data)-1:
    for i in range(tpN-fL,len(st.data)-L-1,le):
        data1=st.data[i-L+1:i+1]
        data2=st.data[i+1:i+L+1]
        lst1.append(signalsearch(data1,data2))

    num=np.argmax(np.array(lst1))
    tmp,_ =find_peaks(np.array(lst1),height=max(np.array(lst1))*0.6)
    if (len(tmp)!=0):
        num=tmp[-1]
    else:
        num=len(lst1)-2
    dT=((num-len(lst1)+1)*le+len(st.data)-L-1-tpN)*delta  
else:
    for i in range(tpN-fL,tpN+fL+le,le):
        data1=st.data[i-L+1:i+1]
        data2=st.data[i+1:i+L+1]
        lst1.append(signalsearch(data1,data2))
    num=np.argmax(np.array(lst1))

    if (num==40):
        tmp,_ =find_peaks(np.array(lst1),height=max(np.array(lst1))*0.6)
        if (len(tmp)!=0):
            num=tmp[-1]
        else:
            num=40
            print("out of expect!")
            exit()
    if (num<40):
        while True:
            if (np.array(lst1)[num+1]/np.array(lst1)[num]>0.95):
                num+=1
            else:
                break
    dT=num*0.5-10.
# plt.plot(lst1)
# plt.show()
# print(np.argmax(np.array(lst1)))
# print(max(np.array(lst1)))
# print(tp+dT)
dn=round(dT/delta)
lst2=[]
for j in range(tpN+dn-le,tpN+dn+le+1):
    data1=st.data[j+1-L:j+1]
    data2=st.data[j+1:j+L+1]
    lst2.append(signalsearch(data1,data2))
ans,_ =find_peaks(np.array(lst2),height=max(np.array(lst2))*0.8)
if (len(ans)!=0):
    Xn=ans[-1]+tpN+dn-le
else:
    Xn=np.argmax(np.array(lst2))+tpN+dn-le
# plt.plot(lst2)
# plt.show()
print(round(Xn*delta+b,3))