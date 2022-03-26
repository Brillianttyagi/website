from django.contrib import admin

from .models import Inventory,PostPicture,ServiceRegionOfSeller

class PostPictureInline(admin.TabularInline):
    model = PostPicture
    fields = ['picture',]


class PostAdmin(admin.ModelAdmin):
    inlines = [PostPictureInline,]

# Register your models here.
admin.site.register(Inventory)
admin.site.register(PostPicture)
admin.site.register(ServiceRegionOfSeller)
