"""Script to find the best value train tickets (miles per pence) in the UK"""
import ipdb
import sys
import string
import math
import pandas as pd
import numpy as np
import os.path

#=========CONFIG===============================================================
# -----------------------------------------------------------------------
# Options:
#   default journey: single
#   default time of day: from 5am onwards
# -----------------------------------------------------------------------
# starting station, full name or three-letter code
start = 'LEI' 
town = 'leicester, uk'
# date DD/MM/YY
date = '09-11-15'
#===============================================================================

day = date.split('-')[0]
month = date.split('-')[1]
year = date.split('-')[2]

def get_prices_from_national_rail(start,day,month,year):
	"""Gets ticket prices from national rail website for all UK journeys starting at *start*"""
	price_data=[]
    # TODO: write price at NaN if not found, rather than ??
    # TODO: write file with no spaces
    # TODO: don't need station codes
	return price_data

def calc_distances_to_stations(start,town):
	"""Calculates distance as the crow flies from starting point to all other station postcodes in statute miles."""
	from geopy import geocoders
	from geopy import distance
	# fileout = open(outfile,'w')
	# fileout.write('station_name,station_code,postcode,lat,long,distance_miles')
	# fileout.close()

	#get town lat, long:
	g=geocoders.GoogleV3()
	place,(start_lat,start_long)=g.geocode(town) 

	#read in station_postcodes_definitive.csv
	postcodes_data=pd.read_csv('station_postcodes_definitive.csv')
	# add column with just first half of postcode
	postcodes_data['postcode1'] = postcodes_data['postcode'].apply(lambda x: x.split(' ')[0])


	#read in uk-postcodes.csv
	lat_long_data = pd.read_csv('uk-postcodes.csv')
	#drop unncessary x,y columns. 
	lat_long_data = lat_long_data.drop(['x','y'], 1)

	#combine distance and price data into one data frame
	dist_data = pd.merge(postcodes_data, lat_long_data, on='postcode1', how='left')
	dist_data = dist_data.drop('postcode1',1)

	#calculate the distance between the start and the destination station for each destination
	dist_data['distance_miles'] = dist_data.apply(lambda x: distance.distance((start_lat,start_long),(x['lat'],x['long'])).miles, axis=1)
	#as a sanity check, remove values that are more than 700 miles away. too far for UK railway station
	dist_data['distance_miles'] = dist_data.apply(lambda x: x['distance_miles'] if x['distance_miles'] < 700. else NaN, axis=1)

	#write to file
	file_name = 'distances_from_'+start+'.csv'
	dist_data.to_csv(file_name, sep=',')

	return dist_data

def calc_value_ratio(dist_data,price_data):
	"""Calculates the best value journeys from *start* using prices and distances to each UK station"""
	

	#combine distance and price data into one data frame
	rail_value=pd.merge(dist_data, price_data, on='station_name', how='left')

	#add a new column, value_ratio = dist/price if the distance from start is < 700 miles (sanity check for UK)
	rail_value['value_ratio'] = rail_value.apply(lambda x : x['distance_miles']/x['price'] if x['distance_miles'] <700. else NaN, axis=1)

	#write to file
	file_name='rail_value_'+start+'_'+date+'.csv' 
	rail_value.to_csv(file_name, sep=',')

	return rail_value

def main():
	"""Main entry point for the script. 
 	Produces file 'rail_fun_<start>.csv'"""

	print 'starting station: '+start
	print 'town name: '+town
	print 'date: '+date

	#read in distance data:
	#don't rerun distances function if data file already exists
	if os.path.exists('distances_from_'+start+'.csv'):
		dist_data=pd.read_csv('distances_from_'+start+'.csv')
		print 'distance data already exists for this station. skipping distance calc...'
	else:
		dist_data=calc_distances_to_stations(start,town)

	#read in price data:
	if os.path.exists('prices_from_'+start+'_'+date+'.csv'):
		price_data=pd.read_csv('prices_from_'+start+'_'+date+'.csv')
		#drop unncessary station code column. data will be merged using station name as a key
		price_data = price_data.drop('station_code', 1)
		print 'price data already exists for this station and date. skipping web query...'
	else:
		price_data=get_prices_from_national_rail(start,day,month,year)
	ipdb.set_trace()


	#rail_value = calc_value_ratio(dist_data,price_data)

	# #get journey with maximum value_ratio
	# best_value=rail_value.loc[rail_value['value_ratio'].idxmax()]

	# best_value_name = best_value['station_name']
	# best_value_code = best_value['station_code']
	# best_value_dist = best_value['distance_miles']
	# best_value_price = best_value['price']

	# print '---------------------------'
	# print 'Best value for money:  '
	# print '   (for single ticket)'
	# print '   Station: '+best_value_name
	# print '   Code: '+best_value_code
	# print '   Dist (miles): '+str(best_value_dist)
	# print '   Price (pounds): '+str(best_value_price)
	# print '---------------------------'


if __name__ == '__main__':
    sys.exit(main())









