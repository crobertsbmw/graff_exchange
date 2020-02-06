from exchange.models import *

#get the exchange we want to make assignments for
exchange = Exchange.objects.get(name="Feb 2020")
#sort by style
users = exchange.users.all() # get our users

handstylers = list(users.filter(write_style="handstyle").all().order_by("-level"))
for a,b in zip(handstylers, handstylers[1:]+handstylers[:1]):
    Assignment(
        exchange=exchange,
        user = a,
        recipient = b,
        style = "handstyle",
        rematch = False,
        moniker = b.moniker
    ).save()
    

throwers = list(users.filter(write_style="throwie").all().order_by("-level"))[2:]
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
piecers = list(users.filter(write_style="piece", level__lte=7, level__gte=4).all())
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
for user in Exchange.users.all():
    print(user.email, user.first_name)




