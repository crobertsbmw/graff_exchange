from django.core.mail import EmailMessage
from exchange.models import *
assignments = Exchange.this_month().assignments.all()


#This code assumes everyone did a sketch. We should have 3 different emails for people who didn't do sketches.
message = '''Thanks everyone for participating in this, especially if this was your first time and you were maybe hesitant. This month I thought went really well. We only had two or three pieces not get finished during the first week, which was awesome (the first month we did this about 50% didn't follow through).

Here's a link to review the piece that was done for you, and a couple survey questions:

{link}

After you do the survey it should redirect you so you can see all the pieces that were done.

Thanks again, and of course let me know if you have any suggests or questions.
-Chase
'''


for assignment in assignments:
    m = message.replace('{link}', assignment.review_link())
    print('*****')
    print("sending to ", assignment.recipient_signup.user.email)
    print(m)
    email = EmailMessage('Exchange RESULTS!', m, to=[assignment.recipient_signup.user.email])
    email.send()

