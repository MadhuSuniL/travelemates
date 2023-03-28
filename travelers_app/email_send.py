from django.core.mail import EmailMessage
from threading import Thread

class EmailThread(Thread):
    
    def __init__(self, subject, html, from_email, recipient_list):
        self.subject = subject
        self.body = html
        self.from_email = from_email
        self.recipient_list = recipient_list
        Thread.__init__(self)

    def run(self):
        try:
            msg = EmailMessage(self.subject, self.body, self.from_email, self.recipient_list)
            msg.content_subtype = "html"            
            msg.send()
        except Exception as e:
            pass
            print(e)
