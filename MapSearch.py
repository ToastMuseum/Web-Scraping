

# Open the web browser to address on GoogleMaps and
#		 automatically search a street address gathered from cmdline arguments or clipboard

# Need To:
#	1. read the command line arguments from sys.argv
#	2. read clipboard contents from pyperclip
#	3. call webbrowser.open() with webbrowser


#User Can:
#	1. Highlight Address
#	2. copy/ ctrl+c
#	3. run MapSearch.py

#		OR

#	1. run 'MapSearch.py [address]'




# Import Modules
import webbrowser, sys, pyperclip


if len(sys.argv)> 1:
	# Get address from cmdline
	address = ' '.join(sys.argv[1:])
	
	print(address)
else:
	# Get address from clipboard
	address = pyperclip.paste()
	
	print(address)
	
webbrowser.open('https://google.com/maps/place/' + address)



