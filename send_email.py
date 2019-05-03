from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_email(name, email, msg):
    
    data = {
        "personalizations": [
            {
            "to": [{
                    "email": "adityaas26@gmail.com"
                }, {
                    "email": "ms.mayankn1@gmail.com"
                }, {
                    "email": "devendrasikarwar1508@gmail.com"
                }, {
                    "email": "themadcorp3@gmail.com"
                }],
            "subject": "Someone approached from the website"
            }
        ],
        "from": {
            "email": "themadcorp3@gmail.com"
        },
        "content": [
            {
            "type": "text/html",
            "value": "Hey, You have a new mail from <strong>{}</strong>! <br>Email Id: {} <br><br>Message: {}".format(name, email, msg)
            }
        ]
    }
    try:
        sg = SendGridAPIClient('SendGrip-API-key')
        response = sg.client.mail.send.post(request_body=data)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)
