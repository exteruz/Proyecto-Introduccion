
from django.contrib import admin
from event.models import event,category
from points.models import rango,reward,insignia
from user.models import user
# Register your models here.
admin.site.register(event)
admin.site.register(category)
admin.site.register(rango)
admin.site.register(reward)
admin.site.register(insignia)
admin.site.register(user)

