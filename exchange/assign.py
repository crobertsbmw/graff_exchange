from exchange.models import *

#get the exchange we want to make assignments for
exchange = Exchange.latest()
signups = exchange.signups.all() # get our users

#sort by style
handstylers = list(signups.filter(style="handstyle").all().order_by("-user__level"))
for a,b in zip(handstylers, handstylers[1:]+handstylers[:1]):
    Assignment(
        exchange=exchange,
        user = a,
        recipient = b,
        style = "handstyle",
        rematch = False,
        moniker = b.moniker
    ).save()
    

throwers = list(signups.filter(style="throwie").all().order_by("-user__level"))
#put all the newbies with eachother. and match the two remaining because they are similar level
for a,b in zip(throwers, throwers[1:]+throwers[:1]):
    Assignment(
        exchange=exchange,
        user = a,
        recipient = b,
        style = "throwie",
        rematch = False,
        moniker = b.moniker
    ).save()



#match the 10's 9's and 8'
piecers = list(signups.filter(style="piece").all().order_by("-user__level"))
for u in piecers:
    print(u.level, u.moniker)

for a,b in zip(piecers, piecers[1:]+piecers[:1]):
    print(a, b)
    Assignment(
        exchange=exchange,
        user = a,
        recipient = b,
        style = "piece",
        rematch = False,
        moniker = b.moniker
    ).save()


#REMATCH emails
exchange = Exchange.objects.all()[0]
assignments = Assignment.objects.filter(exchange=exchange, rematch=True)
for assignment in assignments:
    print(assignment.user.email, assignment.user.moniker, assignment.recipient.moniker, assignment.upload_link())


#CAN WE POST TO REDDIT?
assignments = Assignment.objects.filter(can_post_to_reddit__isnull=False, posted_to_reddit=False, completed=True)
for assignment in assignments:
    print("****")
    print("Reddit", assignment.can_post_to_reddit)
    print(assignment.user.moniker, "->", assignment.moniker)
    print(assignment.completed)


#Send Signup Confirmation email.
exchange = Exchange.objects.get(name="Feb 2020")
user_pks = []
for user in exchange.users.all():
    user_pks.append(user.pk)
    first_name = user.first_name
    if not first_name:
        first_name = user.moniker
    link = "https://graffexchange.com/confirm_signup/"+user.username+"/"+str(user.pk)
    print(user.email, "|", user.name(), "|", link)


users = User.objects.all().exclude(pk__in=user_pks)
for user in users:
    link = "https://graffexchange.com/confirm_signup/"+user.username+"/"+str(user.pk)
    print(user.email, "|", user.name(), "|", link)
    user.do_double


#SEND EMAILS TO PEOPLE

message = '''{first_name},
Thanks for signing up for the graffiti exchange! I just need to confirm your email address. If you can just click this link then you should be good to go:

{link}

Also, if you add this address to your contacts that would be good, just to make sure that these emails don't end up in spam.
I'm going to try to get the assignments out by Monday, and then you'll have a week to complete the sketch. If you have any questions, of course, don't hesitate to email me.

Thanks again,
Chase
'''

from django.core.mail import EmailMessage
users = User.objects.filter(pk__gte=113).exclude(pk=115)
for user in users:
    link = "https://graffexchange.com/confirm_signup/"+user.username+"/"+str(user.pk)
    m = message.replace('{first_name}', user.name()).replace('{link}', link)
    print('*****')
    print("sending to ", user.email)
    # print(m)
    email = EmailMessage('Graff Exchange Confirmation', m, to=[user.email])
    email.send()

