from django.urls import path, include
from . import views
from django.views.generic import TemplateView 

urlpatterns = [
    path('', views.index,  name='index_pay',),
    path('success/', TemplateView.as_view(template_name="success_page.html"), name='success'),
]