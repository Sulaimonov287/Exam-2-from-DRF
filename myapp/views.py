from rest_framework import generics
from .models import *
from .serializer import *


class AccountListCreateView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class ProfileListCreateView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class AvatarListCreateView(generics.ListCreateAPIView):
    queryset = Avatar.objects.all()
    serializer_class = AvatarSerializer


class AvatarDetailView(generics.RetrieveDestroyAPIView):
    queryset = Avatar.objects.all()
    serializer_class = AvatarSerializer


class ChatListCreateView(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class ChatDetailView(generics.RetrieveDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class MessageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageDetailView(generics.RetrieveDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class GroupListCreateView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupMemberListCreateView(generics.ListCreateAPIView):
    queryset = GroupMember.objects.all()
    serializer_class = GroupMemberSerializer


class GroupMemberDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GroupMember.objects.all()
    serializer_class = GroupMemberSerializer


class GroupMessageListCreateView(generics.ListCreateAPIView):
    queryset = GroupMessage.objects.all()
    serializer_class = GroupMessageSerializer


class GroupMessageDetailView(generics.RetrieveDestroyAPIView):
    queryset = GroupMessage.objects.all()
    serializer_class = GroupMessageSerializer


class ChannelListCreateView(generics.ListCreateAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


class ChannelDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


class FollowingListCreateView(generics.ListCreateAPIView):
    queryset = Following.objects.all()
    serializer_class = FollowingSerializer


class FollowingDetailView(generics.RetrieveDestroyAPIView):
    queryset = Following.objects.all()
    serializer_class = FollowingSerializer


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer