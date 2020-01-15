from PIL import Image
from django.http import Http404
import json, random, string
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from exchange.models import User, Sketch, Assignment, Exchange
from django.contrib.gis.geoip2 import GeoIP2
# Create your views here.

#filter
g = GeoIP2()

def rand_string():
    return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(12))

def upload_sketch(request, assignment_pk, tag, password):
    assignment = Assignment.objects.get(pk=assignment_pk)
    if assignment.moniker.lower() != tag.lower():
        raise Http404("Tag doesn't exist")
    if assignment.password != password:
        raise Http404("Incorrect Password")
    if request.method == 'POST':
        time = request.POST.get("time")
        files = request.FILES.getlist('sketches')
        for f in files:
            Sketch(image=f, user=assignment.user, assignment=assignment, time_spent=time).save()
        assignment.completed = True
        assignment.save()
    return render(request, 'upload.html', {
        "sketches": assignment.sketches.all(),
        "tag": assignment.moniker,
    })


def rematch_guide(request, exchange=None):
    if exchange:
        exchange = get_object_or_404(Exchange, name__iexact=exchange.replace("_", " "))
    else:
        exchange = Exchange.objects.all().order_by("-pk")[0]
    assignments = list(Assignment.objects.filter(exchange=exchange))
    if request.method == 'POST':
        pass
    
    for assignment in assignments:
        if assignment.sketches.all().count() > 0:
            assignment.completed = True
            assignment.save()

    #get the exchange circles.
    assignment_groups = []
    next_assignment = None
    loop_count = 0 
    while len(assignments) > 0 and loop_count < 1000:
        print("*******")
        assignment = assignments[0]
        sorted_assignments = []
        while assignment in assignments:
            print(assignment)
            assignments.remove(assignment)
            next_assignment = Assignment.objects.get(user=assignment.recipient)
            sorted_assignments.append(next_assignment)
            assignment = next_assignment
        assignment_groups.append(sorted_assignments)
        loop_count += 1

    return render(request, 'rematch_guide.html', {
        "assignment_groups": assignment_groups,
        "exchange": exchange,
    })

def review(request, exchange=None):
    if exchange:
        exchange = get_object_or_404(Exchange, name__iexact=exchange.replace("_", " "))
    else:
        exchange = Exchange.objects.all().order_by("-pk")[0]
    assignments = Assignment.objects.filter(exchange=exchange)
    if request.method == 'POST':
        pass

    assignments = Assignment.objects.filter(completed=True)
    return render(request, 'review.html', {
        "assignments": assignments,
        "exchange": exchange,
    })

def review_sketches(request, exchange, assignment_pk, tag, password):
    exchange = get_object_or_404(Exchange, name__iexact=exchange.replace("_", " "))    
    assignment = get_object_or_404(Assignment, pk=assignment_pk)
    if exchange != assignment.exchange:
        raise Http404("Sketch doesn't exist")
    if assignment.moniker.lower() != tag.lower():
        raise Http404("Tag doesn't exist")
    if assignment.review_password != password:
        raise Http404("Incorrect Password")
    assignment_sketches = assignment.sketches.all()
    
    return render(request, 'review_sketch.html', {
        "assignment_sketches": assignment_sketches,
        "assignment": assignment,
    })


def signup(request):
    if request.method == 'POST':
        email = request.POST["email"].lower().strip()
        try:
            user = User.objects.get(email=email)
            return render(request, 'already_signed_up.html', {

            })
        except:
            pass
        user = User(email=email, username=rand_string())
        user.moniker = request.POST["moniker"].strip()
        user.write_style = request.POST.get("write_style", None)
        user.recieve_style = request.POST.get("recieve_style", None)
        user.do_double = request.POST.get("do_double", "") == "true"
        user.comments = request.POST.get("comments", None)
        user.ip = request.META.get('REMOTE_ADDR', None)
        if user.ip:
            try:
                locale = g.city(user.ip)
                user.country = locale["country_name"]
                user.city = locale["city"]
            except:
                pass
        user.save()
        exchange = Exchange.objects.all()[0]
        exchange.users.add(user)
        exchange.save()

        return render(request, 'thank_you.html', {
            "email": email
        })
    return render(request, 'signup.html', {
})

def december(request):
    return render(request, 'december.html', {
    })
