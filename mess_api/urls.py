from django.urls import path
from . import views
from rest_framework.views import APIView


urlpatterns = [
    path('createuser/', views.CreateUserView.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view(), name="user-detail"),
    path('users/<int:pk>/all_messages', views.get_all_messages_by_user),
    path('createconversation/', views.CreateConversationView.as_view()),
    path('conversations/', views.ConversationList.as_view()),
    path('conversations/<int:pk>', views.ConversationsView.as_view()),

]