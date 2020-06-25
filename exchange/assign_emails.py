from django.core.mail import EmailMessage
from exchange.models import *
assignments = Exchange.this_month().assignments.all()

message = '''{first_name},
Thanks again for signing up for the June exchange! You're going to be writing "{tag}" as a {style}. The deadline for this first sketch is June 24th, and then I'll assign rematches if needed.
When you've got it done, you can upload your sketch using this link:

{link}

Let me know if you have any questions, or have any trouble getting it uploaded.

Thanks,
Chase
'''

for assignment in assignments:
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
    email = EmailMessage('June Exchange Assignment', m, to=[assignment.user_signup.user.email])
    email.send()



# Reminder Email

from django.core.mail import EmailMessage
from exchange.models import *
assignments = Exchange.this_month().assignments.all()

message = '''{first_name},
Quick reminder that the deadline for writing "{tag}" is Tomorrow (Wednesday). Let me know if you have any questions.

Thanks,
Chase
'''

message_rematch = '''{first_name},
Just a quick reminder that deadline for writing "{tag}" is Tomorrow, and then I'll send out the rematches Thursday. Thanks for your help!

Thanks,
Chase
'''

for assignment in assignments:
    if assignment.completed:
        continue
    print('*****')
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
    email = EmailMessage('Pieces due Tomorrow', m, to=[assignment.user_signup.user.email])
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


#REMATCHES -----------------
#find all the people that need a grade
from exchange.models import *
users = User.objects.filter(level=0)

for user in users:
    if user.sketches.all().count() > 0:
        print(user.email, user.moniker, user.pk, user.sketches.all()[0].image.url)

#make assignments
from exchange.models import *
assignments = Exchange.this_month().assignments.filter(completed=False, rematch=False).order_by("-recipient_signup__user__level")
needers = []
for assignment in assignments: #assignment is the original assignment that wasn't completed.
    rematches = Assignment.objects.filter(recipient_signup=assignment.recipient_signup, rematch=True)
    if rematches.count() > 0:
        continue #this user has already been rematched.
    recipient_a = Assignment.objects.get(user_signup=assignment.recipient_signup, style=assignment.style)
    if recipient_a.completed:
        needers.append(assignment.recipient_signup)
        #we need to do a rematch
        print("Needs rematch", assignment.recipient_signup)


doublers = []
doublers_a = Exchange.this_month().assignments.filter(completed=True, user_signup__do_double=True, rematch=False).order_by("-user_signup__user__level")
for doubler in doublers_a:
    rematches = Assignment.objects.filter(user_signup=doubler.user_signup, rematch=True)
    if rematches.count() > 0:
        print(doubler.user_signup, "already doing a rematch")
        continue
    doublers.append(doubler.user_signup)


ddoublers = doublers[:]
nneeders = needers[:]


doublers = ddoublers[:]
needers = nneeders[:]
assignments = []
for needer in needers:
    for doubler in doublers:
        if doubler == needer:
            continue
        #we've already done this assignment
        if Assignment.objects.filter(user_signup__user=doubler.user, recipient_signup__user=needer.user).count() > 0:
            continue
        #The needer drew out the doubler. 
        if Exchange.this_month().assignments.filter(user_signup__user=needer.user, recipient_signup__user=doubler.user).count() > 0:
            continue
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

#Save the assignments if it looks good.
[a.save() for a in assignments]


# doublers = ddoublers[:]
# needers = nneeders[:]
# random.shuffle(needers)
# random.shuffle(doublers)
# assignments = []

# for needer in needers:
#     best_match = None
#     for doubler in doublers:
#         if doubler == needer:
#             continue
#         #we've already done this assignment
#         elif Assignment.objects.filter(user_signup__user=doubler.user, recipient_signup__user=needer.user).count() > 0:
#             continue
#         #The needer drew out the doubler. 
#         elif Exchange.this_month().assignments.filter(user_signup__user=needer.user, recipient_signup__user=doubler.user).count() > 0:
#             continue
#         #perfect level match.
#         elif doubler.user.level == needer.user.level:
#             print("pair", doubler, "->", needer)
#             assignments.append(Assignment(
#                 exchange=Exchange.this_month(),
#                 user = doubler.user,
#                 user_signup = doubler,
#                 recipient = needer.user,
#                 recipient_signup = needer,
#                 style = "piece",
#                 rematch = True,
#             ))
#             doublers.remove(doubler)
#             break
#         if not best_match:
#             best_match = doubler
#         if best_match.user.level < needer.user.level and doubler.user.level > best_match.user.level:
#             best_match = doubler
#             continue
#         if doubler.user.level < needer.user.level:
#             continue
#         elif doubler.user.level > best_match.user.level:
#             continue
#         best_match = doubler
#     else:
#         print("apair", best_match, "->", needer)
#         assignments.append(Assignment(
#             exchange=Exchange.this_month(),
#             user = best_match.user,
#             user_signup = best_match,
#             recipient = needer.user,
#             recipient_signup = needer,
#             style = "piece",
#             rematch = True,
#         ))
#         doublers.remove(best_match)


# #Save the assignments if it looks good.
# [a.save() for a in assignments]


#Send the emails --------------
from django.core.mail import EmailMessage
message = '''{first_name},
Thanks for getting your sketch done on time, and double thanks for being signing up for the rematch! Is Monday (29th) enough time to get it done?
For the reassignment I'm going to have you write "{tag}". Once it's done you can upload it here:

{link}

Thanks again for your help!
Best,
Chase
'''

for assignment in assignments:
    m = message
    name = assignment.user_signup.user.first_name
    if not name:
        name = assignment.user_signup.tag
    m = m.replace('{first_name}', name.title())
    m = m.replace('{link}', assignment.upload_link())
    m = m.replace('{tag}', assignment.recipient_signup.tag)
    print('*****')
    print("sending to ", assignment.user_signup.user.email)
    print(m)
    email = EmailMessage('Rematch Assignment: '+assignment.recipient_signup.tag, m, to=[assignment.user_signup.user.email])
    email.send()