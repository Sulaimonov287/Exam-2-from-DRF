from django.db import models


class Account(models.Model):
    phone_number = models.CharField( max_length=50, unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.phone_number


class Profile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    first_name = models.CharField( max_length=50)
    last_name = models.CharField( max_length=50)
    bio = models.TextField()
    username = models.CharField( max_length=50, unique=True)

    def __str__(self):
        return self.username

class Avatar(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatars/', blank=True, null=True)

class Chat(models.Model):
    user_1 = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='chats_initiated')
    user_2 = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='chats_received')
    created_at = models.DateTimeField( auto_now_add=True)

    class Meta:
        unique_together = ('user_1', 'user_2')

class Message(models.Model):
    sender = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='messages')
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    created_at = models.DateTimeField( auto_now_add=True)

class Group(models.Model):
    owner = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='owner_groups')
    title = models.CharField( max_length=100)
    avatar = models.CharField( max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title

class GroupMember(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE, related_name='group_memberships')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='members')
    role = models.CharField( max_length=50, default='member')
    joining_date = models.DateTimeField( auto_now_add=True)

    class Meta:
        unique_together = ('user', 'group')

class GroupMessage(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='group_messages')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    cr_at = models.DateTimeField(auto_now_add=True)

class Channel(models.Model):
    owner = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='channels')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=20, default='public')
    cr_at = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=100, unique=True, blank=True, null=True)

    def __str__(self):
        return self.title

class Following(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='following')
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name='followers')

    class Meta:
        unique_together = ('user', 'channel')

class Post(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    cr_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title