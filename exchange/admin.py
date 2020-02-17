from django.contrib import admin

# Register your models here.
from exchange.models import User, Sketch, Assignment, Exchange, Signup

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'moniker', 'level', 'signed_up', 'comments', 'country', 'city')
    def signed_up(self, obj):
        return obj.signed_up()
    signed_up.boolean = True

class AssignAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'rematch', 'completed', 'excitement', 'time_spent', 'upload_link')

class SketchAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_recipient', 'exchange')
    def get_recipient(self, obj):
        if obj.assignment.recipient_signup:
            return obj.assignment.recipient_signup.tag
        else:
            return obj.assignment.recipient.username
    get_recipient.short_description = 'Recipient'
    get_recipient.admin_order_field = 'assignment__recipient_signup__tag'

class SignupAdmin(admin.ModelAdmin):
    list_display = ('get_email', 'tag', 'exchange', 'get_level', 'style', 'do_double', 'comments')
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