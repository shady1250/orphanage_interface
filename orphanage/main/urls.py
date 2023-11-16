from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name="home"),
    path("gallery",views.gallery, name="gallery"),
    path("donate",views.donate, name="donate"),
    path("volunteering",views.volunteering, name="volunteering"),
    path("celebrate",views.celebrate, name="celebrate"),
    path('success', views.success, name='success'),

]