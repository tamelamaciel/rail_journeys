#! /usr/local/bin/python
#===============================================================================
# Calculates distance as the crow flies from starting point to all other station postcodes
# in statute miles.
# uses a package installed called geopy which isn't installed on the work computer
#-------------------------------------------------------------------------------
# Tamela Maciel Nov 2013
#===============================================================================
import sys
import string
import math
import numpy as np
from geopy import geocoders
from geopy import distance

start='OXF' #<-------- edit for starting location (CBG, BHM, KGXetc)
 
outfile='distances_from_'+start+'.txt' 

fileout = open(outfile,'w')
fileout.write('# station, code, postcode, lat, long, distance_miles\n')
fileout.close()

#starting location lat, long:

g=geocoders.GoogleV3()
place,(start_lat,start_long)=g.geocode('oxford, uk') #<-------- edit for starting location


#read in station_postcodes_definitive.txt

postcodes_data=np.genfromtxt('station_postcodes_definitive.txt',dtype=[('name','|S30'),('code','S5'),('postcode','S12')], comments='#',delimiter=',')


#read in uk-postcodes.csv

lat_long_data=np.genfromtxt('uk-postcodes.csv',dtype=[('code','S5'),('x','float'),('y','float'),('lat','float'),('long','float')], comments='#',delimiter=',')


for line in postcodes_data:
	station_name=line['name']
	station_code=line['code']
	station_postcode=line['postcode']

	#first part of station postcode

	station_postcode1=station_postcode.split()[0]


	#index of postcode in dist_data

	i=np.where(lat_long_data['code']==station_postcode1)[0][0]

	#lat and long

	station_lat=lat_long_data['lat'][i]
	station_long=lat_long_data['long'][i]

	#distance from starting station

	dist_miles=distance.distance((start_lat,start_long),(station_lat,station_long)).miles

	if dist_miles > 700.:
		print '---'
		print station_name+' has too large a distance ('+dist_miles+')'
		print '---'
		dist_miles='??'

	nextline=string.join([station_name,station_code,station_postcode,str(station_lat),str(station_long),str(dist_miles)+'\n'],', ')

	fileout = open(outfile,'a')
	fileout.write(nextline)
	fileout.close()
