from . import views
from django.urls import path


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about-me', views.about_me, name='about-me')
]
