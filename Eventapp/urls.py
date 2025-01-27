from django.urls import path
from .views import *

app_name = 'Eventapp'

urlpatterns = [
    path('', home, name='home'),
    path('gallery/', gallery, name='gallery'),
    path('venue/', venue, name='venue'),
    path('planningservice/', planningservices, name='planning-services'),
    path('viewdetail/<int:id>/', viewdetail, name='viewdetail'),
    path('contact/', contact, name='contact'),
    path('thankyou/', thankyou, name='thankyou')
]