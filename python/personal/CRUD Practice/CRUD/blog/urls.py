from django.urls import  path
from .views import BlogListview, BlogCreateview, BlogDeleteview, BlogUpdateview, BlogViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('rest',BlogViewset, basename='viewset')

urlpatterns = [
    path('',BlogListview.as_view(),name='List'),
    path('new/',BlogCreateview.as_view(),name='newpost'),
    path('delete/<pk>/',BlogDeleteview.as_view(),name='delete'),
    path('update/<pk>/', BlogUpdateview.as_view(), name= 'update'),
    
] + router.urls
