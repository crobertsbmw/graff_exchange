from django.core.management.base import BaseCommand
from django.core.mail import EmailMessage
from exchange.models import *


message1 = '''{first_name},
Thanks again for signing up for the graff exchange! I just need you to confirm your signup with the link below:

{link}

You can also edit your details if you need to. I'm hoping to get this underway this {date}, so you can expect an email then with your assignment.

Thanks,
Chase
'''
def send_confirmation_email():
    users = Exchange.this_month().users.all()
    message = message1.replace('{date}', Exchange.this_month().assignment_date.strftime('%A'))
    for user in users:
        m = message1.replace('{first_name}', user.name())
        m = m.replace('{link}', user.confirm_link())
        print('*****')
        print("sending to ", assignment.user_signup.user.email)
        print(m)
        email = EmailMessage('Graff Exchange Assignment', m, to=[assignment.user_signup.user.email])
        email.send()

class Command(BaseCommand):
    def handle(self, *args, **options):
        scrape()

