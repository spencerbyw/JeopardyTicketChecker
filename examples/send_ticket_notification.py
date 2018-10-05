import sendgrid
import urllib.request

from sendgrid.helpers.mail import *

SENDER_EMAIL='from@email.com'
RECIPIENT_EMAIL='to@email.com'
SENDGRID_API_KEY='SENDGRID_KEY_HERE'

NO_SHOWTIMES_STR = 'edit-no-showtimes'
YES_SHOWTIMES_STR = 'js-form-item-showtimes'
TICKETS_URL = 'https://www.jeopardy.com/tickets'

TICKETS_AVAILABLE_MESSAGE = f"""\
Hello there!

This email is to inform you that it appears that live tickets are now available on the Jeopardy website!

To see available showtimes please visit {TICKETS_URL}

Have a great day!

Jeopardy Ticket Checker
"""

UNSUCCESSFUL_MESSAGE = """\
Hello!

It appears that something unexpected happened while running the Jeopardy Ticket Checker.
Here's what we know:
%s

Hope you can figure it out!

Jeopardy Ticket Checker
"""

def main():
	try:
		resp = urllib.request.urlopen(TICKETS_URL)
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
	subject = 'Live Jeopardy Tickets are Available!'
	send_email(subject, TICKETS_AVAILABLE_MESSAGE)
	exit(0)

def showtimes_unavailable():
	# Code to execute when showtimes are NOT available
	print('Tickets are not available.')
	exit(1)

def inconclusive():
	# Code to run if it wasn't clear if the
	msg = 'Check was inconclusive. The site may be down, or the site content has changed and this script needs to be updated.'
	print(msg)
	full_message = UNSUCCESSFUL_MESSAGE % msg
	subject = 'Jeopardy Ticket Checker - Warning'
	send_email(subject, full_message)
	exit(1)

def fail(msg):
	# Code to run if the site's down or a bad response is received
	print(msg)
	full_message = UNSUCCESSFUL_MESSAGE % msg
	subject = 'Jeopardy Ticket Checker - Error'
	send_email(subject, full_message)
	exit(1)

def send_email(subject, message):
	sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)
	to_email = Email(RECIPIENT_EMAIL)
	from_email = Email(email=SENDER_EMAIL, name='Jeopardy Ticket Checker')
	content = Content('text/plain', message)
	mail = Mail(from_email, subject, to_email, content)

	# Send the email
	response = sg.client.mail.send.post(request_body=mail.get())
	print('Email sent to %s with response code %s' % (RECIPIENT_EMAIL, response.status_code))

if __name__ == '__main__':
	main()
