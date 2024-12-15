#!/bin/python
#get the timelag and cc
from obspy.signal.cross_correlation import correlate
from obspy.signal.cross_correlation import xcorr_max
import sys
import numpy as np
from obspy import read
#caculate the rms rate
def getrmsrate(tr1,tr2,d,t1,t2,dt):
    n1=int(t1/d)
    n2=int(t2/d)
    n3=abs(int(dt/d))
    if dt <= 0:
        tr2=tr2[n1+n3:n2+n3]
        tr1=tr1[n1:n2]
    else:
        tr1=tr1[n1+n3:n2+n3]
        tr2=tr2[n1:n2]
    rms1=np.sqrt(np.mean(tr1**2))
    rms2=np.sqrt(np.mean(tr2**2))
    return rms1/rms2
# define the windows length
s=30.0
args=sys.argv[1:]
if len(args)!=3:
    print("parameter error!")
t=sys.argv[1]
f1=sys.argv[2]
f2=sys.argv[3]
st1=read(f1)[0]
st2=read(f2)[0]
d1=st1.stats.delta
d2=st2.stats.delta
d1=round(d1,3)
d2=round(d2,3)
d = d1
if d2>d1:
    st2.interpolate(sampling_rate = 1/d1)
    d=d1
elif d1>d2:
    st1.interpolate(sampling_rate = 1/d2)
    d=d2
ts1=st1.stats.starttime
ts2=st2.stats.starttime
b1=st1.stats.sac.b
b2=st2.stats.sac.b
if t=='t0':
    tp1=st1.stats.sac.t0
    tp2=st2.stats.sac.t0
elif t=='t1':
    tp1=st1.stats.sac.t1
    tp2=st2.stats.sac.t1
elif t=='t2':
    tp1=st1.stats.sac.t2
    tp2=st2.stats.sac.t2
elif t=='t3':
    tp1=st1.stats.sac.t3
    tp2=st2.stats.sac.t3  
elif t=='t4':
    tp1=st1.stats.sac.t4
    tp2=st2.stats.sac.t4  
elif t=='t5':
    tp1=st1.stats.sac.t5
    tp2=st2.stats.sac.t5
elif t=='t6':
    tp1=st1.stats.sac.t6
    tp2=st2.stats.sac.t6
elif t=='t7':
    tp1=st1.stats.sac.t7
    tp2=st2.stats.sac.t7
elif t=='t8':
    tp1=st1.stats.sac.t8
    tp2=st2.stats.sac.t8  
elif t=='t9':
    tp1=st1.stats.sac.t9
    tp2=st2.stats.sac.t9
else :
    print('parameter wrong!')
    exit()

st11=st1.copy().trim(ts1+tp1-b1,ts1+tp1+s-b1)
st22=st2.copy().trim(ts2+tp2-b2,ts2+tp2+s-b2)

#define max timelag second
maxlags = 25.0
maxlagn=int(maxlags/d)

def cc(tr1,tr2,maxlagn):
    cc=correlate(tr1,tr2,maxlagn)
    timelag, value= xcorr_max(cc,abs_max=False)
    tlag=timelag*d+tp1-tp2
    tlag=round(tlag,3)
    value=round(value,3)
    return value,tlag,timelag
value,tlag,timelag=cc(st11.data,st22.data,maxlagn)

if value >0.5 and value <0.95 and abs(timelag*d) >= 3:
    # print(ts2+tp2-b2+abs(timelag*d), ts2+tp2+s-b2+abs(timelag*d))
    if timelag<=0:
        st22=st2.copy().trim(ts2+tp2-b2+abs(timelag*d),ts2+tp2+s-b2+abs(timelag*d))
    else:
        st11=st1.copy().trim(ts1+tp1-b1+timelag*d,ts1+tp1+s-b1+timelag*d)
    value, _, lag =cc(st11.data,st22.data,maxlagn)
    tlag += lag*d
    timelag += lag
rms=round(getrmsrate(st11.data,st22.data,d,0,10,timelag*d),3)
station=f1.split("/")[-1]
print("{0},{1:.3f},{2:.3f},{3:.3f}".format(station,tlag,rms,value))
