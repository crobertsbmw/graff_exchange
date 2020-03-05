from exchange.models import *

exchange = Exchange.objects.get(name="Feb 2020")
assignments = exchange.assignments.filter(completed=True)
for ass in assignments:
    print(ass, ass.can_post_to_reddit)

