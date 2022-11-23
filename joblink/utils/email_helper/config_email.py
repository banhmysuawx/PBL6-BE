import threading

from django.core.mail import EmailMessage


class _EmailThread(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


def send(data):
    email = EmailMessage(
        subject=data["email_subject"], body=data["email_body"], to=[data["to_email"]]
    )
    _EmailThread(email).start()
