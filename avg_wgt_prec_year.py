import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import scipy.stats as stats

data1 = nc.Dataset('C:\\Users\\gheom\\.spyder-py3\\EVAPintp\\EVAP.199711.nc')
data2= nc.Dataset('C:\\Users\\gheom\\.spyder-py3\\PRECintp\\PREC.201801.nc')  

lat = data1.variables['lat'][:]
lon = data1.variables['lon'][:]
time = data1.variables['time'][:]

#### Import monthly evaporation data 
EVAPdir='C:\\Users\\gheom\\.spyder-py3\\EVAPintp\\' # directory
PRECdir = 'C:\\Users\\gheom\\.spyder-py3\\PRECintp\\'

styear=1979 #start year
edyear=2019 #end year

evap_year = np.zeros([(edyear-styear+1), len(lat), len(lon)])
prec_year = np.zeros([(edyear-styear+1), len(lat), len(lon)])

nday_list1=np.array([31,28,31,30,31,30,31,31,30,31,30,31])
nday_list2=np.array([31,29,31,30,31,30,31,31,30,31,30,31])


for i in range(styear,edyear+1):
    ## checking leap year
    if i%4 != 0:
        nday = nday_list1[:]
        
    else:
        nday = nday_list2[:]
	
    ## Save annual evaporation (m) in evap_year 
    for j in range(1,13): # loop for months 
    
        year = str(i)
        
        month = str(j).zfill(2) # two digit string
        
        filename = EVAPdir+'EVAP.'+year+month+'.nc' #file name
        
        data = nc.Dataset(filename) #read EVAP file
        
        evap_month = data.variables['e'][:,:] #[m/day]
        
        evap_year[i-styear,:,:] += evap_month[0,:,:]*nday[j-1]
        
        filename2 = PRECdir+'PREC.'+year+month+'.nc'
            
        data2 = nc.Dataset(filename2)
            
        prec_month = data2.variables['tp'][:,:] 
        
        prec_year[i-styear,:,:] += prec_month[0,:,:]*nday[j-1]
        
print(i)
       

#### Cosine weighting & area average  
cosarray=np.zeros((len(lat),len(lon))) 

for x in range(0, len(lon)):
    
	cosarray[:,x] = np.cos(lat*np.pi/180)

wgt_evap_year0 = np.zeros(evap_year.shape)
wgt_prec_year0 = np.zeros(prec_year.shape)


for t in range(0, len(evap_year)):
    
    wgt_evap_year0[t,:,:] = -evap_year[t,:,:]*cosarray
    wgt_prec_year0[t,:,:] = prec_year[t,:,:]*cosarray
    
    
# np.sum(np.sum(wgt_evap_year0,2))/(37*72)

#avg_evap_year =np.sum(np.sum(wgt_evap_year0,2),2)/(37*72)

wgt = np.sum(wgt_evap_year0,2)

avg_evap_year = np.sum(wgt,1)/np.sum(cosarray)

wgt_prec_year = np.sum(wgt_prec_year0,2)

avg_prec_year = np.sum(wgt_prec_year,1)/np.sum(cosarray)

fig = plt.figure(figsize=(5.5,5))
plt.plot(avg_evap_year, avg_prec_year, 'go')

r = stats.linregress (avg_evap_year,avg_prec_year)

xx = np.arange(1,1.095,0.01)
yy = r.slope*xx + r.intercept

plt.plot(avg_evap_year, avg_prec_year, 'go', xx, yy, 'r')

    

