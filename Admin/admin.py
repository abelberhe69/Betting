from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(MainAdmin)
admin.site.register(League)
admin.site.register(Club)
admin.site.register(TopMatch)
admin.site.register(NextToGo)
admin.site.register(Trending)