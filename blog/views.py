from django.shortcuts import render, get_object_or_404
from blog.models import Post, Tag
from analytics.models import View


def blog(request):
    return render(request, 'blog.html', {
        'posts': Post.objects.order_by('-created')
    })


def post(request, pk):
    post_obj = get_object_or_404(Post, pk=pk)

    return render(request, 'post.html', {
        'post': post_obj
    })

def post_list(request, pk):
    posts = Post.objects.filter(tags__pk=pk)
    tag = Tag.objects.get(pk=pk)
    return render(request, 'blog.html', {
        'posts': posts,
        'tag' : tag
    })

def page_view(request, pk):
    views = View.objects.filter(pk=pk)
    return render(request, 'page_view.html', {
        'views' : views
    })

def error(request):
    my_variable = '!'
    my_list = ['testing', 'a', 'list', 'out']
    my_list = ["{}{}".format(list_item, my_variable) for list_item in my_list]
    raise NotImplementedError("Woops! This doesn't exist.")