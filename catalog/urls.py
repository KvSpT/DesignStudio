from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('registration/', views.registration.as_view(template_name="registration.html"), name='registration'),
    path('account/', views.account, name='account'),
]

