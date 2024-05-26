from django.shortcuts import render,get_object_or_404,redirect
from .models import Link
from .forms import LinkForm
from django.urls import reverse


# Create your views here.
def index(request):
    links = Link.objects.all()
    context = {
        'links':links
    }
    return render(request,'bitly_clone/index.html',context)


def add_link(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    else:        
        form = LinkForm()
    context = {
        'form': form
    }
    return render(request,'bitly_clone/create.html',context)


# def reset_link(request,link_slug):
#     link = get_object_or_404(Link,slug=link_slug)
#     link.restetClicks()
#     print(request)
#     return redirect("home")

def root_link(request,link_slug):
    link = get_object_or_404(Link,slug=link_slug)
    link.onClick()
    return redirect(link.url)



def add_link3(request):
    if not  request.method == 'POST':
        form = LinkForm()

    elif form.is_valid():
        form = LinkForm(request.POST)
        return redirect(reverse('home'))

    context = {
        'form': form
    }
    return render(request,'bitly_clone/create.html',context)