from pickletools import read_floatnl
from django.shortcuts import render
from rest_framework import permissions, generics
from django.contrib.auth import get_user_model 
from .serializers import UserSerializer, ConversationViewSerializer, MessageSerializer, AllMessagesSerializer, UserViewSerializer, ConversationCreateSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .models import Message, Conversation
from .permissions import IsIncluded


class CreateUserView(generics.CreateAPIView):
    model = get_user_model()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserList(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserViewSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class ConversationsView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    permission_classes = [IsIncluded]
    serializer_class = MessageSerializer

    def list(self, request, pk):
        conv = Conversation.objects.get(pk=pk)
        messages = Message.objects.filter(conversation_id=conv) 
        serializer_context = {'request': request,}  
        return Response(MessageSerializer(messages, read_only=True, many=True, context=serializer_context).data)

    def create(self, request, pk):
        conv = Conversation.objects.get(pk=pk)
        usr = get_user_model().objects.get(username=request.user)
        msg = Message.objects.create(text=request.data['text'], conversation_id=conv, user_id=usr)
        ser = MessageSerializer(msg)
        return Response(ser.data)



@api_view()
def get_all_messages_by_user(request, pk):
    cur_user = get_user_model().objects.get(pk=pk)
    messages = Message.objects.filter(user_id=cur_user)
    return Response(AllMessagesSerializer(messages, many=True).data)


class CreateConversationView(generics.CreateAPIView):
    model = Conversation
    serializer_class = ConversationCreateSerializer


class ConversationList(generics.ListAPIView):
    queryset = Conversation.objects.all()
    serializer_class = ConversationViewSerializer