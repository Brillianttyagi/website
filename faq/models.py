from django.template.defaultfilters import default
from django.db import models
from ckeditor.fields import RichTextField

#Faq models
class Faq(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=500)
    answer = RichTextField(blank=True,null=True)
    created = models.DateField(
        auto_now_add=True
    )
    author = models.CharField(max_length=60,default="theseventhsquare")
    tags = models.CharField(max_length=60)

    def __str__(self):
        return self.question