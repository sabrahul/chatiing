from rest_framework.permissions import BasePermission
from .models import Message,User


class getpermission(BasePermission):
    def has_permission(self, request,view):   
        current_user=request.user
        try:
            user=User.objects.get(pk=current_user.id)
        except User.DoesNotExist:
            user=None
        if user is not None:
            return True
        if request.method == 'GET':
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        # if request.method == "GET":
        #     return True
        Message = Message.objects.get(pk = obj.id)
        if request.user == Message.sender:
            return True
        return False
        
        