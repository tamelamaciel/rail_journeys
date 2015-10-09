#! /usr/local/bin/python
#===============================================================================
# works out best value for money using
# prices from 'prices_from_<start>' and
# distances from 'distances_frm_<start>'
# 
# produces file 'rail_fun_<start>.txt'
#-------------------------------------------------------------------------------
# Tamela Maciel Nov 2013
#===============================================================================
import sys
import string
import math
import numpy as np

#################### BEGIN USER INTERFACE ######################################
print '-----------------------------------------------------------------------'
print 'UK Rail Value - Miles per Pound calculator'
print '-----------------------------------------------------------------------'
start = raw_input('Starting station (e.g. KGX, CBG, BHM, etc): ')
print '-----------------------------------------------------------------------'
date = raw_input('Date of travel (e.g. oct2014): ')

 
file_name='rail_value_'+start+'_'+date+'.txt' 
fileout = open(file_name,'w')
fileout.write('station_name, station_code, station_postcode, lat, long, dist_miles, price, miles_per_pound\n')
fileout.close()


#get distance data:

dist_data=np.genfromtxt('distances_from_'+start+'.txt',delimiter=', ',dtype=[('name', 'S30'), ('code', 'S4'), ('pc', 'S9'), ('lat', '<f8'), ('long', '<f8'), ('dist', '<f8')])



#read in price data:

rail_fun=[]
file=open('prices_from_'+start+'.txt','r')

while 1:
	line=file.readline()
	if '#' in line:
		continue
	if not line: break

	items=string.split(line,',')
	
	station_name=items[0]
	station_code=items[1]
	price=items[2].strip('\n')

	#get distance data:

	#index of postcode in dist_data
	i=np.where(dist_data['code']==station_code)[0][0]

	station_postcode=dist_data['pc'][i]
	station_lat=dist_data['lat'][i]
	station_long=dist_data['long'][i]
	dist_miles=dist_data['dist'][i]
	if dist_miles<700.:
		try:
			fun_ratio=dist_miles/float(price)
		except ValueError:
			fun_ratio=0

	rail_fun.append([station_name,station_code,station_postcode,station_lat,station_long,dist_miles,price,fun_ratio])

	nextline=string.join([station_name,station_code,station_postcode,str(station_lat),str(station_long),str(dist_miles),price,str(fun_ratio)+'\n'],', ')

	print nextline

	fileout = open(file_name,'a')
	fileout.write(nextline)
	fileout.close()	






#sort rail_fun array according to fun_ratio
from operator import itemgetter
rail_fun.sort(key=itemgetter(7))

best_value_name = rail_fun[-1][0]
best_value_dist = rail_fun[-1][5]
best_value_price = rail_fun[-1][6]

print '---------------------------'
print 'Best value for money:  '
print '   (for single ticket)'
print '   Station: '+best_value_name
print '   Dist (miles): '+str(best_value_dist)
print '   Price (pounds): '+str(best_value_price)
print '---------------------------'

file.close()





