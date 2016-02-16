import urllib    #library for fetching internet resources
import json      #library for json operations
import os
title=os.environ["word"]
# title = raw_input("Enter word to search: ") #Input word to search dictionary
# print "Word: ",title
 
#stores the json formatted output to a variable
url = 'http://glosbe.com/gapi/translate?from=eng&dest=eng&format=json&phrase='+title+'&pretty=true'
 
#json representation of url is stored in variable result
result = json.load(urllib.urlopen(url)) 
 
#get the first text in "meaning" in "tuc" from result
result = result["tuc"][0]["meanings"][:3]
for mean in result:
	print "Meaning: " +  mean['text']
