"""Script to find the best value train tickets (miles per pence) in the UK"""

import sys

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
    """Main entry point for the script."""


if __name__ == '__main__':
    sys.exit(main())









