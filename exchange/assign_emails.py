from django.core.mail import EmailMessage
from exchange.models import *
assignments = Exchange.this_month().assignments.all()

message = '''{first_name},
Thanks again for signing up for the exchange! You're going to be writing "{tag}" as a {style}. I'm giving everyone one week to get it done. Then I'll assign the rematches, and after I get all of those back then I'll notify you of the results.
When you've got it done, you can upload your sketch using this link:

{link}

If you have any questions, or have any trouble getting it uploaded you can email me.

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
    m = message
    name = assignment.user_signup.user.first_name
    if not name:
        name = assignment.user_signup.tag
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
Just a reminder that deadline for writing "{tag}" is tomorrow (Monday). If you are working on it, and need more time, just let me know.

Thanks,
Chase
'''
message_rematch = '''{first_name},
Just a reminder that deadline for writing "{tag}" is tomorrow (Monday). If you are working on it, and need more time, just let me know. Then, we'll do rematches if there are any (last month almost everyone followed through, so there was only like one or two rematches which was awesome).

Thanks,
Chase
'''

for assignment in assignments:
    if assignment.completed:
        continue
    print('*****')
    if assignment.user_signup.user.email == 'diedre.m.atkinson@gmail.com':
        print("skipping")
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
    print("sending to ", assignment.user_signup.user.email)
    print(m)
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


#REMATCHES
#find all the people that need a grade
from exchange.models import *
users = User.objects.filter(level=0)

for user in users:
    if user.sketches.all().count() > 0:
        print(user.email, user.moniker, user.pk)

#make assignments
from exchange.models import *
assignments = Exchange.this_month().assignments.filter(completed=False).order_by("-recipient_signup__user__level")
needers = []
for assignment in assignments:
    recipient_a = Assignment.objects.get(user_signup=assignment.recipient_signup, style=assignment.style)
    if recipient_a.completed:
        needers.append(assignment.recipient_signup)
        #we need to do a rematch
        print("Needs rematch", assignment.recipient_signup)

doublers = []
doublers_a = Exchange.this_month().assignments.filter(completed=True, user_signup__do_double=True).order_by("-user_signup__user__level")
for doubler in doublers_a:
    doublers.append(doubler.user_signup)

assignments = []
for needer in needers:
    best_match = None
    for doubler in doublers:
        if doubler == needer:
            continue
        elif Assignment.objects.filter(user_signup__user=doubler.user, recipient_signup__user=needer.user).count() > 0:
            continue
        elif Exchange.this_month().assignments.filter(user_signup__user=needer.user, recipient_signup__user=doubler.user).count() > 0:
            continue
        elif doubler.user.level == needer.user.level:
            print("pair", doubler, "->", needer)
            assignments.append(Assignment(
                exchange=Exchange.this_month(),
                user = doubler.user,
                user_signup = doubler,
                recipient = needer.user,
                recipient_signup = needer,
                style = "piece",
                rematch = True,
            ))
            doublers.remove(doubler)
            break
        if not best_match:
            best_match = doubler
        if best_match.user.level < needer.user.level and doubler.user.level > best_match.user.level:
            best_match = doubler
            continue
        if doubler.user.level < needer.user.level:
            continue
        elif doubler.user.level > best_match.user.level:
            continue
        best_match = doubler

    else:
        print("apair", best_match, "->", needer)
        doublers.remove(best_match)

#--------------

exchange = Exchange.this_month()
assignments = Assignment.objects.filter(exchange=exchange, rematch=True)
for assignment in assignments:
    print(assignment.user.email, assignment.user.moniker, assignment.recipient.moniker, assignment.upload_link())
    

