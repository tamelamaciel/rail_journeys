**UK Railway Value for Money**
By Tamela Maciel

*By train, how far can I get for the least amount of money?*

This simple question led to the development of a python script that, using data from the UK's National Rail website, lists the price of a single ticket on the morning of 1st October 2014 from a starting station to all other UK stations. 
Being based in Cambridge at the time, I first ran this script starting from Cambridge. I acquired the latitude and longitudes of each station and calculated the 'as the crow flies' distance from Cambridge to said station. The resulting 'Value for Money' ratio divides the distance in miles from Cambridge by the price in pounds. I repeated the process for other UK starting points including London King's Cross and Birmingham New Street.  

**Ticket price data** is scaped from the [National Rail website](http://www.nationalrail.co.uk/) using the Python library [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/). The ticket prices were collected for a single advance ticket travelling sometime after 5am on Wednesday 1 Oct 2014. Data collected in July 2014.  

**Station postcodes** come from the National Rail website, with amendments from [Railway Station](http://www.railwaystation.co.uk/) and Google. 

**Distance as the crow flies** is calculated using the Python [Geopy](https://github.com/geopy/geopy) package. 

**Value for Money** = distance (miles) / ticket price (£)  
By this definition, if the Value for Money ratio is large, then £1 carries you further away from the starting location and thus that journey is particularly good value. 

**Data is visualized** in a basic way with the maps.py file, and in a more sophisticated, interactive way using [Tableau Public](http://www.tableausoftware.com/public/community).  

**Caveat**: These maps are simply intended to illustrate the regional railway values throughout the UK. While I have checked the majority of stations for accuracy in price (as retrieved in July 2014 for 1 October 2014) and location, small inaccuracies might still exist for individual stations. 

***
Starting from Cambridge (CBG) - Bursting the bubble
***
Best value journey: Devonport, Plymouth (224 miles for £25.60)

<center>
<script type='text/javascript' src='https://public.tableausoftware.com/javascripts/api/viz_v1.js'></script><div class='tableauPlaceholder' style='width: 654px; height: 929px;'><noscript><a href='#'><img alt='Cambridge Rail Value ' src='https:&#47;&#47;public.tableausoftware.com&#47;static&#47;images&#47;Ca&#47;CambridgeRailValue&#47;CambridgeRailValue&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz' width='654' height='929' style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableausoftware.com%2F' /> <param name='site_root' value='' /><param name='name' value='CambridgeRailValue&#47;CambridgeRailValue' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableausoftware.com&#47;static&#47;images&#47;Ca&#47;CambridgeRailValue&#47;CambridgeRailValue&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /></object></div><div style='width:654px;height:22px;padding:0px 10px 0px 0px;color:black;font:normal 8pt verdana,helvetica,arial,sans-serif;'><div style='float:right; padding-right:8px;'><a href='http://www.tableausoftware.com/public/about-tableau-products?ref=https://public.tableausoftware.com/views/CambridgeRailValue/CambridgeRailValue' target='_blank'>Learn About Tableau</a></div></div>
</center>
**Notes on rail journeys from Cambridge**
* Cambridge is generally quite an expensive starting point and only a few regions on the map are of good value, especially when compared to the London King's Cross map below.

* The best value journeys are to locations in the West Country around Plymouth, south Wales, as well as a few stops in Yorkshire, Glasgow, and stations along the Far North line in the Scottish Highlands. 


***
London King's Cross (KGX) - Is it cheaper to start in central London? 
***
Best value journey:  Solihull, West Midlands (93 miles for £6)

<center>
<script type='text/javascript' src='https://public.tableausoftware.com/javascripts/api/viz_v1.js'></script><div class='tableauPlaceholder' style='width: 654px; height: 929px;'><noscript><a href='#'><img alt='King&#39;s Cross Rail Value ' src='https:&#47;&#47;public.tableausoftware.com&#47;static&#47;images&#47;Ki&#47;KingsCrossRailValue&#47;KingsCrossRailValue&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz' width='654' height='929' style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableausoftware.com%2F' /> <param name='site_root' value='' /><param name='name' value='KingsCrossRailValue&#47;KingsCrossRailValue' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableausoftware.com&#47;static&#47;images&#47;Ki&#47;KingsCrossRailValue&#47;KingsCrossRailValue&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /></object></div><div style='width:654px;height:22px;padding:0px 10px 0px 0px;color:black;font:normal 8pt verdana,helvetica,arial,sans-serif;'><div style='float:right; padding-right:8px;'><a href='http://www.tableausoftware.com/public/about-tableau-products?ref=https://public.tableausoftware.com/views/KingsCrossRailValue/KingsCrossRailValue' target='_blank'>Learn About Tableau</a></div></div>
</center>

**Notes on rail journeys from London King's Cross**
* As might be expected when starting from a station on the main line, King's Cross journeyers have a much better value ticket than Cambridge folk to pretty much anywhere in the UK.

* Similar regions of the UK are particularly good value. The Glasgow, Birmingham, and Liverpool regions as well as the Yorkshire Dales and coastal towns in Norfolk have great bang for buck.

* Too far away from London and the miles per pound value goes down again (i.e. north Scotland and Cornwall) but in general, Londoners can do very well on a weekend getaway.

***
Birmingham New Street (BHM) - Is it as cheap to leave as to arrive?
***
Best value journey: Sanquhar, Scotland (217 miles for £12.50)

<center>
<script type='text/javascript' src='https://public.tableausoftware.com/javascripts/api/viz_v1.js'></script><div class='tableauPlaceholder' style='width: 654px; height: 929px;'><noscript><a href='#'><img alt='Birmingham Rail Value ' src='https:&#47;&#47;public.tableausoftware.com&#47;static&#47;images&#47;Bi&#47;BirminghamRailValue&#47;BirminghamRailValue&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz' width='654' height='929' style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableausoftware.com%2F' /> <param name='site_root' value='' /><param name='name' value='BirminghamRailValue&#47;BirminghamRailValue' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableausoftware.com&#47;static&#47;images&#47;Bi&#47;BirminghamRailValue&#47;BirminghamRailValue&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /></object></div><div style='width:654px;height:22px;padding:0px 10px 0px 0px;color:black;font:normal 8pt verdana,helvetica,arial,sans-serif;'><div style='float:right; padding-right:8px;'><a href='http://www.tableausoftware.com/public/about-tableau-products?ref=https://public.tableausoftware.com/views/BirminghamRailValue/BirminghamRailValue' target='_blank'>Learn About Tableau</a></div></div>
</center>

**Notes on rail journeys from Birmingham**
* Birmingham is a excellent starting location to get great value rail tickets to most of Scotland. However the Argyll region is not good value. This because stations in this region are the tail end of the western line up from Glasgow. This line only runs two or three trains a day from BHM that can get you to places like Mallaig and Loch Awe on the same day of travel. Stations in the rest of Scotland have more frequent services and are better value as a result.

* The Glasgow - Edinburgh region continues to be excellent value for money, as well as Liverpool, the Lake District, and north Wales.

* Kent is surprisingly good value from Birmingham, given the need to travel through London (Euston and St Pancreas). But by taking the 5:29am train from Birmingham New Street, one can get to Dover and other seaside towns for just £25.50 advance. Note that this not cheaper than a ticket to central London (which is about £20 in advance from BHM), but it is better value because of the greater distance travelled.
