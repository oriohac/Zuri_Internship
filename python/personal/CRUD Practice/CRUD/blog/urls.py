from django.urls import  path
from .views import BlogListview, BlogCreateview, BlogDeleteview


urlpatterns = [
    path('',BlogListview.as_view(),name='List'),
    path('new/',BlogCreateview.as_view(),name='newpost'),
    path('delete/<pk>/',BlogDeleteview.as_view(),name='delete')
]
