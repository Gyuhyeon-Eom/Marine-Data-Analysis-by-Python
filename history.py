
MODE = 1

## 첫번째 공간 주성분을 뽑아서 EOF 라는 변수에 저장 
EOF = np.reshape(eigen_vec[:,MODE-1], (len(lat_region), len(lon_region)))
print(EOF.shape)

## 첫번째 시간 주성분을 뽑아서 PC 라는 변수에 저장
PC = PCs[:,MODE-1]
print(PC.shape)

######################################################

###### Normalize eigenvector 
n_EOF = EOF * np.sqrt(s[MODE-1])

###### Normalize PC Time-series
n_PC = PC * np.sqrt(s[MODE-1])
PC.shape
EOF.shape
len(lat_region)
T2_month
T2_month.shape
T2_year.shape
for i in range(len(lat)):
    for j in range(len(lon)):
        t2 = T2_year[:,i,j]
        r = stats.linregress(n_PC,t2)
        beta = r.slope
        T2_beta[i,j] = beta
        
        if r.pvalue < 0.2:
            T2_sig[i,j] = 1
            
        else:
            T2_sig[i,j] = np.NAN
            
T2_beta_sig = T2_beta * T2_sig
T2_year_detrend = signal.detrend(T2_year,0) 

T2_beta = np.zeros((len(lat),len(lon)))
T2_sig = np.zeros(np.shape(T2_beta)) 

for i in range(len(lat)):
    for j in range(len(lon)):
        t2 = T2_year[:,i,j]
        r = stats.linregress(n_PC,t2)
        beta = r.slope
        T2_beta[i,j] = beta
        
        if r.pvalue < 0.2:
            T2_sig[i,j] = 1
            
        else:
            T2_sig[i,j] = np.NAN
            
T2_beta_sig = T2_beta * T2_sig
runfile('C:/Users/gheom/.spyder-py3/기말프로젝트_엄규현.py', wdir='C:/Users/gheom/.spyder-py3')
T2_beta_sig.shape
T2_beta.shape
T2_sig.shape
runfile('C:/Users/gheom/.spyder-py3/기말프로젝트_엄규현.py', wdir='C:/Users/gheom/.spyder-py3')
T2_year.shape
T2_month.shape
n_PC.shape
runfile('C:/Users/gheom/.spyder-py3/기말프로젝트_엄규현.py', wdir='C:/Users/gheom/.spyder-py3')
years.shape
runfile('C:/Users/gheom/.spyder-py3/기말프로젝트_엄규현.py', wdir='C:/Users/gheom/.spyder-py3')
PCs.shape
t2.shape
SST_month.shape
OEF
EOF.shape
eigen_vec
eigen_vec.shape
PCs.shape
PC.shape
runfile('C:/Users/gheom/.spyder-py3/기말프로젝트_엄규현.py', wdir='C:/Users/gheom/.spyder-py3')
len(SST_month)
len(T2_month)
runfile('C:/Users/gheom/.spyder-py3/기말프로젝트_엄규현.py', wdir='C:/Users/gheom/.spyder-py3')
len(lat_region)
len(SST_region_a)
len(lon_region)
runfile('C:/Users/gheom/.spyder-py3/기말프로젝트_엄규현.py', wdir='C:/Users/gheom/.spyder-py3')

## ---(Wed Dec  2 20:16:45 2020)---
runfile('C:/Users/gheom/.spyder-py3/기말프로젝트_엄규현.py', wdir='C:/Users/gheom/.spyder-py3')

## ---(Wed Dec  2 20:22:18 2020)---
runfile('C:/Users/gheom/.spyder-py3/기말프로젝트_엄규현.py', wdir='C:/Users/gheom/.spyder-py3')

## ---(Wed Dec  9 11:46:10 2020)---
runfile('C:/Users/gheom/.spyder-py3/open_SST_monthly_annAvg_wgtPlot.py', wdir='C:/Users/gheom/.spyder-py3')
len(lat)
len(lon)
SSTs = np.zeros([12*40, len(lat), len(lon)])
SSTs.shape
SSTs
runfile('C:/Users/gheom/.spyder-py3/untitled9.py', wdir='C:/Users/gheom/.spyder-py3')
runfile('C:/Users/gheom/.spyder-py3/open_SST_monthly_annAvg_wgtPlot.py', wdir='C:/Users/gheom/.spyder-py3')

## ---(Wed Dec 16 12:17:52 2020)---
runfile('C:/Users/gheom/.spyder-py3/open_SST_monthly_annAvg_wgtPlot.py', wdir='C:/Users/gheom/.spyder-py3')
runfile('C:/Users/gheom/.spyder-py3/Q01_use_List.py', wdir='C:/Users/gheom/.spyder-py3')
SST_year = np.zeros([40, len(lat), len(lon)])
SST_year = list(np.zeros([40, len(lat), len(lon)]))
SST_year
runfile('C:/Users/gheom/.spyder-py3/Q01_use_List.py', wdir='C:/Users/gheom/.spyder-py3')
SST_year = list(np.zeros([40, len(lat), len(lon)]))
SST_year.format
format(SST_year)
runfile('C:/Users/gheom/.spyder-py3/Q01_use_List.py', wdir='C:/Users/gheom/.spyder-py3')
runfile('C:/Users/gheom/.spyder-py3/Q02_use_Function.py', wdir='C:/Users/gheom/.spyder-py3')
def Cosine_wgt(x):
    cosarray = np.zeros((len(lat),len(lon))) 
    for x in range(0, len(lat)):
        cosarray[x,:]=np.cos(lat[x]*np.pi/180)
        
Cosine_wgt(15)
print(Cosine_wgt(15))
runfile('C:/Users/gheom/.spyder-py3/Q02_use_Function.py', wdir='C:/Users/gheom/.spyder-py3')
cosarray = np.zeros((len(lat),len(lon))) 
for x in range(0, len(lat)):
    cosarray[x,:]=np.cos(lat[x]*np.pi/180)
    
cosarray
cosarray.shape
cosarray = np.zeros((len(lat), len(lon)))

def Cosine_wgt(x):
    cosarray = np.zeros((len(lat),len(lon))) 
    for x in range(0, len(lat)):
        cosarray[x,:]=np.cos(lat[x]*np.pi/180)
        
    return x
    
cosarray.shape
Cosine_wgt(30)
cosarray = np.zeros((len(lat),len(lon))) 
for x in range(0, len(lat)):
    cosarray[x,:]=np.cos(lat[x]*np.pi/180)
    
runfile('C:/Users/gheom/.spyder-py3/Q02_use_Function.py', wdir='C:/Users/gheom/.spyder-py3')
idxNaN2d = (np.isnan(SST_year[0,:,:]) == True)
cosarray[idxNaN2d] = np.NaN
SST_year.shape
runfile('C:/Users/gheom/.spyder-py3/Q02_use_Function.py', wdir='C:/Users/gheom/.spyder-py3')
runfile('C:/Users/gheom/.spyder-py3/기말프로젝트_엄규현.py', wdir='C:/Users/gheom/.spyder-py3')
runfile('C:/Users/gheom/.spyder-py3/해양데이터분석_엄규현4.py', wdir='C:/Users/gheom/.spyder-py3')
runfile('C:/Users/gheom/.spyder-py3/Q03_use_LinRegress.py', wdir='C:/Users/gheom/.spyder-py3')
styear
runfile('C:/Users/gheom/.spyder-py3/Q03_use_LinRegress.py', wdir='C:/Users/gheom/.spyder-py3')
styear
edyear
runfile('C:/Users/gheom/.spyder-py3/Q03_use_LinRegress.py', wdir='C:/Users/gheom/.spyder-py3')
x = np.arange(1979, 2018+1)
plt.plot(x, avg_SST_year, 'go--')
runfile('C:/Users/gheom/.spyder-py3/Q03_use_LinRegress.py', wdir='C:/Users/gheom/.spyder-py3')
x.shape
y.shape
y = beta*x + alpha
y.shape
x.shape
x = np.arange(styear,edyear,5)
x

x = np.arange(styear,edyear,4)
x
x = np.arange(1980,2020,4)
x
x = np.arange(1980,2020,5)
x
x = np.arange(1980,2021,5)
x
runfile('C:/Users/gheom/.spyder-py3/Q03_use_LinRegress.py', wdir='C:/Users/gheom/.spyder-py3')
x.shape
y.shape
runfile('C:/Users/gheom/.spyder-py3/Q03_use_LinRegress.py', wdir='C:/Users/gheom/.spyder-py3')
runfile('C:/Users/gheom/.spyder-py3/Q04_use_PrincipalComp.py', wdir='C:/Users/gheom/.spyder-py3')
month = str(j).rjust(2,"0")
month
a = 1
mt = a.rjust(2,"0")
runfile('C:/Users/gheom/.spyder-py3/Q04_use_PrincipalComp.py', wdir='C:/Users/gheom/.spyder-py3')
SST_year = []
for y in range(11, len(SSTs)-1, 12): 
    SSTy = np.nanmean(SSTs[y:y+3,:,:],0)
    SST_year.append(SSTy)
    
SST_year
SST_year.shape
len(SSTs)-1
runfile('C:/Users/gheom/.spyder-py3/Q04_use_PrincipalComp.py', wdir='C:/Users/gheom/.spyder-py3')
SST_year = []
for y in range(11, len(SSTs)-1, 6): 
    SSTy = np.nanmean(SSTs[y:y+4,:,:],0)
    SST_year.append(SSTy)
#############################################################
runfile('C:/Users/gheom/.spyder-py3/Q04_use_PrincipalComp.py', wdir='C:/Users/gheom/.spyder-py3')
eigen_vec
eigen_vec.shape
a = eigen_vec * PCs
eigen_vec * eigen_val
eigen_vec * EOF
EOF
EOF.shape
runfile('C:/Users/gheom/.spyder-py3/Q02_use_Function.py', wdir='C:/Users/gheom/.spyder-py3')
runfile('C:/Users/gheom/.spyder-py3/Q03_use_LinRegress.py', wdir='C:/Users/gheom/.spyder-py3')
plt.plot(x, avg_SST_year, 'go--')
# -*- coding: utf-8 -*-
"""
기말고사 3번 문제 (8점): 최소제곱법 이해 및 회귀분석법 적용 
3-A: 최소제곱법의 정의를 기술 (2점)
3-B: 파이썬 linregress 적용하고 그림 그리기 (3점)
3-C: 평균제곱오차 (Mean squared error) 계산 (3점)
"""
# load necessary modules
import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import scipy.stats as stats

data1 = nc.Dataset('sst/sst.197901.nc')
lat = data1.variables['lat'][:]
lon = data1.variables['lon'][:]

#### Import monthly SST data
styear=1979 #start year
edyear=2018 #end year

SSTs = np.zeros([12*40, len(lat), len(lon)])

k=0
for i in range(styear,edyear+1):
    for j in range(1,13): # loop for months

        year = str(i)
        month = str(j).zfill(2) # two digit string
        filename = 'sst/sst.'+year+month+'.nc' #file name
        data = nc.Dataset(filename) #read SST file
        SST_month = data.variables['sst'][:,:] 
        SSTs[k,:,:] = SST_month[0,:,:]
        
        k+=1
print(i)

idxNaN = np.where(SSTs<0)
SSTs[idxNaN] = np.NaN

print(np.nanmax(SSTs))
print(np.nanmin(SSTs))

#### Annual mean
SST_year = np.zeros([40, len(lat), len(lon)]) 
for i in range(0, 40):
    SST_year[i,:,:] = np.nanmean(SSTs[12*i:12*(i+1),:,:],0)
    
#### Cosine weighting & area average  
cosarray = np.zeros((len(lat),len(lon))) 
for x in range(0, len(lat)):
    cosarray[x,:]=np.cos(lat[x]*np.pi/180)

idxNaN2d = (np.isnan(SST_year[0,:,:]) == True)
cosarray[idxNaN2d] = np.NaN

wgt_SST_year0 = np.zeros(SST_year.shape)
for t in range(0, len(SST_year)):
    wgt_SST_year0[t,:,:] = SST_year[t,:,:]*cosarray
    
wgt_SST_year = np.nansum(wgt_SST_year0, 2)
avg_SST_year = np.nansum(wgt_SST_year, 1)/np.nansum(cosarray) -273

#################################################################
## 3-A: 최소제곱법 (Least Squared Method) ##
# 최소제곱법에 대해서 아는대로 기술하세요 (2점) 
'''
 최소제곱법은 회귀 분석법중 하나로 실제로 관측된 값과 코딩을 통하여 이론적으로 가정한 
 기댓값의 편차 제곱 합을 최소로 하여 모집단의 값을 추정하는 방법이다. 
'''
##################################################################
x = np.arange(1979, 2018+1)
plt.plot(x, avg_SST_year, 'go--')

x= np.arange(1980,2021,5)
r = stats.linregress (x,avg_SST_year)

beta = r.slope
alpha = r.intercept

x= np.arange(1980,2021,5)
y = beta*x + alpha
runfile('C:/Users/gheom/.spyder-py3/Q04_use_PrincipalComp.py', wdir='C:/Users/gheom/.spyder-py3')
eigen_Vec
eigen_vec
eigen_vec.shape
PCs.shape
efrac.shape
efrac1.shape
eigen_val, eigen_vec = np.linalg.eig(cov_T2a_1d)
runfile('C:/Users/gheom/.spyder-py3/Q02_use_Function.py', wdir='C:/Users/gheom/.spyder-py3')
Mse = np.sum((y-avg_SST_year)**2)
runfile('C:/Users/gheom/.spyder-py3/Q03_use_LinRegress.py', wdir='C:/Users/gheom/.spyder-py3')
runfile('C:/Users/gheom/.spyder-py3/plot_EOF_week12_PCs(1).py', wdir='C:/Users/gheom/.spyder-py3')
runfile('C:/Users/gheom/.spyder-py3/plot_EOF_week12_students.py', wdir='C:/Users/gheom/.spyder-py3')
eigen_vec
eigen_vec.shape
eigen_vec**2.shape
a = eigen_vec * eigen_vec
a.shape
a
a = eigen_vec @ eigen_vec
a.shape
a
SST_year = []
for y in range(11, len(SSTs)-1, 12): 
    SSTy = np.nanmean(SSTs[y:y+4,:,:],0)
    SST_year.append(SSTy)
    
SST_year.shape
SST_year
for y in range(11, len(SSTs)-1, 12)
runfile('C:/Users/gheom/.spyder-py3/Q04_use_PrincipalComp.py', wdir='C:/Users/gheom/.spyder-py3')
SST_year = []
for y in range(6, len(SSTs)-1, 12): 
    SSTy = np.nanmean(SSTs[y:y+4,:,:],0)
    SST_year.append(SSTy)
    
runfile('C:/Users/gheom/.spyder-py3/Q03_use_LinRegress.py', wdir='C:/Users/gheom/.spyder-py3')
Mse = np.sum((y-avg_SST_year)**2)
mse
Mse
Mse.shape
runfile('C:/Users/gheom/.spyder-py3/Q02_use_Function2.py', wdir='C:/Users/gheom/.spyder-py3')
runcell(0, 'C:/Users/gheom/.spyder-py3/Q02_use_Function2.py')
runfile('C:/Users/gheom/.spyder-py3/Q02_use_Function2.py', wdir='C:/Users/gheom/.spyder-py3')