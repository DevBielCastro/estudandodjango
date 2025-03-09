from django.urls import path
from .views import UserListCreateView, UserDetailUpdateDeleteView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='list_create_users'),
    path('users/<str:nick>/', UserDetailUpdateDeleteView.as_view(), name='user_detail_update_delete'),
]
