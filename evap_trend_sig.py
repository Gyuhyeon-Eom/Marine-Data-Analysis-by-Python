import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import scipy.stats as stats
from mpl_toolkits.basemap import Basemap

data1 = nc.Dataset('C:\\Users\\gheom\\.spyder-py3\\EVAPintp\\EVAP.201801.nc')
lat = data1.variables['lat'][:]
lon = data1.variables['lon'][:]
time = data1.variables['time'][:]

EVAPdir='C:\\Users\\gheom\\.spyder-py3\\EVAPintp\\' 

styear=1979 
edyear=2019 

evap_year = np.zeros([(edyear-styear+1), len(lat), len(lon)])
nday_list1=np.array([31,28,31,30,31,30,31,31,30,31,30,31])
nday_list2=np.array([31,29,31,30,31,30,31,31,30,31,30,31])

for i in range(styear,edyear+1):
    
    evap_list_month = []
    
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
        
        evap_year[i-styear,:,:] -= evap_month[0,:,:]*nday[j-1]
        
    print(i)
       
evap_trend = np.zeros((len(lat),len(lon)))

evap_sig = np.zeros(np.shape(evap_trend))

years = np.arange(styear, edyear+1)

for i in range(len(lat)):
    
    for j in range(len(lon)):
        evaps = evap_year[:,i,j]
        r = stats.linregress(years, evaps)
        
        evap_trend[i,j] = 100*r.slope*len(years)
        if r.pvalue < 0.05 :
            evap_sig[i,j] = 1
            
        else:
            evap_sig[i,j]=np.NAN
            
evap_trend_sig = evap_trend*evap_sig

fig = plt.figure(figsize=(8, 5))

plt.plot(years, evaps, 'go')
m = Basemap(projection='cyl', resolution='c', llcrnrlat =- 90, urcrnrlat=90, llcrnrlon=0, urcrnrlon=360) 
m.drawparallels(np.arange(-90,120,30), labels=[1,0,0,0])
m.drawmeridians(np.arange(0,420,60), labels=[0,0,0,1]) 
m.drawcoastlines()

levels = np.arange(-40,41,4.0)


draw = plt.contourf(lon,lat,evap_trend, levels, cmap='jet', extend='both', latlon = True)

plt.colorbar(draw, orientation ='horizontal', fraction = 0.05, pad = 0.08, label = '[cm]')

plt.title('Surface Evaporation Trend', fontsize = 15)
            
            
            
            



