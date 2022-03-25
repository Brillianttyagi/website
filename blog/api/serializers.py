from rest_framework import serializers
from blog.models import Blog
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)
from taggit.models import Tag

class BlogSerializer(TaggitSerializer,serializers.ModelSerializer):
    tags = TagListSerializerField()
    class Meta:
        model = Blog
        fields = ['id','title','body','image','author','slug','tags','created']

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ['slug']


class MainSerializer(serializers.Serializer):
    posts = BlogSerializer(many=True)
    tags = TagSerializer(many=True)
