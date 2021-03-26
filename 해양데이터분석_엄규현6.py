import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import scipy.stats as stats
from mpl_toolkits.basemap import Basemap

data = nc.Dataset('C:\\Users\\gheom\\.spyder-py3\\T2m_ERA5_1979_2018_lowR.nc')

lat = data.variables['lat'][:]
lon = data.variables['lon'][:]
time = data.variables['time'][:]

T2m = data.variables['t2m'][:]

T2m.shape

T2m_trend = np.zeros((len(lat),len(lon)))
                     
T2m_sig = np.zeros((len(lat),len(lon)))   
                   
years = np.arange(1979,1979+len(time))

for i in range(len(lat)):
    
    for j in range(len(lon)):
        
        t2 = T2m[:,i,j]
        
        r = stats.linregress(years,t2)
        
        T2m_trend[i,j] = r.slope*len(time)
        
        if r.pvalue < 0.05 :
            T2m_sig[i,j] = 1
            
        else:
            T2m_sig[i,j]=np.NAN
            
T2m_trend_sig = T2m_trend*T2m_sig

fig = plt.figure(figsize=(8, 5))

m = Basemap(projection='cyl', resolution='c', llcrnrlat =- 90, urcrnrlat=90, llcrnrlon=0, urcrnrlon=360) 
m.drawparallels(np.arange(-90,120,30), labels=[1,0,0,0])
m.drawmeridians(np.arange(0,420,60), labels=[0,0,0,1]) 
m.drawcoastlines()

levels = np.arange(-2.25,2.5,0.25)


draw = plt.contourf(lon,lat,T2m_trend_sig, levels, cmap='jet', extend='both', latlon = True)

plt.colorbar(draw, orientation ='horizontal', fraction = 0.05, pad = 0.08, label = '[K]')

plt.title('Surface Temperature Trend', fontsize = 15)

cosarray=np.zeros((len(lat),len(lon))) 

for x in range(0, len(lon)):
    
	cosarray[:,x] = np.cos(lat*np.pi/180)

wgt_T2m_year0 = np.zeros(T2m.shape)

for t in range(0, len(T2m)):
    
    wgt_T2m_year0[t,:,:] = T2m[t,:,:]*cosarray
    
wgt_T2m_year = np.sum(wgt_T2m_year0, 2)
avg_T2m_year = np.sum(wgt_T2m_year,1)/ np.sum(cosarray) - 273

x = np.arange(1979,2018+1)
r = stats.linregress(x,avg_T2m_year)
beta = r.slope
alpha = r.intercept

y = beta*x + alpha

fig = plt.figure(figsize=(5.5, 4.5))
plt.plot(x,avg_T2m_year,'go--')

            
            