#!/usr/bin/env python
import sys

# Mapper to return Donald Trump's top 10 states
# Data source: 
# Data header: "States" "Donald Trump" "Hillary Clinton"

# Initialise a list to store the top N records as a collection of touples (Donald Trump, record)
myList = []
n = 10	# Number of top N records

for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	# split data values into list
	data = line.split(",")
	
	# convert Donald Trump (currently a string) to int
	try:
		Donald_Trump = int(data[1])
	except ValueError:
		# ignore/discard this line
		continue
	
	# add (Donald Trump, record) touple to list
	myList.append( (Donald_Trump, line) )
	# sort list in reverse order
	myList.sort(reverse=True)
	
	# keep only first N records
	if len(myList) > n:
		myList = myList[:n]
		
# Print top N records
for (k,v) in myList:
	print(v)