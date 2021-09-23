from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('allauth.urls')),
    path('', TemplateView.as_view(template_name='login.html'), name='home'),
    path('logout/', LogoutView.as_view()),

    path('pay/', include('payapp.urls'))
]
