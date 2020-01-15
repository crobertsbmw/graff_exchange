from django.contrib import admin

# Register your models here.
from exchange.models import User, Sketch, Assignment, Exchange

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'moniker', 'level', 'write_style', 'recieve_style','do_double', 'comments', 'country', 'city')

class SketchAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_recipient', 'exchange')
    def get_recipient(self, obj):
        return obj.assignment.recipient.moniker
    get_recipient.short_description = 'Recipient'
    get_recipient.admin_order_field = 'assignment__recipient__moniker'

    

admin.site.register(User, UserAdmin)
admin.site.register(Sketch, SketchAdmin)
admin.site.register(Assignment)
admin.site.register(Exchange)