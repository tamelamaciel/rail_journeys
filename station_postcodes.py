#! /usr/local/bin/python
#===============================================================================
#
#-------------------------------------------------------------------------------
# Tamela Maciel Nov 2013
#===============================================================================
import sys
import string
import mechanize
import math
import time
from BeautifulSoup import BeautifulSoup





#################### INPUT and OUTPUT FILES ####################################
stationfile='Station_use_2011-12.csv'
resultsfile='station_postcodes.txt'

######### Write header #########################
fileout = open(resultsfile, 'w')
fileout.write('#Station_name station_code postcode\n')
fileout.close()
################################################

######################
#list of possible stations
#read in txt file 
array=[]
file=open(stationfile, 'r')
for line in file:
  if '#' in line:
    continue
  else: array.append(line.split(','))
file.close()


#define a function that extracts column i from the specified matrix
def column(matrix,i): 
  return [row[i] for row in matrix]

station_codes=column(array,1) 
station_names=column(array,2)


######### Setup browser #######################


# Browser
br = mechanize.Browser()

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# User-Agent (I don't understand this?)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
################################################

########################################################
#Then query national rail
# The site we will navigate into, handling its session
# find form action journey planner, form id journeyPlannerForm


for station in station_names:
	i=station_names.index(station)
	code=station_codes[i]
	try:
		br.open('http://www.nationalrail.co.uk/stations/'+code+'/details.html')

		html = br.response().read()
		soup = BeautifulSoup(html)
		txtsoup=str(soup).split('\n')

		#find item txtsoup that matches '</address>'
		i=txtsoup.index('                          </address>')	
		postcode=txtsoup[i-1].strip(' ' ).strip('\r') #returns just postcode
	except:
		postcode='??'

	print station+' postcode: '+postcode
	#write to outfile
	nextline=string.join([station,code,postcode+'\n'],',')
	fileout=open(resultsfile,'a')
	fileout.write(nextline)
	fileout.close()
	time.sleep(2) #wait 2 seconds






