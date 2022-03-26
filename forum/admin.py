from django.contrib import admin
from .models import Discussion,Comment,TalkToUs,RequestACallback

# Register your models here.
admin.site.register(Discussion)
admin.site.register(Comment)
admin.site.register(TalkToUs)
admin.site.register(RequestACallback)