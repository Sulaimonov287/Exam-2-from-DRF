from rest_framework import serializers
from .models import *

class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Account
        fields = ('id', 'phone_number', 'password')\

    def create(self, validate_data):
        user = Account.objects.create(phone_number = validate_data['phone_number'],
                                      password=validate_data['password'])
        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user', 'first_name', 'last_name', 'bio', 'username')

class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avatar
        fields = ('id', 'profile', 'image')


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('id', 'user_1', 'user_2', 'created_at')

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'sender', 'chat', 'content', 'created_at')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'owner', 'title', 'avatar')

class GroupMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMember
        fields = ('id', 'user', 'group', 'role', 'joining_date')
        read_only_fields = ('user', 'joining_date')

class GroupMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMessage
        fields = ('id', 'user', 'group', 'content', 'cr_at')

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('id', 'owner', 'title', 'description', 'type', 'cr_at', 'link')

class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Following
        fields = ('id', 'user', 'channel')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'channel', 'content', 'cr_at')
        read_only_fields = ('cr_at',)