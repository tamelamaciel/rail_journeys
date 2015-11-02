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
start = 'CBG' 
# date DD/MM/YY
date = '09-11-15'
#===============================================================================

day = date.split('-')[0]
month = date.split('-')[1]
year = date.split('-')[2]

def get_prices_from_national_rail(start,day,month,year,journey):
    """Gets ticket prices from national rail website for all UK journeys starting at *start*"""
    price_data=[]
    # TODO: write price at NaN if not found, rather than ??
    # TODO: write file with no spaces
    # TODO: don't need station codes
    return price_data

def calc_distances_to_stations(start):
    """Calculates distance as the crow flies from starting point to all other station postcodes in statute miles."""
    dist_data=[]
    # TODO: write file with no spaces
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

	#read in distance data:
	#don't rerun distances function if data file already exists
	if os.path.exists('distances_from_'+start+'.csv'):
		dist_data=pd.read_csv('distances_from_'+start+'.csv')
		print 'distance data already exists for this station. skipping distance calc...'
	else:
		dist_data=calc_distances_to_stations(start)

	#read in price data:
	if os.path.exists('prices_from_'+start+'_'+date+'.csv'):
		price_data=pd.read_csv('prices_from_'+start+'_'+date+'.csv')
		#drop unncessary station code column. data will be merged using station name as a key
		price_data = price_data.drop('station_code', 1)
		print 'price data already exists for this station and date. skipping web query...'
	else:
		price_data=get_prices_from_national_rail(start,day,month,year)


	rail_value = calc_value_ratio(dist_data,price_data)

	#get journey with maximum value_ratio
	best_value=rail_value.loc[rail_value['value_ratio'].idxmax()]

	best_value_name = best_value['station_name']
	best_value_code = best_value['station_code']
	best_value_dist = best_value['distance_miles']
	best_value_price = best_value['price']

	print '---------------------------'
	print 'Best value for money:  '
	print '   (for single ticket)'
	print '   Station: '+best_value_name
	print '   Code: '+best_value_code
	print '   Dist (miles): '+str(best_value_dist)
	print '   Price (pounds): '+str(best_value_price)
	print '---------------------------'


if __name__ == '__main__':
    sys.exit(main())









