from django.urls import path
from .views import *


urlpatterns = [
    path('accounts/', AccountListCreateView.as_view()),
    path('accounts/<int:pk>/', AccountDetailView.as_view()),
    path('profiles/', ProfileListCreateView.as_view()),
    path('profiles/<int:pk>/', ProfileDetailView.as_view()),
    path('avatars/', AvatarListCreateView.as_view()),
    path('avatars/<int:pk>/', AvatarDetailView.as_view()),
    path('chats/', ChatListCreateView.as_view()),
    path('chats/<int:pk>/', ChatDetailView.as_view()),
    path('messages/', MessageListCreateView.as_view()),
    path('messages/<int:pk>/', MessageDetailView.as_view()),
    path('groups/', GroupListCreateView.as_view()),
    path('groups/<int:pk>/', GroupDetailView.as_view()),
    path('group-members/', GroupMemberListCreateView.as_view()),
    path('group-members/<int:pk>/', GroupMemberDetailView.as_view()),
    path('group-messages/', GroupMessageListCreateView.as_view()),
    path('group-messages/<int:pk>/', GroupMessageDetailView.as_view()),
    path('channels/', ChannelListCreateView.as_view()),
    path('channels/<int:pk>/', ChannelDetailView.as_view()),
    path('following/', FollowingListCreateView.as_view()),
    path('following/<int:pk>/', FollowingDetailView.as_view()),
    path('posts/', PostListCreateView.as_view()),
    path('posts/<int:pk>/', PostDetailView.as_view()),
]
