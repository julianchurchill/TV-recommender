#!/usr/bin/env python
#python guardian and Radio Times highlights parser from kbuss.co.uk
#to be used with TV Wish
from xml.dom import minidom
import os
import urllib
import time
import datetime
import re
import urllib2
from BeautifulSoup import BeautifulSoup

################## UPDATE THESE FIELDS ####
#filename = "/home/user/recommendations.txt"
filename = "recommendations.txt"
unwanted_titles = ['CSI: Miami','The Apprentice',] #list shows you will never want
unwanted_channels = ['Sky2', 'Watch', 'Sky Living, HD', 'Sky Premiere', 'Sky Atlantic', 'Sky Arts 1, HD'] #list channels you don't receive
rt_commented = "false" #change this value to true to comment out the radiotimes sugggestions
g_commented = "false" #change this value to true to comment out the radiotimes sugggestions
minstars = 4 #set the minimum number of stars required for films
include_films = "true" 
########################################

url = 'http://www.radiotimes.com/tv/recommendations?genre='
try:
	doc = urllib2.urlopen(url)

	soup = BeautifulSoup(doc)
	items = soup.findAll('article')
	
	titles = []
	unwanted = []
	
	record = open(filename, 'w')
	date = str(datetime.date.today())
	record.write("%s" %("#Radio Times highlights on "))
	record.write("%s" %(date))
	i = 0
	size = len(items)
	d = (size - 2)
	for item in items:
		if (0<i<d):
			title = (item.find('a')).string	
			title = title.encode('ascii','ignore')
			titles.append(title)
			channel = (item.find('dd')).string
			description = (item.find('p')).string
			if not title in unwanted_titles:
				if not channel in unwanted_channels:
					if rt_commented == "true":
						text = "#Show: "+title
					else:
						text = "Show: "+ title 
					record.write("\n%s" %(text))
					describe = "#" 
					if description != None:
						describe += description
					record.write("\n%s" %(describe))
				else:
					unwanted.append(title)
			else:
				unwanted.append(title)				
		i = (i+1)
except urllib2.URLError:
    print "Error opening RadioTimes website"

minstars = minstars - 1
    
if include_films == "true":    
	furl = 'http://www.radiotimes.com/film/film-on-tv'
	
	fdoc = urllib2.urlopen(furl)

	soup = BeautifulSoup(fdoc)
	items = soup.findAll('article')
	date = str(datetime.date.today())
	i = 0
	size = len(items)
	d = (size - 2)
	for item in items:
		if (0<i<d):
			title = (item.find('a')).string	
			titles.append(title)
			stars = (item.find('dd')).string
			starrate = "# Stars:" + stars
			stars = int(stars)
			
			if (stars>minstars):
				channel = (item.find("dd", "channel")).string			
				description = (item.find('p')).string
				if not title in unwanted_titles:
					if not channel in unwanted_channels:
						if rt_commented == "true":
							text = "# "+title
						else:
							text = title 
						record.write("\n%s" %(text))
						
						record.write("\n%s" %(starrate))
						describe = "#" + description
						record.write("\n%s" %(describe))
					else:
						unwanted.append(title)
				else:
					unwanted.append(title)		
			else:
				unwanted.append(title)		
		i = (i+1)

#################
day = datetime.date.isoweekday(datetime.date.today())
if day < 6:
	clean = []
	for x in unwanted:
	    x = str(x)
	    x = x.encode('ascii','ignore')
	    clean.append(x)
	unwanted = clean

	gfilename = "/home/katy/Dropbox/TVWish/guardiantorecord.txt"

	gurl = "http://www.guardian.co.uk/culture/series/watchthis/rss"
	gdoc = minidom.parse(urllib.urlopen(gurl))
	description = gdoc.getElementsByTagName('description')[1].firstChild.nodeValue
	description =description.encode('UTF-8')
	clean = []
	for x in titles:
	    x = str(x)
	    x = x.encode('ascii','ignore')
	    clean.append(x)
	titles = clean
	temptitles = []
	temptitles = re.findall('</p><h2>(.*?)<br />', description)
	gtitles = []
	[gtitles.append(i) for i in temptitles if not gtitles.count(i)]
	notunwanted = []
	[notunwanted.append(i) for i in gtitles if not unwanted.count(i)]
	tempgtitles = []
	[tempgtitles.append(i) for i in notunwanted if not titles.count(i)]
	notlisted = []
	[notlisted.append(i) for i in tempgtitles if not unwanted_titles.count(i)]

	gtitles = notlisted
	record.write("\n%s" %("########### and from the Guardian: "))
	for title in gtitles:
		needle = "</p><h2>"+ title +"<br />"
		d = (description.find(needle)+(len(needle)))
		e = description[d:(d+1000)]
		f = e.find("<em>")
		g = e[0:f]
		desc = "# "+ (g)
		if g_commented == "true":
			text = "#Show: "+title
		else:
			text = "Show: "+ title
		record.write("\n%s" %(text))
		record.write("\n%s" %(desc))

	record.close()

