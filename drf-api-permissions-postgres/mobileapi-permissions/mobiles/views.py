from django.shortcuts import render
from .permissions import IsOwnerOrReadOnly
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers  import ThingSerializer,PostSerializer
# Create your views here.
from .models import Mobile,Post
from rest_framework.permissions import AllowAny,IsAuthenticatedOrReadOnly


class MobileListView(ListCreateAPIView):
    queryset=Mobile.objects.all()
    serializer_class= ThingSerializer


class MobileDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Mobile.objects.all()
    serializer_class= ThingSerializer
    permission_classes=[IsOwnerOrReadOnly]
    
class PostListView(ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class= PostSerializer
    permission_classes=[AllowAny]


class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class= PostSerializer
    permission_classes=[AllowAny]
    
