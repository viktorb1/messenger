from rest_framework import serializers
from django.contrib.auth import get_user_model
UserModel = get_user_model()
from .models import Conversation, Message, User

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user

    class Meta:
        model = UserModel
        fields = ( "id", "username", "password")
        ordering = ('id',)

class UserViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ( "id", "username")
        ordering = ('id',)

class UsernameOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ("username",)

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    user_url = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True, source='user_id')

    class Meta:
        model = Message
        fields = ('text', 'time_sent', 'user_url')
        read_only_fields = ('user_url',)

    

class ConversationCreateSerializer(serializers.HyperlinkedModelSerializer):
    # user_set = UserViewSerializer(source='user_set.id', many=True)
    class Meta:
        model = Conversation
        fields = ['conversation_name', 'user_set', 'id']



class ConversationViewSerializer(serializers.HyperlinkedModelSerializer):
    user_set = serializers.HyperlinkedRelatedField(many=True, view_name='user-detail', read_only=True)

    class Meta:
        model = Conversation
        fields = ['conversation_name', 'user_set']


class AllMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('text', 'time_sent', 'user_id', 'conversation_id')
