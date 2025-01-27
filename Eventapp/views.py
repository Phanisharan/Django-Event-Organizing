from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'Home.html')

def planningservices(request):
    return render(request, 'PlanningServices.html')

def viewdetail(request, id):
    return render(request, f'details/Viewdetail{id}.html')

def gallery(request):
    return render(request, 'Gallery.html')

def venue(request):
    return render(request, 'Venue.html')

def contact(request):
    return render(request, 'Contact.html')

def thankyou(request):
    return render(request, 'Thankyou.html')