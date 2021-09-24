from django.contrib import admin
from django.urls import path, include
from .views import LoginCustomView, SignUpCustomView, MoviesListView
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('allauth.urls')),

    path('pay/', include('payapp.urls')),

    path("signup/", SignUpCustomView.as_view(), name="account_signup"),
    path('login/', LoginCustomView.as_view(), name='account_login'),
    path('profile/', TemplateView.as_view(template_name='login.html'), name='home'),
    path('logout/', LogoutView.as_view()),

    path('', MoviesListView.as_view(), name='movies_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
        document_root = settings.STATIC_ROOT)

    urlpatterns += static(settings.MEDIA_URL,
        document_root = settings.MEDIA_ROOT)
