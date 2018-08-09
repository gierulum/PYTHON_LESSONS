import smtplib
import string

value_list = [[1, "First" ],
         [2, "Second" ]]

for x in value_list:
	print (x[0])
	f_elem = x[0]
	print (x[1])
	sec_elem = x[1]

	#multiple mails [mail, mail, mail] >>> msg['To'] = ", ".join(recipients)
value =  "BARCA!!"

HOST = "smtp.gmail.com"
SUBJECT = "TYTUL MAILA"
TO = "mail__adress"
FROM = "mail__adress"
text = "TRESC MAILA!!"
BODY = "".join((
        "From: %s" % FROM,
        "To: %s" % TO,
        "Subject: %s" % SUBJECT ,
        "",
        value
        ))
server = smtplib.SMTP(HOST)
server.login("mail__adress", "Password")
server.sendmail(FROM, TO, BODY)
server.close()
