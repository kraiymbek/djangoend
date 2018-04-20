from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect,get_object_or_404,redirect
from .models import Blog
from .forms import BlogForm

# Create your views here.

def blog_create(request):
    form = BlogForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect("blog")


    context = {
        "button_name": "Create blog",
        'form': form
    }
    return render(request, "blog_form.html", context)

def blog_detail(request,id):
    instance = get_object_or_404(Blog, id=id)
    context = {
        "title": instance.title,
        "instance": instance
    }
    return render(request, "blog_detail.html", context)

def blog_list(request):
    queryset = Blog.objects.all()

    context = {
        "object_list": queryset,
    }

    return render(request, "base.html", context)

def blog_update(request,id):
    instance = get_object_or_404(Blog, id=id)
    form = BlogForm(request.POST or None, instance = instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context = {
        "button_name" : "Update blog",
        'title': instance.title,
        'instance' : instance,
        'form': form
    }
    return render(request, "blog_form.html", context)


def blog_delete(request, id=None):
    instance = get_object_or_404(Blog, id=id)
    instance.delete()
    return redirect("blog:list")


