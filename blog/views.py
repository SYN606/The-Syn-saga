from django.shortcuts import render, get_object_or_404
from .models import Blog
from taggit.models import Tag
from django.core.paginator import Paginator


def blog(request):
    blog = Blog.objects.order_by("-date")
    tag = Tag.objects.all()
    if request.method == "POST":
        query = request.POST['search_data']
        blog = Blog.objects.filter(blog_title__icontains = query)

    paginator = Paginator(blog, 15)
    page_num = request.GET.get('page')
    final_data = paginator.get_page(page_num)
    

    data = {
        "blog" : final_data,
        "title" : "Blogs Homepage",
        "tag" : tag
    }
    return render(request, "blog.html", data)


def blog_data(request, slug):
    blog = Blog.objects.get(slug = slug)
    tag = Blog.objects.prefetch_related('tags').all()
    data = {
        "blog" : blog,
        'tag' : tag,
    }
    return render(request, "blog_render.html", data)



def tagged(request, tag_slug):
    tag = get_object_or_404(Tag, slug = tag_slug)
    blog = Blog.objects.filter(tags__in = [tag])
    data = {
        'tag' : tag,
        'blog' : blog
    }
    return render(request, 'blog.html', data)