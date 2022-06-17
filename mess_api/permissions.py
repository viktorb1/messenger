from rest_framework import permissions
from .models import Conversation


class IsIncluded(permissions.BasePermission):
    def has_permission(self, request, view):
        conv = Conversation.objects.get(pk=request.get_full_path()[-1:])
        return str(request.user) in [user.username for user in conv.user_set.all()]