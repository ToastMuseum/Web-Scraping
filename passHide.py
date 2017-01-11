
#python35

# get Password using msvcrt and sys
# replace typed keys with asterisks


# <backspace> to delete characters
# <escape> to cancel
# <enter> submit password


def hidePassword():
	import msvcrt,sys
	sys.stdout.write('Enter Password: ')	
	sys.stdout.flush()
	
	raw_password = []
	
	while True:
		character = msvcrt.getch()
		
		if ord(character) == 27:									#escape
			break
		elif ord(character) == 8:									#backspace
			if(len(raw_password) >= 1):
				sys.stdout.write('\b \b')
				sys.stdout.flush()

				raw_password.pop()
		elif ord(character) == 13: 									#enter
			return raw_password
			break
		elif (character == b'\xe0'):								# Arrow Keys
			if (msvcrt.getch() in (b'H', b'M', b'K', b'P')):
				continue
		elif ord(character) > 32 and ord(character) < 127:
				sys.stdout.write('*')
				sys.stdout.flush()
				raw_password.append(bytes.decode(character))
		else:
			pass
			
	
if __name__ == "__main__":
	
	password = hidePassword()
	
	
	print(password) if password else print('')