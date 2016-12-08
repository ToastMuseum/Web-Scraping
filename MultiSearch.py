
# multiSearch.py - opens multiple google search engine results

#	1. Get search keywords from command line arguments (sys module)
#	2. Retrieve the search results page (requests module)
#	3. Find links to each search result (bs4 module)
#	4. Open a browser tab for each result (webbrowser module)
#	 
#
#	User Must have default web browser already opened
#		if not a new window will open per result



# import modules
import webbrowser, requests, bs4, sys 

# Display text while downloading results page
print('Searching...')

# Get search keywords from command line arguments 
# retrieve top search result links
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()



# Find links to each search result
soup = bs4.BeautifulSoup(res.text, "html.parser")

# select all elements named <a> withing all elements that use a CSS class attibute named 'r'
searchElems = soup.select('.r a')

if (len(searchElems)) > 2:
	print(str(len(searchElems)) +' results found: opening 3...')
	# Open browser tab for each result
	
	numTabs = min(3, len(searchElems))	#open a minimum of 3 tabs
	for i in range(numTabs):
		webbrowser.open('http://google.com' + searchElems[i].get('href')) 
		
# open browswer tab for first result if there are less than 3 results		
elif (len(searchElems)) > 0:
	print(str(len(searchElems)) +' results found: opening first...')
	
	webbrowser.open('http://google.com' + searchElems[0].get('href')) 
	
else:
	print(str(len(searchElems)) +' results found: ')
	
	

# TODO: Add more than one search engine option	