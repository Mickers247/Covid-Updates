import smtplib

carriers = {
	'att':    '@mms.att.net',
	'tmobile':' @tmomail.net',
	'verizon':  '@vtext.com',
	'sprint':   '@messaging.sprintpcs.com'
}

def send(message, number, carrier):
	to_number = number + '{}'.format(carriers[carrier])
	print(to_number)
	auth = ('email', 'password')

	# Establish a secure session with gmail's outgoing SMTP server
	server = smtplib.SMTP( "smtp.gmail.com", 587 )
	server.starttls()
	print("logging in")
	server.login(auth[0], auth[1])
	print("logged in")

	# Send text message through SMS gateway of destination number
	server.sendmail( auth[0], to_number, message)
