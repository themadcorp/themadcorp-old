import smtplib
from email.mime.text import MIMEText

def send_email(name, email, message):
    FROM_EMAIL='adityaas26@gmail.com'
    FROM_PASSWORD='g.morning@1998'
    message="Hey, You have a new mail from <strong>%s</strong>! <br>Email Id: %s <br>Message: %s" % (name, email, message)
    subject="You have a new mail"
    toList=["adityaas26@gmail.com", "ms.mayank.n1@gmail.com", "devendrasikarwar1508@gmail.com"]

    gmail = smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(FROM_EMAIL,FROM_PASSWORD)

    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=','.join(toList)
    msg['From']=FROM_EMAIL

    gmail.send_message(msg)
