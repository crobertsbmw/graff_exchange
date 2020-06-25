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
I just set the dates for the June exchange. Again, we are starting a little late this month, and the deadline for signing up is going to be this {date}, if you want to participate this month, click the link and can confirm your details.

{link}

And, of course, let me know if you have any questions.

Best,
Chase
'''

def send_confirmation_email():
#     users = Exchange.this_month().users.all()
#     message = message1.replace('{date}', Exchange.this_month().assignment_date.strftime('%A'))
#     for user in users:
#         m = message.replace('{first_name}', user.name())
#         m = m.replace('{link}', user.confirm_link())
#         print('*****')
#         print("sending to ", user.email)
#         print(m)
#         email = EmailMessage('Confirm Graff Exchange Signup', m, to=[user.email])
#         email.send()

    signups = Signup.objects.filter(exchange=Exchange.this_month())
    two_months_ago = datetime.datetime.now() - datetime.timedelta(days=170)
    sketches = Sketch.objects.filter(datetime__gt=two_months_ago)
    user_pks = list(set([s.user_id for s in sketches]))
    users = User.objects.filter(pk__in=user_pks).exclude(pk__in=[s.user_id for s in signups])
    message = message2.replace('{date}', Exchange.this_month().sign_up_date.strftime('%A'))
    
    for user in users:
        m = message.replace('{first_name}', user.name())
        m = m.replace('{link}', user.confirm_link()+"?do_double=True")
        print('*****')
        print("sending 2 ", user.email)
        print(m)
        email = EmailMessage(datetime.datetime.now().strftime("%B Exchange?"), m, to=[user.email])
        email.send()


class Command(BaseCommand):
    def handle(self, *args, **options):
        scrape()

