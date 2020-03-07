from django.core.management.base import BaseCommand
from django.core.mail import EmailMessage
from exchange.models import *


message1 = '''{first_name},
Thanks again for signing up for the graff exchange! I just need you to confirm your signup with the link below:

{link}

You can also edit your details if you need to. I'm hoping to get this underway this on {date}, so you can expect an email then with your assignment.

Thanks,
Chase
'''

message2 = '''{first_name},
Hey, we're starting the next Exchange this {date}, if you want to join this month, go ahead and click this link and you can confirm your details.

{link}

Let me know if you have any questions or concerns.

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
        print("sending to ", user.email)
        print(m)
        email = EmailMessage('Confirm Graff Exchange Signup', m, to=[user.email])
        email.send()

    two_months_ago = datetime.datetime.now() - datetime.timedelta(days=70)
    sketches = Sketch.objects.filter(datetime__gt=two_months_ago)
    user_pks = list(set([s.user_id for s in sketches]))
    users = User.objects.filter(user_pk__in=user_pks).exclude(user_pk__in=[u.id for u in users])
    
    message = message1.replace('{date}', Exchange.this_month().assignment_date.strftime('%A'))
    for user in users:
        m = message1.replace('{first_name}', user.name())
        m = m.replace('{link}', user.confirm_link())
        print('*****')
        print("sending to ", user.email)
        print(m)
        email = EmailMessage(datetime.datetime.now().strftime("%b Exchange?"), m, to=[user.email])
        email.send()


class Command(BaseCommand):
    def handle(self, *args, **options):
        scrape()

