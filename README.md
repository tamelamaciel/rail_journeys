**UK Railway Value for Money**

By Tamela Maciel

ABOUT:

*By train, how far can I get for the least amount of money?*

This simple question led to the development of a python script that, using data from the UK's National Rail website, lists the price of a single ticket on the morning of 1st October 2014 from a starting station to all other UK stations. 
Being based in Cambridge at the time, I first ran this script starting from Cambridge. I acquired the latitude and longitudes of each station and calculated the 'as the crow flies' distance from Cambridge to said station. The resulting 'Value for Money' ratio divides the distance in miles from Cambridge by the price in pounds. I repeated the process for other UK starting points including London King's Cross and Birmingham New Street.  

**Ticket price data** is scaped from the [National Rail website](http://www.nationalrail.co.uk/) using the Python library [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/). The ticket prices were collected for a single advance ticket travelling sometime after 5am on Wednesday 1 Oct 2014. Data collected in July 2014.  

**Station postcodes** come from the National Rail website, with amendments from [Railway Station](http://www.railwaystation.co.uk/) and Google. 

**Distance as the crow flies** is calculated using the Python [Geopy](https://github.com/geopy/geopy) package. 

**Value for Money** = distance (miles) / ticket price (£)  
By this definition, if the Value for Money ratio is large, then £1 carries you further away from the starting location and thus that journey is particularly good value. 

**Data is visualized** using [Tableau Public](http://www.tableausoftware.com/public/community).  

**Caveat**: These maps are simply intended to illustrate the regional railway values throughout the UK. While I have checked the majority of stations for accuracy in price (as retrieved in July 2014 for 1 October 2014) and location, small inaccuracies might still exist for individual stations. 

HOW TO RUN:

Run rail_value.py. 

`python rail_value.py`

This contains a series of functions to scrape ticket price data from the National Rail website, calculate distances between stations, and compute the value for money ratio for each station.

The code checks to make sure that the data does not already exist in the directory, and if it does exist, it skips the website query.

Note, there is a built-in time delay between requests to the National Rail website and this part of the code takes a long time to run. I normally leave it to run overnight. 

To re-generate station postcodes, run station_postcodes.py to create a data file "station_postcodes.txt". Note this only needs to be done once.


RESULTS:

**Starting from Cambridge (CBG) - Bursting the bubble**

Best value journey: Devonport, Plymouth (224 miles for £25.60)

[See Cambridge rail journey viz on Tableau Public](https://public.tableau.com/profile/tm419#!/vizhome/CambridgeRailValue/CambridgeRailValue)

<a href="https://public.tableau.com/profile/tm419#!/vizhome/CambridgeRailValue/CambridgeRailValue" target="_blank"><img src="Cambridge Rail Value.png" width="649"/></a>


*Notes on rail journeys from Cambridge*
* Cambridge is generally quite an expensive starting point and only a few regions on the map are of good value, especially when compared to the London King's Cross map below.

* The best value journeys are to locations in the West Country around Plymouth, south Wales, as well as a few stops in Yorkshire, Glasgow, and stations along the Far North line in the Scottish Highlands. 



**London King's Cross (KGX) - Is it cheaper to start in central London?**

Best value journey:  Solihull, West Midlands (93 miles for £6)

[See London King's Cross rail journey viz on Tableau Public](https://public.tableau.com/profile/tm419#!/vizhome/KingsCrossRailValue/KingsCrossRailValue)

<a href="https://public.tableau.com/profile/tm419#!/vizhome/KingsCrossRailValue/KingsCrossRailValue" target="_blank"><img src="King's Cross Rail Value.png" width="649"/></a>

*Notes on rail journeys from London King's Cross*
* As might be expected when starting from a station on the main line, King's Cross journeyers have a much better value ticket than Cambridge folk to pretty much anywhere in the UK.

* Similar regions of the UK are particularly good value. The Glasgow, Birmingham, and Liverpool regions as well as the Yorkshire Dales and coastal towns in Norfolk have great bang for buck.

* Too far away from London and the miles per pound value goes down again (i.e. north Scotland and Cornwall) but in general, Londoners can do very well on a weekend getaway.



**Birmingham New Street (BHM) - Is it as cheap to leave as to arrive?**

Best value journey: Sanquhar, Scotland (217 miles for £12.50)

[See Birminham New Street rail journey viz on Tableau Public](https://public.tableau.com/profile/tm419#!/vizhome/BirminghamRailValue/BirminghamRailValue)

<a href="https://public.tableau.com/profile/tm419#!/vizhome/BirminghamRailValue/BirminghamRailValue" target="_blank"><img src="Birmingham Rail Value.png" width="649"/></a>

*Notes on rail journeys from Birmingham*
* Birmingham is a excellent starting location to get great value rail tickets to most of Scotland. However the Argyll region is not good value. This because stations in this region are the tail end of the western line up from Glasgow. This line only runs two or three trains a day from BHM that can get you to places like Mallaig and Loch Awe on the same day of travel. Stations in the rest of Scotland have more frequent services and are better value as a result.

* The Glasgow - Edinburgh region continues to be excellent value for money, as well as Liverpool, the Lake District, and north Wales.

* Kent is surprisingly good value from Birmingham, given the need to travel through London (Euston and St Pancreas). But by taking the 5:29am train from Birmingham New Street, one can get to Dover and other seaside towns for just £25.50 advance. Note that this not cheaper than a ticket to central London (which is about £20 in advance from BHM), but it is better value because of the greater distance travelled.

For more details see [GitHub repository](https://github.com/tamelamaciel/rail_journeys/).
