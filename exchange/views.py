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
    print(assignment_pk)
    print(tag)
    assignment = Assignment.objects.get(pk=assignment_pk)
    if assignment.moniker.lower() != tag.lower():
        raise Http404("Tag doesn't exist")
    if assignment.password != password:
        raise Http404("Incorrect Password")
    if request.method == 'POST':
        files = request.FILES.getlist('sketches')
        for f in files:
            Sketch(image=f, user=assignment.user, assignment=assignment).save()
    return render(request, 'upload.html', {
        "sketches": assignment.sketches.all(),
        "tag": assignment.moniker,
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
