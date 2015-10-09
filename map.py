import sys
import string
import math
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import colors
from geopy import geocoders
from geopy import distance
import time

from matplotlib import rcParams
rcParams['font.family'] = 'serif'
rcParams['font.serif'] = ['Palatino']
# rcParams['text.usetex'] = True
# rcParams['text.latex.preamble'] = \
#     '\usepackage{amsfonts},' \
#     '\usepackage{amsmath},' \
#     '\usepackage[T1]{fontenc},' \
#     '\usepackage{txfonts},' 


# cities=[]
# g=geocoders.GoogleV3()
# cities.append(['Cambridge',g.geocode('cambridge,uk')[1][1],g.geocode('cambridge, uk')[1][0]])
# cities.append(['London',g.geocode('london,uk')[1][1],g.geocode('london, uk')[1][0]])
# cities.append(['Manchester',g.geocode('Manchester,uk')[1][1],g.geocode('Manchester, uk')[1][0]])
# time.sleep(1)
# cities.append(['Birmingham',g.geocode('Birmingham,uk')[1][1],g.geocode('Birmingham, uk')[1][0]])
# cities.append(['Bristol',g.geocode('Bristol,uk')[1][1],g.geocode('Bristol, uk')[1][0]])
# #cities.append(['Leeds',g.geocode('Leeds,uk')[1][1],g.geocode('Leeds, uk')[1][0]])
# #time.sleep(1)
# cities.append(['Glasgow',g.geocode('Glasgow,uk')[1][1],g.geocode('Glasgow, uk')[1][0]])
# cities.append(['Newcastle',g.geocode('Newcastle,uk')[1][1],g.geocode('Newcastle, uk')[1][0]])
# cities.append(['Southampton',g.geocode('Southampton,uk')[1][1],g.geocode('Southampton, uk')[1][0]])

# g.geocode('london, uk')[1]
# g.geocode('manchester, uk')[1]
# g.geocode('birmingham, uk')[1]
# g.geocode('Leeds, uk')[1]
# g.geocode('liverpool uk')[1]
# g.geocode('glasgow, uk')[1]
# g.geocode('bristol, uk')[1]
# g.geocode('cambridge, uk')[1]
# g.geocode('edinburgh, uk')[1]
# g.geocode('cardiff, uk')[1]
# g.geocode('newcastle, uk')[1]
# g.geocode('cambridge, uk')[1]
# g.geocode('southampton, uk')[1]

start='OXF' #<-------- edit for starting location

#read in data
file=open('rail_fun_'+start+'.txt','r')
station_points=[]
while 1:
	line=file.readline()
	if '#' in line:
		continue
	if not line: break

	station_points.append(string.split(line,', ')) # station_name, station_code, station_postcode, lat, long, dist_miles, price, fun_ratio

	



#plot map

plt.cla()
plt.clf()

fig_dims      = [5.13*1.3, 6.5*1.3] # fig dims as a list

fig=plt.figure(figsize=fig_dims)
# ax = fig.add_subplot(111)


# Plot latlon data on an OSGB map.
ax = plt.axes([0.01, 0.01, 0.98, 0.98], projection=ccrs.PlateCarree())

ax.set_xlim([-8, 3])
ax.set_ylim([48, 61])

#ax.stock_img()
#ax.coastlines(resolution='50m')

# land_50m = cfeature.NaturalEarthFeature('physical', 'land', '50m',
#                                         edgecolor='face',
#                                         facecolor=cfeature.COLORS['land'])

coastline_50m = cfeature.NaturalEarthFeature('physical', 'coastline', '50m',
                                        edgecolor='black',
		                                facecolor='white')
# cities_50m = cfeature.NaturalEarthFeature('cultural', 'populated_places', '50m',edgecolor='black',facecolor='black',zorder=13)


# ax.add_feature(land_50m)
ax.add_feature(coastline_50m)
#ax.add_feature(cities_50m)
# ax.add_feature(cfeature.LAND)
# ax.add_feature(cfeature.COASTLINE)
# ax.add_feature(cfeature.RIVERS)
# ax.add_feature(cfeature.LAKES)
#ax.add_feature(states_provinces, edgecolor='gray')

station_points=np.array(station_points)
longs=[float(x) for x in station_points[:,4]]
lats=[float(x) for x in station_points[:,3]]
fun=[float(x.strip('\n')) for x in station_points[:,7]]


plt.text(0.02, 0.98,'Best-value rail destinations from '+start, ha='left',va='center',transform = ax.transAxes,fontsize=12,weight='bold')
plt.text(0.98, 0.02,'Tamela Maciel 2013\n  data from National Rail', ha='right',va='center',transform = ax.transAxes,fontsize=7)
# for city in cities:
# 	plt.text(city[1], city[2], city[0],horizontalalignment='left',transform=ccrs.Geodetic(),fontsize=8,color='#808080',zorder=14)

norm = matplotlib.colors.Normalize(vmin = 0.01, vmax = max(fun), clip = False)

stations=plt.scatter(longs,lats, c=fun, norm=norm, marker='o',s=9,lw=0.1,cmap='jet_r',zorder=12,transform=ccrs.Geodetic())
plt.colorbar(stations,ax=ax,fraction=0.1, pad = 0.02,orientation='horizontal',shrink=0.7) #ticks=[0,3,6,9,12,15,18]

plt.text(0.5, -0.1,'Miles per pound', ha='center',va='center',transform = ax.transAxes,fontsize=11,weight='bold')
plt.text(0.15, -0.09,'worst value', ha='center',va='center',transform = ax.transAxes,fontsize=10)
plt.text(0.85, -0.09,'best value', ha='center',va='center',transform = ax.transAxes,fontsize=10)
#plt.tight_layout(pad=0.1)
#plt.savefig('ukmap_bestvalue_rail_from_'+start+'.pdf',dpi=300,bbox='tight')
plt.savefig('maps/ukmap_bestvalue_rail_from_'+start+'.jpeg',dpi=300,bbox='tight')