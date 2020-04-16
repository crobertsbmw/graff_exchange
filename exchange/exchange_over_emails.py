from django.core.mail import EmailMessage
from exchange.models import *
assignments = Exchange.this_month().assignments.all()


#This code assumes everyone did a sketch. We should have 3 different emails for people who didn't do sketches.
message = '''Thanks everyone for participating! I kind of screwed some things up, so we had a rough start, but thanks to everyone for being patient with me. There are still a few sketches that I haven't gotten back, so I'll add those in as I get them. Also, I will email them directly to the recipient just to be sure they see it.

Here's a link to review the piece that was done for you:

{link}

And after you answer the questions, it should redirect you so you can see all the pieces.

Thanks again!
-Chase
'''

message_not_completed = '''Thanks everyone for participating! I kind of screwed some things up, so we had a rough start, but thanks to everyone for being patient with me. There are still a few sketches that I haven't gotten back, so I'll add those in as I get them. Also, I will email them directly to the recipient just to be sure they see it.

Here's a link to review all the pieces.

{link}

Thanks again!
-Chase
'''


# we need to redo this for people who get 2 back, etc.

signups =  Exchange.this_month().signups.all()
for signup in signups:
    assignments = signup.favors.filter(completed=True)
    if assignments.count() > 0:
        links = [a.review_link() for a in assignments]
        m = message.replace('{link}', "\n".join(links))
    else:
        link = "https://graffexchange.com/review/"+Exchange.this_month().name.replace(" ", "_")+"/"
        m = message_not_completed.replace('{link}', link)
    print("sending to ", signup.user.email)
    print(m)
    email = EmailMessage('Exchange RESULTS!', m, to=[signup.user.email])
    email.send()


