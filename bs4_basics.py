


import requests, bs4

res = requests.get('http://www.codingbat.com/python')
res.raise_for_status()

mySoup = bs4.BeautifulSoup(res.text, "html.parser")
print(type(mySoup))

# pull and return a list of all elements with a <p> tag within the HTML. Store each Tag object in myElems
pElems = mySoup.select('p')
print(type(pElems))

# identify if there was a match: value>0
print(len(pElems))

print(type(pElems[0]))

# return string that includes the opening/closing tags also
print(str(pElems[0]))

# '.attrs' returns a dictionary containing the element's id and value: 
#		For (<p class = "slogan">Better Call Saul!</p>) 
#			pElems[0].attrs would return {'class' : ['slogan']}
#				attribute id: 'class'
#				value of id attribute: ['slogan']	
pElems[0].attrs


# print the text of every p element found
for i in range(0, len(pElems)):
	
	# getText() returns the text within the tag elements (ex: <p> Hello Friend </p>)
	pElems[i].getText()	
	
	
	#store all <span> element matches 
spanElems = mySoup.select('span')

	#store the first <span> element matches
firstSpanElem = mySoup.select('span')[0]


# get() method returns the attribute value from the attribute id
#		For Example: (<p class = "slogan">Better Call Saul!</p>)  
#			get() returns slogan
print('firstSpanElem.attrs: ', firstSpanElem.attrs)
print()
print('firstSpanElem.get(\'style\'): ', firstSpanElem.get('style'))

















	
