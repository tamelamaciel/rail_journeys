"""Script to find the best value train tickets (miles per pence) in the UK"""

import sys
import string
import math
import numpy as np

#=========CONFIG===============================================================
# -----------------------------------------------------------------------
# Options:
#   default journey: single
#   default time of day: from 5am onwards
# -----------------------------------------------------------------------
# starting station, full name or three-letter code
start = 'LEI' 
# date DD/MM/YY
date = '09/11/15'
# type (s for single or r for return):
journey = 's'
#===============================================================================

day = date.split('/')[0]
month = date.split('/')[1]
year = date.split('/')[2]

def get_prices_from_national_rail(start,day,month,year,journey):
    """Gets ticket prices from national rail website for all UK journeys starting at *start*"""
    pass

def calc_distances_to_stations(start):
    """Calculates distance as the crow flies from starting point to all other station postcodes in statute miles."""
    pass

def calc_value_ratio(start):
	"""Calculates the best value journeys from *start* using prices and distances to each UK station"""
	pass

def main():
	"""Main entry point for the script. 
	Works out best value for money using 
	prices from 'prices_from_<start>' and distances from 'distances_frm_<start>' 
	and produces file 'rail_fun_<start>.csv'"""
    # initialize output file for rail value data
	file_name='rail_value_'+start+'_'+date+'.csv' 
	fileout = open(file_name,'w')
	fileout.write('station_name,station_code,station_postcode,lat,long,dist_miles,price,miles_per_pound\n')
	fileout.close()

	#read in distance data:
	#TODO: if dist_data in namespace, use that; otherwise load data from file.
	dist_data=np.genfromtxt('distances_from_'+start+'.txt',delimiter=', ',dtype=[('name', 'S30'), ('code', 'S4'), ('pc', 'S9'), ('lat', '<f8'), ('long', '<f8'), ('dist', '<f8')])

	#read in price data:
	rail_value=[]
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
				value_ratio=dist_miles/float(price)
			except ValueError:
				value_ratio=0

		rail_value.append([station_name,station_code,station_postcode,station_lat,station_long,dist_miles,price,value_ratio])

		nextline=string.join([station_name,station_code,station_postcode,str(station_lat),str(station_long),str(dist_miles),price,str(value_ratio)+'\n'],', ')

		print nextline

		fileout = open(file_name,'a')
		fileout.write(nextline)
		fileout.close()	

	#sort rail_value array according to value_ratio
	from operator import itemgetter
	rail_value.sort(key=itemgetter(7))

	best_value_name = rail_value[-1][0]
	best_value_dist = rail_value[-1][5]
	best_value_price = rail_value[-1][6]

	print '---------------------------'
	print 'Best value for money:  '
	print '   (for single ticket)'
	print '   Station: '+best_value_name
	print '   Dist (miles): '+str(best_value_dist)
	print '   Price (pounds): '+str(best_value_price)
	print '---------------------------'

	file.close()


if __name__ == '__main__':
    sys.exit(main())









