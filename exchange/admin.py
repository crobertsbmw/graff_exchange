from django.contrib import admin

# Register your models here.
from exchange.models import User, Sketch, Assignment, Exchange, Signup

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'moniker', 'level', 'write_style', 'recieve_style','do_double', 'comments', 'country', 'city')

class AssignAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'rematch', 'completed', 'excitement', 'time_spent')

class SketchAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_recipient', 'exchange')
    def get_recipient(self, obj):
        return obj.assignment.recipient.moniker
    get_recipient.short_description = 'Recipient'
    get_recipient.admin_order_field = 'assignment__recipient__moniker'

class SignupAdmin(admin.ModelAdmin):
    list_display = ('get_email', 'tag', 'get_level', 'style', 'do_double', 'comments')
    def get_level(self, obj):
        return obj.user.level
    def get_email(self, obj):
        return obj.user.email
    get_level.short_description = 'Level'
    get_level.admin_order_field = 'user__level'
    get_email.short_description = 'Email'
    get_email.admin_order_field = 'user__email'


admin.site.register(User, UserAdmin)
admin.site.register(Signup, SignupAdmin)
admin.site.register(Sketch, SketchAdmin)
admin.site.register(Assignment, AssignAdmin)
admin.site.register(Exchange)