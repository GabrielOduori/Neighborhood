from django.shortcuts import render, redirect, get_object_or_404
from neighbors.models import Neighborhood, Business, Contact, Post
from neighbors.forms import (AddBusinessForm, AddContactForm, 
                             AddNeighborhoodForm, AddPostForm)
from django.urls import reverse
from django.http import Http404

# Create your views here.


def home(request):
    # projects = Project.objects.all()
    
    # context = {
    #     "projects":projects
    # }
    
    title = "Neighbors"
    posts = Post.objects.all()[:3]
    hoods = Neighborhood.objects.all()[:3]
    business = Business.objects.all()[:3]
    
    
    return render(request, 'neighbors/index.html', {"title":title, "posts":posts, "hoods":hoods, "business":business})


def all_neighbors(request):
    all_neighbors = Neighborhood.objects.all()
    
    return render(request, 'neighbors/neighborhoods.html', {"all_neighbors":all_neighbors})

def create_neighhood(request):
    current_user = request.user.profile
    
    form = AddNeighborhoodForm()
    if request.method =='POST':
        form = AddNeighborhoodForm(request.POST)
        if form.is_valid():
            hood = form.save(commit = False)
            hood.profile = current_user
            hood.save()
            return redirect(reverse('accounts:view_profile'))
        else:
            form = AddNeighborhoodForm()
            
    return render(request, 'neighbors/add_hood.html',{"form":form})






def neighborhood_details(request, id):
    hood_detals = get_object_or_404(Neighborhood, id = id)
    
    return render(request, 'neighbors/neighborhoods_details.html', {"hood_detals":hood_detals})


def posts(request):
    posts = Post.objects.all()
    
    
    
    return render(request, 'neighbors/posts.html', {"posts":posts})