from django.shortcuts import render
from neighbors.models import Neighborhood

# Create your views here.


def home(request):
    # projects = Project.objects.all()
    
    # context = {
    #     "projects":projects
    # }
    
    title = "Neighbors"
    
    
    
    return render(request, 'neighbors/index.html', {"title":title})


def create_neighhood(request):
    pass



def neighborhoods(request):
    hoods = Neighborhood.objects.all()
    
    return render(request, 'neighbors/location.html', {"hoods":hoods})



def neighborhood_detail(request, id):
    hoods = Neighborhood.objects.all()
    
    return render(request, 'neighbors/details.html', {"hoods":hoods})