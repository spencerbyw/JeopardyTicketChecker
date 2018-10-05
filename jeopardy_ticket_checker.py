import urllib.request

NO_SHOWTIMES_STR = 'edit-no-showtimes'
YES_SHOWTIMES_STR = 'js-form-item-showtimes'
url = 'https://www.jeopardy.com/tickets'

def main():
	try:
		resp = urllib.request.urlopen(yup_url)
		resp_content = resp.read()
		content = resp_content.decode('utf-8')
	except Exception as e:
		msg = 'Something broke while trying to access, read, or decode from the url provided.'
		msg += ' Error Message: ' + str(e)
		fail(msg)

	if NO_SHOWTIMES_STR in content:
		showtimes_unavailable()
	elif YES_SHOWTIMES_STR in content:
		showtimes_available()
	else:
		inconclusive()

def showtimes_available():
	# Code to execute when showtimes are available
	print('Tickets are available!')
	exit(0)

def showtimes_unavailable():
	# Code to execute when showtimes are NOT available
	print('Tickets are not available.')
	exit(1)

def inconclusive():
	# Code to run if it wasn't clear if the
	print('Check was inconclusive. The site may be down, or the site content has changed and this script needs to be updated.')
	exit(1)

def fail(msg):
	# Code to run if the site's down or a bad response is received
	print(msg)
	exit(1)

if __name__ == '__main__':
	main()
