from exchange.models import *

#get the exchange we want to make assignments for

exchange = Exchange.objects.all()[0]
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


#rosk -> Zere
#Lang -> Suchr


#Review the submissions.

for assignment in Assignment.objects.all():
    sketches = assignment.sketches.all()
    if len(sketches) == 0:
        print("Not Done", assignment.user.moniker, "->", assignment.recipient.moniker)
        continue
    print(assignment.user.moniker, "->", assignment.recipient.moniker)
    for sketch in sketches:
        print("    ", "https://graffexchange.com"+sketch.image.url)




#REMATCH emails
exchange = Exchange.objects.all()[0]
assignments = Assignment.objects.filter(exchange=exchange, rematch=True)
for assignment in assignments:
    print(assignment.user.email, assignment.user.moniker, assignment.recipient.moniker, assignment.upload_link())

