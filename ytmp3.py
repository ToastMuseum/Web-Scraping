
# Youtube to mp3 converter via webscraping
#
#	[Info]
#		This program allows the user to compile a list of links while browsing youtube and then 
#	convert the list of links into mp3 files using selenium webdriver module to utilize the website
#	'http://www.listentoyoutube.com/'. It then moves the files to a specified default destination. 
#		


# Using selenium webdriver for webscraping
# Using os, shutil, datetime for file moving file to specified folder
#
#


# The user must:
# 	Set default firefox pathway to open firefox in user's default mode
# 	Set default download directory
# 	Set default destination directory
# 	set first download pop-up dialog to "save and do this automatically"



from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time,os,shutil
from datetime import datetime, timedelta


def main():

	browser = OpenConnection()	
	
	# Compile List of youtube links
	youtubeList = []
	
	print('Find a video to convert\n')
	prev = ''
	temp = ''
	
	prompt = True
	
	ignoreLinks = ['https://www.youtube.com/results', 'https://www.youtube.com/channel', 'https://www.youtube.com/playlist','https://www.youtube.com/feed','https://www.youtube.com/upload']
	
	while True:
			
		curr = browser.current_url
		

		if (curr == prev) or (curr.endswith('https://www.youtube.com/') or any(curr.startswith(i) for i in ignoreLinks)):		#if still on same or homepage ignore
			#ignore
			pass
		
		else:					# otherwise ask to add to list or convert list
		
			if prompt == True:
				response = input('Add this video to List [Y/N/Q]?: [Y-Yes/ N-No/ Q-Quit to convert or exit]: ').lower()
				prev = curr
		
			# YES
			if response.startswith('y'):
				print(curr + ': Added to list!\nChoose next video.\n')
				youtubeList.append(curr)
					

				
			# NO		
			elif response.startswith('n'):
			
			
				if not youtubeList:
					print('Got it. Continuing on...\nChoose next video.\n')
				
					prev = curr
					prompt = True
					
				else:
					convert = input('Would you like to convert your list to mp3 Now?  [Y/N]: [Y- Yes Convert/ N-No]: ').lower()
			
					if convert.startswith('y'):
						prompt = True
				
						convertToMp3(browser, youtubeList)
						break
						
			
					elif convert.startswith('n'):	
						print('Got it. Continuing on...\nChoose next video.\n')
				
						prev = curr
						prompt = True
					else:
						print('Sorry that is not a valid input.')
						prev = ''
						prompt = False
				
				
			# QUIT	
			elif response.startswith('q'):
			
				if not youtubeList:
					print('/nExiting...')
					break
				else:
					convert = input('Would you like to convert your list to mp3 Now? [Y/N]: [Y- Yes Convert/ N-No]: ').lower()
			
					if convert.startswith('y'):	
						convertToMp3(browser, youtubeList)
						break
					
					elif convert.startswith('n'):
						print('Quitting...')
						break
					else:	
						print('Sorry That is not a valid input.\n')
						prev = ''
						prompt = False
	
			else:
				print ('Sorry that is not a valid input.')
				prev = ''
				
			
		
		
def convertToMp3(browser, ytList):
	
	
	start_time = datetime.now()
	browser.get('http://www.listentoyoutube.com/')
	
	print('\nConverting List...\n')
	
	time_wait = 4
	
	for item in ytList:
		time.sleep(time_wait/2)
		#inject the youtube link into the form
		try:
			
			pasteElem = browser.find_element_by_css_selector('input')
			pasteElem.send_keys(item)

			goButton = browser.find_element_by_id('go-button').click()
			#goButton.click()
			
			time.sleep(time_wait)
			
			#print('get-download')
			getDownload = browser.find_element_by_link_text('CLICK HERE to get your Download Link').click()
			#getDownload.click()
			
			time.sleep(time_wait)
			downloadMp3 = browser.find_element_by_id('downloadmp3').click()
			
			time.sleep(time_wait)
			browser.get('http://www.listentoyoutube.com/')
			
			time.sleep(time_wait)
	
		except:
			print('Sorry unable to convert song. You may need to check off you are not a robot\n')
			break
	
	
	print('\n...Process Complete\n')
	
	response = input('Move files to a specific folder? [Y/N]: ')
	
	if(response.lower() == 'y'):
		moveFiles(start_time)
	else:
		print('\nExiting...')
	
	
	
def moveFiles (start_time):
	
	print('Moving Files...')
	
	sourcePath = ''
	destinationPath = ''
	
	while True:
	
		if sourcePath == '':
			sourcePath = input('Paste your browser\'s default download folder path [Copy and paste source filepath]: ')
		elif destinationPath  == '':
			destinationPath = input('Where would you like the files to be saved? [Copy and paste destination filepath]: ')
		else:
			break
	
	print('\nlooking for recently added mp3s...\n')
	time.sleep(6)
	
	source = os.listdir(sourcePath)

	
	for file in source:
	
		try:
			#get file timestamp
			file_time = (time.ctime(os.path.getmtime(sourcePath + file))).split(" ")
		
			file_time.pop(0)

			for item in file_time:
				if item == '':
					file_time.remove(item)
		
		 
			if (int(file_time[1]) > 0) and (int(file_time[1]) <10):
				file_time[1] = "0" + file_time[1]
		
			file_time = "".join(file_time)
			file_time_dt = datetime.strptime(file_time, "%b%d%H:%M:%S%Y")
		
			if '.part' in file:
				print(file.encode(), 'partial file dont move')

			elif (file.endswith('.mp3')) and (start_time < file_time_dt):
				
				#print(file.encode(), ' size: ', os.path.getsize(sourcePath+file))
				
				# make sure file is not moved until download is complete
				i =0
				while(os.path.getsize(sourcePath + file) < 30000):		
					#print(file.encode(), ': too small to move')
					i+=1
					time.sleep(6)
					if i>10:
						break
				else:	
					print('moving: ', file.encode())
					if '.part' in file:
						print(file.encode(), 'partial file dont move')
					else:
						shutil.move(os.path.join(sourcePath, file), os.path.join(destinationPath, file))
		
		
		except FileNotFoundError:
			print('Sorry {} not found'.format(file))
			print()
		except UnicodeEncodeError:
			print('UnicodeEncodeError: bad symbols in filename')
		except:
			print('Sorry there was a problem')
	
	print('\n...File Move Complete\n')
	

def OpenConnection():
	
	defaultProfilePath = input('Provide a default firefox profile path [N - to ignore]: ')
	
	if defaultProfilePath != '' :
		if defaultProfilePath.lower() != 'n':
			fp = webdriver.FirefoxProfile(defaultProfilePath)
			print('\nOpening Firefox...\n')
	
			browser = webdriver.Firefox(fp)
	else:
		print('\nOpening Firefox...\n')
	
		browser = webdriver.Firefox()
	
	#open browser to youtube
	browser.get('http://www.youtube.com')
	
	return browser
		
			
	
	
if __name__ == "__main__":

	main()
	


	

