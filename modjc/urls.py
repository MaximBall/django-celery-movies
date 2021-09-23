from django.contrib import admin
from django.urls import path, include
from .views import LoginCustomView, SignUpCustomView
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('allauth.urls')),

    path("signup/", SignUpCustomView.as_view(), name="account_signup"),
    path('login/', LoginCustomView.as_view(), name='account_login'),
    path('profile/', TemplateView.as_view(template_name='login.html'), name='home'),
    path('logout/', LogoutView.as_view()),

    path('pay/', include('payapp.urls'))
]
