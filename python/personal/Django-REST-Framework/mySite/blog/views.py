from django.http import JsonResponse
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Payload ={
#     "title":"welcome2",
#     "body":"this is a post2"
# }

# Post.objects.create(title=Payload['title'],body=Payload['body'])