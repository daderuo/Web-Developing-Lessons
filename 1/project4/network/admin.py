from django.contrib import admin

# Register your models here.

from .models import *

# Register your models here.

admin.site.register(Post)
admin.site.register(User)
admin.site.register(Net)
#admin.site.register(Comments)