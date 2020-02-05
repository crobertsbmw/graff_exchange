import datetime, random, string
from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django.conf import settings
import os
from stdimage import JPEGField

def rand_string():
    return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(8))

STYLES = (("handstyle", "handstyle"), 
            ("wildstyle", "wildstyle"), 
            ("throwie", "throwie"), 
            ("keyboard", "keyboard"),
            ("piece", "piece"))

class User(AbstractUser):
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-date_joined',]

    def __str__(self):
        if self.moniker:
            return self.moniker
        return self.email

    points = models.IntegerField(default=0)
    level = models.IntegerField(default=0)
    moniker = models.CharField(max_length=255)
    write_style = models.CharField(max_length=255, choices=STYLES, null=True, blank=True)
    recieve_style = models.CharField(max_length=255, choices=STYLES, null=True, blank=True)
    do_double = models.BooleanField(default=False)
    comments = models.CharField(max_length=1200, null=True, blank=True)
    ip = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)


class Signup(models.Model):
    user = models.ForeignKey('User', related_name="signups", on_delete=models.CASCADE)
    tag = models.CharField(max_length=255, null=True, blank=True)
    style = models.CharField(max_length=255, choices=STYLES, null=True, blank=True)
    comments = models.CharField(max_length=1200, null=True, blank=True)
    do_double = models.BooleanField(default=False)
    exchange = models.ForeignKey('Exchange', related_name="signups", related_query_name="signups", on_delete=models.CASCADE)

def upload_to(instance, filename):
    return '%s/%s' % (instance.user.username, filename)


class Sketch(models.Model):
    # image = models.ImageField(upload_to=upload_to)
    image = JPEGField(
        upload_to=upload_to,
        variations={'large': (750, 450), 'thumbnail': (125, 75)},
    )
    assignment = models.ForeignKey('Assignment', related_name="sketches", on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey('User', related_name="portfolio", on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=datetime.datetime.now)
    time_spent = models.CharField(max_length=255, blank=True, null=True)
    exchange = models.ForeignKey('Exchange', related_name="sketches", related_query_name="sketches", on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return str(self.user)+"->"+str(self.assignment.recipient)

    def rotate(self):
        im = Image.open(self.image.file)
        angle = 90
        im = im.rotate(angle, expand=True)
        im.save(self.image.file.name)

    # https://stackoverflow.com/questions/23945494/use-html5-to-resize-an-image-before-upload
    # https://stackoverflow.com/questions/623698/resize-image-on-save
    def resize(self):
        basewidth = 800
        im = Image.open(self.image.file)
        if im.size[0] < basewidth: basewidth = 800
        wpercent = (basewidth / float(im.size[0]))
        hsize = int((float(im.size[1]) * float(wpercent)))
        im = im.resize((basewidth, hsize), Image.ANTIALIAS)
        im = im.convert('RGB')
        name = os.path.splitext(self.image.file.name)[0]+"_resize.jpg"
        im.save(name)
        name = name.replace(settings.MEDIA_ROOT, "")
        if name[0] == "/": name = name[1:]
        self.image = name
        self.save()

class Assignment(models.Model):
    def __str__(self):
        if self.style:
            return self.user.moniker+" -> "+self.moniker+" ("+self.style+")"
        else:
            return self.user.moniker+" -> "+self.moniker
    exchange = models.ForeignKey('Exchange', related_name="assignments", related_query_name="assignment", on_delete=models.CASCADE)
    user = models.ForeignKey('User', related_name="assignments", related_query_name="assignment", on_delete=models.CASCADE)
    user_signup = models.ForeignKey('Signup', related_name="assignments", related_query_name="assignment", on_delete=models.CASCADE, null=True, blank=True)
    recipient = models.ForeignKey('User', related_name="favors", on_delete=models.CASCADE)
    recipient_signup = models.ForeignKey('Signup', related_name="favors", related_query_name="favor", on_delete=models.CASCADE, null=True, blank=True)
    style = models.CharField(max_length=255, choices=STYLES, null=True, blank=True)
    time_spent = models.CharField(max_length=255, blank=True, null=True)
    rematch = models.BooleanField(default=False)
    password = models.CharField(max_length=10, default=rand_string)
    review_password = models.CharField(max_length=10, default=rand_string)
    completed = models.BooleanField(default=False)
    can_post_to_reddit = models.CharField(max_length=255, null=True, blank=True)
    excitement = models.IntegerField(null=True, blank=True)
    posted_to_reddit = models.BooleanField(default=False)

    def upload_link(self):
        return "https://graffexchange.com/upload/"+str(self.pk)+"/"+self.moniker.lower()+"/"+self.password+"/"
    def review_link(self):
        return "https://graffexchange.com/review/"+self.exchange.name.replace(" ", "_")+"/"+str(self.pk)+"/"+self.moniker.lower()+"/"+self.review_password+"/"

def month_year_string():
    return datetime.datetime.now().strftime("%b %Y")

class Exchange(models.Model):
    def __str__(self):
        return self.name
    users = models.ManyToManyField(User, blank=True)
    name = models.CharField(max_length=255, default=month_year_string)
    start_date = models.DateTimeField(null=True, blank=True)

