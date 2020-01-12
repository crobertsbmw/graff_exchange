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



piecers = list(users.filter(write_style="piece").all().order_by("-level"))
for a,b in zip(piecers, piecers[1:]+piecers[:1]):
    Assignment(
        exchange=exchange,
        user = a,
        recipient = b,
        style = "piece",
        rematch = False,
        moniker = b.moniker
    ).save()