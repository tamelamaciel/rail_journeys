#! /usr/local/bin/python
#===============================================================================
# Calculates distance as the crow flies from Cambridge, CB1, (lat 52.176, long 0.19) to any other postcode
# in statute miles. and works out best value for money if 'furthest_away_stations.txt' exists
# uses a package installed called geopy which isn't installed on the work computer
#-------------------------------------------------------------------------------
# Tamela Maciel Nov 2013
#===============================================================================
import sys
import string
import math
import numpy as np
import time
from geopy import geocoders
from geopy import distance



fileout = open('rail_fun.txt','w')
fileout.write('# station_name, station_code, station_postcode, dist_miles, price, fun_ratio')
fileout.close()

g=geocoders.GoogleV3()
place,(cam_lat,cam_long)=g.geocode('cambridge, uk')

postcode_data=np.genfromtxt('station_postcodes.txt',delimiter=',',dtype=None)



#read in furthest_away_stations.txt
rail_fun=[]
file=open('furthest_away_stations.txt','r')

while 1:
	line=file.readline()
	if '#' in line:
		continue
	if not line: break

	#price_data.append(string.split(line))
	items=string.split(line,',')
	
	station_name=items[0]
	station_code=items[1]
	#postcodes in furthest away stations is wrong. get from station_postcodes.txt instead
	price=items[3].strip('\n')

	#get postcodes from station_postcodes.txt:
	i=np.where(postcode_data[:,0]==station_name)[0][0] #get index of station_name
	station_postcode=postcode_data[:,2][i]
	station_postcode1=station_postcode.split()[0]

	#get distance corresponding to postcode via distances.txt file:
	dist_data=np.genfromtxt('distances.txt',dtype=[('pc', 'S4'), ('d', '<f8')])
	try:
		#index of postcode in dist_data
		j=np.where(dist_data['pc']==station_postcode1)[0][0]
		#distance from cambridge CB1
		dist_miles=dist_data['d'][j]
		if dist_miles<700.:
			try:
				fun_ratio=dist_miles/float(price)
			except ValueError:
				fun_ratio=0
		else:
			print '---'
			print station_name+' has too large a distance ('+dist_miles+')'
			print '---'
			fun_ratio=0
		rail_fun.append([station_name,station_code,station_postcode,dist_miles,price,fun_ratio])
		nextline=string.join([station_name,station_code,station_postcode,str(dist_miles),price,str(fun_ratio)+'\n'],', ')
		print nextline
		fileout = open('rail_fun.txt','a')
		fileout.write(nextline)
		fileout.close()	


	except IndexError:
		print '---'
		print station_name+' postcode not found in distances.txt'
		print '---'
		dist_miles='??'
		fun_ratio=0
		rail_fun.append([station_name,station_code,station_postcode,dist_miles,price,fun_ratio])
		nextline=string.join([station_name,station_code,station_postcode,str(dist_miles),price,str(fun_ratio)+'\n'],', ')		
		print nextline
		fileout = open('rail_fun.txt','a')
		fileout.write(nextline)
		fileout.close()	




	# ## using geocoder method. takes a while and has limited number of queries you can run in 24 hours:
	# try:
	# 	#get lat, long of station
	# 	place,(stat_lat,stat_long)=g.geocode(station_name+',uk')
	# 	#distance from cambridge CB1
	# 	dist_miles=distance.distance((cam_lat,cam_long),(stat_lat,stat_long)).miles
	# 	if dist_miles<700.:
	# 		try:
	# 			fun_ratio=dist_miles/float(price)
	# 		except ValueError:
	# 			fun_ratio=0
	# 	else:
	# 		print '---'
	# 		print station_name+' has too large a distance ('+dist_miles+')'
	# 		fun_ratio=0
	# 	rail_fun.append([station_name,station_code,stat_lat,stat_long,dist_miles,price,fun_ratio])
	# 	nextline=string.join([station_name,station_code,str(stat_lat),str(stat_long),str(dist_miles),price,str(fun_ratio),'\n'],', ')
	# 	print nextline
	# 	fileout = open('rail_fun.txt','a')
	# 	fileout.write(nextline)
	# 	fileout.close()	
	# 	time.sleep(0.5) #wait 2 seconds

	# except TypeError:
	# 	stat_lat='??'
	# 	stat_long='??'
	# 	dist_miles='??'
	# 	fun_ratio=0
	# 	rail_fun.append([station_name,station_code,stat_lat,stat_long,dist_miles,price,fun_ratio])
	# 	nextline=string.join([station_name,station_code,str(stat_lat),str(stat_long),str(dist_miles),price,str(fun_ratio),'\n'],', ')		
	# 	print nextline
	# 	fileout = open('rail_fun.txt','a')
	# 	fileout.write(nextline)
	# 	fileout.close()	
	# 	time.sleep(0.5)


#sort rail_fun array according to fun_ratio
from operator import itemgetter
rail_fun.sort(key=itemgetter(5))

best_value_name = rail_fun[-1][0]
best_value_dist = rail_fun[-1][3]
best_value_price = rail_fun[-1][4]

print '---------------------------'
print 'Best value for money:  '
print '   (for single ticket leaving Sat 1 Feb 2014)'
print '   Station: '+best_value_name
print '   Dist (miles): '+str(best_value_dist)
print '   Price (pounds): '+str(best_value_price)

file.close()





