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
	'SQ':'Square',
	'CI':'Circle',
	'WK':'Walk',
	'PT':'Point',
	'PW':'Parkway',
	'CTR':'Center',
	'LP':'Loop',
	'CM':'Common',
	'TR':'Terrace',
	'TE':'Terrace',
	'CV':'Cove',
	'PZ':'Plaza',
	'AL':'Alley'
}

directions = {
	'N': 'North',
	'S': 'South',
	'E': 'East',
	'W': 'West',
	'NE': 'Northeast',
	'NW': 'Northwest',
	'SE': 'Southeast',
	'SW': 'Southwest',
	'WB': 'Westbound',
	'EB': 'Eastbound'
	}

cities =[]

def fixCap(name):
	return string.capwords(name)

def filterTags(tags):
	if tags is None:
		return
	newtags = {}
	newtags['addr:city'] = fixCap(tags['CITY'])
	#newtags['addr:country']= 'US'
	#newtags['addr:state']='CA'
	newtags['addr:housenumber'] = tags['ST_NUM']
	newtags['addr:postcode'] = tags['ZIPCODE']
	streetName = fixCap(tags['FEANME'])
	try:
		if(tags['FEATYP'] is not ''):
			streetName = streetName+" "+road_types[tags['FEATYP']]
		if(tags['DIRPRE'] is not ''):
			streetName = directions[tags['DIRPRE']]+" "+streetName
		if(tags['DIRSUF'] is not ''):
			streetName = streetName +" "+directions[tags['DIRSUF']]
		if(tags['UNIT'] is not ''):
			newtags['addr:unit'] = tags['UNIT']
		newtags['addr:street']=streetName
	except:
		print streetName +' '+ tags['FEATYP'] + ' ' + tags['CITY']
		print tags
	if(not tags['CITY']):
		print tags
	return newtags
