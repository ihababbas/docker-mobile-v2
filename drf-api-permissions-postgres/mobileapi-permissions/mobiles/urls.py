
from django.urls import path
from .views import MobileListView,MobileDetailView,PostListView,PostDetailView
urlpatterns = [
   path('', MobileListView.as_view(), name='thing_list'),
   path('<int:pk>', MobileDetailView.as_view(),name='thing_detail'),
   path('posts/', PostListView.as_view(), name='post_list'),
   path('posts/<int:pk>', PostDetailView.as_view(),name='post_detail')
]