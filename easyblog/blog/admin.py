from django.contrib import admin

from blog.models import *
from events.models import *

# Register your models here.
admin.site.register(Post)
admin.site.register(Event)