#! /usr/local/bin/python
#===============================================================================
# To query the national rail website
#       http://www.nationalrail.co.uk/
# Asks for starting destination
# Picks date one month ahead
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

print "Querying National Rail for journeys from "+start+" on "+date

#################### INPUT and OUTPUT FILES ####################################
stationfile='Station_use_2011-12.csv'
resultsfile='prices_from_'+start+'.txt'

######### Write header #########################
fileout = open(resultsfile, 'w')
fileout.write('#Furthest journeys from '+start+', travelling on '+date+'\n')
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
class NoHistory(object):
  def add(self, *a, **k): pass
  def clear(self): pass


# Browser
br = mechanize.Browser(history=NoHistory())
# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# User-Agent 
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]


################################################

########################################################
#Then query national rail
# The site we will navigate into, handling its session
# find form action journey planner, form id journeyPlannerForm

for station in station_names:

	br.open('http://www.nationalrail.co.uk/')
	i=station_names.index(station)
	code=station_codes[i]
	#postcode=station_postcodes[i]
	# Select the first (index zero) form
	br.select_form(nr=2)
	#br.form.set_all_readonly(False)
	# Fill in form. 
	br.form['from.searchTerm']=start
	br.form['to.searchTerm'] = code
	br.form['timeOfOutwardJourney.monthDay'] = date
	br.form['timeOfOutwardJourney.hour'] = ['05']
	br.form['timeOfOutwardJourney.minute'] = ['0']
	if journey == 'r':
		br.form['checkbox'] = [true] #select for return journey
		br.form['timeOfReturnJourney.monthDay'] = return_date
		br.form['timeOfReturnJourney.hour'] = ['17']
		br.form['timeOfReturnJourney.minute'] = ['0']

	br.form['rcards'] = ['YNG'] #search with young persons rail card
	br.form['numberOfEachRailcard'] = ['1']


	# Submit query 
	br.submit()

	html = br.response().read()
	soup = BeautifulSoup(html)
	txtsoup=str(soup).split('\n')

	#find item txtsoup that matches 'buyCheapest button'

	matches = [s for s in txtsoup if "cheapestFare" in s] #list of matches
	print matches
	try:
		cheapest=matches[0].split('&#163;')[1].strip('\r') #string of pound value. '&#163;' is the pound sign
	except IndexError:
		cheapest='??'

	print 'The cheapest fare between '+start+' and '+station+' is: '+cheapest
	#write to outfile
	nextline=string.join([station,code,cheapest+'\n'],',')
	fileout=open(resultsfile,'a')
	fileout.write(nextline)
	fileout.close()
	time.sleep(2) #wait 2 seconds


	# br.select_form
	# br.follow_link(text_regex=r"edit-j-btn")
	# <li class="ctf-edit ctf-bl"><a href="#num2" id="edit-j-btn">Edit journey / add return</a></li>




