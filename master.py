#master file for rail journeys project

#=========USER CONFIG===========================================================
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

import national_rail

import distances_for_postcodes.py

import fun_ratio_calc



