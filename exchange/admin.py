from django.contrib import admin

# Register your models here.
from exchange.models import User, Sketch, Assignment, Exchange

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'moniker', 'level', 'write_style', 'recieve_style','do_double', 'comments', 'country', 'city')

admin.site.register(User, UserAdmin)
admin.site.register(Sketch)
admin.site.register(Assignment)
admin.site.register(Exchange)