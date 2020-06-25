from django.core.mail import EmailMessage
from exchange.models import *


#This code assumes everyone did a sketch. We should have 3 different emails for people who didn't do sketches.
message_not_completed = '''Sorry we ran so late on this, but thanks for everyone who participated. Here's a link to view all the results. 

{link}

Let me know if you have any questions or suggestions.
Best,
Chase
'''

message_rematched = '''{first_name}, thanks so much for doing the rematch, and I appreciate the responsiveness. Sorry that I ran so late on this. But here's the link you've been waiting for:

{link}

Let me know if you have any questions or suggestions, and thanks again for participating! See you next month.
Best,
Chase
'''

message_completed = '''{first_name}, thanks so much for participating and getting your sketch done! Sorry that I ran so late on this. But here's the link you've been waiting for:

{link}

Let me know if you have any questions or suggestions, and thanks again for participating! See you next month.
Best,
Chase
'''

message_no_sketch = '''{first_name}, thanks so much for participating and getting your sketch done! I hate to say this, but the person assigned to you dropped the ball, and then the person assigned to pick up the slack hasn't delivered yet. But I'll forward the sketch to you if and when I get it. Sorry about the disappointment. Here's a link to all the completed sketches:

{link}

Let me know if you have any questions or suggestions, and thanks again for participating! Hopefully we better luck next month.
Best,
Chase
'''

exchange = Exchange.this_month()
signups =  exchange.signups.all()

for signup in signups:
    m = message_not_completed
    assignments = signup.favors.filter(completed=True)
    if signup.assignments.filter(rematch=True, completed=True).count() > 0:
        m = message_rematched
    elif signup.assignments.filter(completed=True).count() > 0:
        m = message_completed
        if assignments.count() == 0:
            m = message_no_sketch
    if assignments.count() > 0:
        links = [a.review_link() for a in assignments]
        m = m.replace('{link}', "\n".join(links))
    else:
        link = "https://graffexchange.com/review/"+exchange.name.replace(" ", "_")+"/"
        m = m.replace('{link}', link)
    m.replace('{first_name}', signup.user.name())
    print("sending to ", signup.user.email)
    print(m)
    email = EmailMessage('Exchange RESULTS!', m, to=[signup.user.email])
    email.send()


