from django.core.mail import EmailMessage
from exchange.models import *


#This code assumes everyone did a sketch. We should have 3 different emails for people who didn't do sketches.
message = '''Another month! There a still some sketches that I haven't gotten back yet, I'll email those out directly, and update the site as they come in. And here's a link to view the sketches:

{link}

Let me know if you have any questions or suggestions, and thanks again for participating! See you next month.
Best,
Chase
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
        m = message.replace('{link}', link)
    print("sending to ", signup.user.email)
    print(m)
    email = EmailMessage('Exchange RESULTS!', m, to=[signup.user.email])
    email.send()


