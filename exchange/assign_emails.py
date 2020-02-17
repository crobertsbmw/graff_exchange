from django.core.mail import EmailMessage
from exchange.models import *
assignments = Exchange.this_month().assignments.all()

message = '''{first_name},
Thanks again for signing up for the exchange! You're going to be writing "{tag}" as a {style}. I'm giving everyone one week to get it done. Then I'll assign the rematches, and after I get all of those back then I'll notify you of the results.
When you've got it done, you can upload your sketch using this link:

{link}

Of course, if you have any questions, or have any trouble getting it uploaded you can email me.

Thanks,
Chase
'''
message_friend = '''{first_name},
Thanks again for signing up for the exchange! I appreciate that you haven't given up on this yet. You're going to be writing "{tag}" as a {style}. I'm trying to match the experienced people together so hopefully you get something back that your happy with. 
I'm giving everyone one week to get it done. Then I'll assign the rematches, and after I get all of those back then I'll notify you of the results.
When you've got it done, you can upload your sketch using this link:

{link}

Of course, if you have any questions, or have any trouble getting it uploaded you can email me.

Thanks for making these awesome!
Best,
Chase
'''

for assignment in assignments:
    if assignment.user_signup.user.level > 6:
        m = message_friend
    else:
        m = message
    name = assignment.user_signup.user.first_name
    if not name:
        name = assignment.user_signup.tag
    if name != "Leighton":
        continue
    m = m.replace('{first_name}', name)
    m = m.replace('{link}', assignment.upload_link())
    m = m.replace('{tag}', assignment.recipient_signup.tag)
    m = m.replace('{style}', assignment.style)
    print('*****')
    print("sending to ", assignment.user_signup.user.email)
    print(m)
    email = EmailMessage('Graff Exchange Assignment', m, to=[assignment.user_signup.user.email])
    email.send()



# Reminder Email

from django.core.mail import EmailMessage
from exchange.models import *
assignments = Exchange.this_month().assignments.all()

message = '''{first_name},
Just a reminder that the deadline for sketches is Monday. So you have two days to finish your sketch for "{tag}". Then we're going to do rematches for people who didn't get one back, so it'll probably be another week before I release all the results.

Thanks,
Chase
'''
message_rematch = '''{first_name},
Just a reminder that the deadline for sketches is Monday. So you have two days to finish your sketch for "{tag}". Then, if your still up for it, I might ask you to do another for the rematch. If I do need you to do another, how much time do you think you would need? Would 5 days be enough?

Thanks,
Chase
'''

for assignment in assignments:
    if assignment.completed:
        print("continueing")
        continue
    if assignment.user_signup.user.email == 'LeightonJaco@gmail.com':
        print("leghton")
        continue
    if assignment.user_signup.do_double:
        m = message_rematch
    else:
        m = message
    name = assignment.user_signup.user.first_name
    if not name:
        name = assignment.user_signup.tag
    m = m.replace('{first_name}', name)
    m = m.replace('{tag}', assignment.recipient_signup.tag)
    print('*****')
    print("sending to ", assignment.user_signup.user.email)
    # print(m)
    email = EmailMessage('Graffiti Exchange Reminder', m, to=[assignment.user_signup.user.email])
    email.send()



from django.core.mail import EmailMessage
from exchange.models import *
assignments = Exchange.this_month().assignments.all()

message = '''{first_name},
Last reminder, sketches are due today, and I still haven't gotten one back from you.

Thanks,
Chase
'''
message_rematch = '''{first_name},
Just a reminder that the deadline for sketches is Monday. So you have two days to finish your sketch for "{tag}". Then, if your still up for it, I might ask you to do another for the rematch. If I do need you to do another, how much time do you think you would need? Would 5 days be enough?

Thanks,
Chase
'''

for assignment in assignments:
    if assignment.completed:
        print("continueing")
        continue
    if assignment.user_signup.user.email == 'LeightonJaco@gmail.com':
        print("leghton")
        continue
    name = assignment.user_signup.user.first_name
    if not name:
        name = assignment.user_signup.tag
    m = m.replace('{first_name}', name)
    m = m.replace('{tag}', assignment.recipient_signup.tag)
    print('*****')
    print(assignment.user_signup.user.email, name)
    # print("sending to ", assignment.user_signup.user.email)
    # print(m)
    # email = EmailMessage('Graffiti Exchange Reminder', m, to=[assignment.user_signup.user.email])
    # email.send()

