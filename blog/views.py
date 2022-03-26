from django.shortcuts import render, redirect
from .models import Blog
from django.shortcuts import render, get_object_or_404
from taggit.models import Tag
from django.template.defaultfilters import slugify
from hitcount.views import HitCountDetailView
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.http import HttpResponseNotFound

@login_required
def addblog(request):
    form = PostForm(request.POST, request.FILES)

    if form.is_valid():
        blog = form.save()
        blog.slug = slugify(blog.title)
        blog.save()

        return redirect("/blog/")
    if request.user.is_superuser:
        return render(request,"addpost.html",{"form":form})
    else:
        return HttpResponseNotFound

def blog(request):
    info = Blog.objects.all()
    common_tags = Blog.tags.most_common()[:18]
    popular_blog = Blog.objects.order_by('hit_count_generic')[:5]
    # print(popular_blog)
    dic = {}
    for i in info:
        li = []
        for j in i.tags.all():
            li.append(j)
        dic[i] = li
    info = {
        'posts':info,
        'common_tags':common_tags,
        'dic':dic,
        'popular_blog' :popular_blog
        
    }
    return render(request, 'blog/blog.html',info)
#Industry blog home page
def post(request,slug):
    tag = get_object_or_404(Tag, slug=slug)
    popular_blog = Blog.objects.order_by('hit_count_generic')[:5]
    common_tags = Blog.tags.most_common()[:18]
    posts = Blog.objects.filter(tags=tag)
    
    context = {
        'tag':tag,
        'common_tags':common_tags,
        'posts':posts,
        'popular_blog' :popular_blog
    }
    return render(request, 'bloglist.html', context)


class PostDetailView(HitCountDetailView):
    model = Blog
    template_name = 'blog4.html'
    context_object_name = 'posts'
    slug_field = 'slug'
    # set to True to count the hit
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context.update({

        'popular_posts': Blog.objects.order_by('-hit_count_generic__hits')[:3],
        })
        return context


#Ecommerce blog home page starts from here
def blog2(request):
    return render(request, 'blog/blog2.html')


def blog3(request):
    return render(request, 'blog/blog3.html')

def blog4(request):
    return render(request, 'blog/blog4.html')

def blog5(request):
    return render(request, 'blog/blog5.html')

def blog6(request):
    return render(request, 'blog/blog6.html')

