import datetime, random, string
from django.db import models
from django.contrib.auth.models import AbstractUser


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

class Sketch(models.Model):
    image = models.FileField(upload_to='%Y/%m/%d/')
    assignment = models.ForeignKey('Assignment', related_name="sketches", on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey('User', related_name="portfolio", on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=datetime.datetime.now)
    time_spent = models.CharField(max_length=255, blank=True, null=True)
    exchange = models.ForeignKey('Exchange', related_name="sketches", related_query_name="sketches", on_delete=models.SET_NULL, null=True, blank=True)

class Assignment(models.Model):
    def __str__(self):
        return self.user.moniker+" -> "+self.moniker+" ("+self.style+")"
    exchange = models.ForeignKey('Exchange', related_name="assignments", related_query_name="assignment", on_delete=models.CASCADE)
    user = models.ForeignKey('User', related_name="assignments", related_query_name="assignment", on_delete=models.CASCADE)
    recipient = models.ForeignKey('User', related_name="favors", on_delete=models.CASCADE)
    style = models.CharField(max_length=255, choices=STYLES, null=True, blank=True)
    rematch = models.BooleanField(default=False)
    moniker = models.CharField(max_length=255)
    password = models.CharField(max_length=10, default=rand_string)
    review_password = models.CharField(max_length=10, default=rand_string)
    completed = models.BooleanField(default=False)
    
    def upload_link(self):
        return "https://graffexchange.com/upload/"+str(self.pk)+"/"+self.moniker.lower()+"/"+self.password+"/"
    def review_link(self):
        return "https://graffexchange.com/review/"+self.exchange.name.replace(" ", "_")+str(self.pk)+"/"+self.moniker.lower()+"/"+self.review_password+"/"

def month_year_string():
    return datetime.datetime.now().strftime("%b %Y")

class Exchange(models.Model):
    def __str__(self):
        return self.name
    users = models.ManyToManyField(User, blank=True)
    name = models.CharField(max_length=255, default=month_year_string)
    start_date = models.DateTimeField(null=True, blank=True)

