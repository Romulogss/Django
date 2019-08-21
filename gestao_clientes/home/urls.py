from django.urls import path
from .views import home, my_logout
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name="home"),
    path('logout/', my_logout, name="logout"),
]