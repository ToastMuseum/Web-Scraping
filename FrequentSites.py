#
#	Open your most visited websites at once instead of one by one
#


# Need To:
#	1. go through list of user determined sites
#	2. webbrowser.open() each item

# User:
#	1. open browser
#	2. run script


# Will not work without browser open first. Race condition occurs. when this opens the next url in list 
#		it is unable to open a tab because the previous window has not resolved. webbrowser.open() defaults
#		to opening a new window.


#	Import Modules
import webbrowser


userURL = ['http://facebook.com','http://amazon.com','http://google.com','http://youtube.com','http://wikipedia.org']

for url in userURL:
	webbrowser.open(url, 2)




# TODO: Store user defined websites in JSON/CSV/txt/ whatever file format
# TODO: Read values from JSON/CSV/txt/etc file 

