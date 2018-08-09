import smtplib

#message = '''From: From Person ME'''

#content = message




value_list = [[1, "First" ],
         [2, "Second" ]]

for x in value_list:
	print (x[0])
	f_elem = x[0]
	print (x[1])
	sec_elem = x[1]

	#multiple mails [mail, mail, mail] >>> msg['To'] = ", ".join(recipients)
	
	value =  'BARCA!!'

	message = """\From: JA <mail__adress>
To: Drugie ja <mail_second>
Content-type: text/html
Subject: SMTP HTML TEST TITLE

<b>This is HTML message.</b>
<h1>This is headline.</h1>
<table>
<tr>
<td>a</td>
<td>1</td>
</tr>
<tr>
<td bgcolor = red>b</td>
<td>2</td>
</tr>
<tr>
<td bgcolor = blue> %s </td>
<td> %s </td>
</tr>
</table>

""" % (f_elem, sec_elem)

	mail = smtplib.SMTP('smtp.gmail.com', 587)
	mail.ehlo()
	mail.starttls()
	mail.login('mail__adress', 'Password')

#from, reeiver, content
	mail.sendmail('mail__adress', 'mail__adress', message, 'abcdsd' )
	mail.close()