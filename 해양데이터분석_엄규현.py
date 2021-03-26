import numpy as np

import matplotlib.pyplot as plt

import netCDF4 as nc

from mpl_toolkits.basemap import Basemap


m = Basemap( projection='cyl', llcrnrlat=-90, urcrnrlat=90, llcrnrlon=0, urcrnrlon=360 )

m.drawcoastlines()

data = nc.Dataset('EVAP.201907.nc')

lat = data.variables['lat'][:]

lon = data.variables['lon'][:]

evaps = data.variables['e'][:]

evaps = -evaps*100*31

levels = np.arange (-42, 38, 6)

draw = plt.contourf(lon, lat, evaps[0,:,:], levels, cmap = 'jet', extend = 'both')

plt.colorbar(draw, orientation = 'horizontal', fraction = 0.05, pad = 0.08, label = '[cm]')

