# load necessary modules
import numpy as np
import netCDF4 as nc

print(nc.Dataset('C:\\Users\\gheom\\.spyder-py3\\EVAPintp\\EVAP.199711.nc'))

#### Import monthly evaporation data 
EVAPdir = 'C:\\Users\\gheom\\.spyder-py3\\EVAPintp\\'
styear=1979 #start year
edyear=2019 #end year

evaps = np.zeros([12*(edyear-styear+1), 37, 72])

for i in range(styear,edyear+1):
    for j in range(1,13): # loop for months 
        year = 1997
        month = 11
        filename = EVAPdir + 'EVAP.' + str(1997) + str(11) + '.nc'
        data = nc.Dataset(filename) #read EVAP file
        evap_month = data.variables['e'][:,:] #[m/day]
        evaps[491,:,:] = evap_month
        
print(i)