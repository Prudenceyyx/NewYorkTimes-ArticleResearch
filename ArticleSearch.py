# Python version 2.7
# By typing "python2 ArticleResearch.py <keyword>",
# it returns:
# Searching <keyword>
# ====================
# <pub_date>        <Headline>
# ...
# ====================
# API of Article Search of New York Times is necessary,
# which you can acquaire here
# https://developer.nytimes.com/
# Documents: https://developer.nytimes.com/article_search_v2.json#/README

import json, requests,sys
# from pprint import pprint


# It's easier to check data structure by using pprint
# pprint(data)

# input nothing, output processed keyword from terminal
# exit if there is no keyword
def get_key():
	# Test if the user input keyword
	if len(sys.argv)<2:
		print "Warning: Use an argument as a search key"
		print "type: python2 <filename> <searchkey>"
		sys.exit()

	#Process the keyword if it contains multiple words and space
	searchkey="%20".join(sys.argv[1:])
	return searchkey

# input processed keyword, output API response
def get_data(searchkey):
	# Apikey can be acquaired here
	# https://developer.nytimes.com/
	apikey="" 
	url="https://api.nytimes.com/svc/search/v2/articlesearch.json?"

	url=url+"q="+searchkey
	url=url+"&api-key:"+apikey

	resp = requests.get(url)
	data = json.loads(resp.text)
	return data

# Input API response, print entries in the dictionary which is the first element of data list
# Or u can try pprint(data) to see if the data is constructured by dictionaries
def check_data_structure(data):
	for key in data["response"]["docs"][0]:
		print key

# input processed searchky, print date and headline
def get_date_and_headline(searchkey):
	data=get_data(searchkey)
	articles=data["response"]["docs"]
	for i in articles:
		print i["pub_date"][:10]+"    "+i["headline"]["main"]
		print "\t\t\t"+i["web_url"]
		print ""

def main():
	searchkey=get_key()
	print "Searching "+searchkey+" ..."
	print "="*20
	# check_data_structure(get_data(searchkey))
	get_date_and_headline(searchkey)
	print "="*20
	print ""

main()