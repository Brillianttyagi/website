from django.template.defaultfilters import default
from django.db import models
from taggit.managers import TaggableManager
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from ckeditor.fields import RichTextField

#Blog models
class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    body = RichTextField(blank=True,null=True)
    created = models.DateField(
        auto_now_add=True
    )
    image = models.ImageField(upload_to = 'pics')
    author = models.CharField(max_length=60,default="theseventhsquare")
    slug = models.SlugField(unique=True, max_length=100)
    tags = TaggableManager()
    
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
     related_query_name='hit_count_generic_relation')

    def __str__(self):
        return self.title