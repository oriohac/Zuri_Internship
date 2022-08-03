from django.urls import  path
from . views import UserListView, SiteIndexView
from django.views.generic import TemplateView
from . import views

app_name = name = 'cmsapp'
urlpatterns = [
    path('', UserListView.as_view(template_name='index.html'), name='index'),
    path('register/', views.register, name='register'),
    path('login_user/',views.login_user, name='login_user'),
    path('createsite/',TemplateView.as_view(template_name='createsite.html'), name='createsite'),
    path('siteindex/',SiteIndexView.as_view(), name='siteindex')
]