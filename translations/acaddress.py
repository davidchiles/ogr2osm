from osgeo import ogr
import re
import urllib
import json
import string

road_types = {
	'WY':'Way',
	'ST':'Street',
	'DR':'Drive',
	'RD':'Road',
	'BL':'Boulevard',
	'AV':'Avenue',
	'CT':'Court',
	'DR':'Drive',
	'LA':'Lane',
	'HW':'Highway',
	'PA':'Path',
	'PL':'Place',
	'TE':'Terrace',
	'SQ':'Square',
	'CI':'Circle',
	'WK':'Walk'
}

directions = {
	'N': 'North',
	'S': 'South',
	'E': 'East',
	'W': 'West',
	'NE': 'Northeast',
	'NW': 'Northwest',
	'SE': 'Southeast',
	'SW': 'Southwest'}

cities =[]

def fixCap(name):
	return string.capwords(name)

def filterTags(tags):
	print tags['CITY']
	if( tags['CITY'] not in cities): 
		cities.append(tags['CITY'])
		print tags['addr:city']
	if tags is None:
		return
	newtags = {}
	if (tags['CITY'] == 'BERKELEY'):
		newtags['addr:city'] = fixCap(tags['CITY'])
		#newtags['addr:country']= 'US'
		#newtags['addr:state']='CA'
		newtags['addr:housenumber'] = tags['ST_NUM']
		newtags['addr:postcode'] = tags['ZIPCODE']
		streetName = fixCap(tags['FEANME'])
		if(tags['FEATYP'] is not ''):
			streetName = streetName+" "+road_types[tags['FEATYP']]
		if(tags['DIRPRE'] is not ''):
			streetName = directions[tags['DIRPRE']]+" "+streetName
		if(tags['DIRSUF'] is not ''):
			streetName = streetName +" "+directions[tags['DIRSUF']]
		if(tags['UNIT'] is not ''):
			newtags['addr:unit'] = tags['UNIT']
		newtags['addr:street']=streetName
	return newtags
