from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.authentication import BasicAuthentication
from .permissions import getpermission
from .models import User,Message
from .serializers import UserLoginSerializer, UserRegisterSerializer,MessageSerializer, UserSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .utils import get_user_by_id, get_conversation
import json

# Create your views here.

from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserRegisterView(APIView):
    def post(self,request,format=None):
        serializer=UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg':'User saved Successfully'},status=status.HTTP_201_CREATED)

class UserLoginView(APIView):
    @method_decorator(csrf_exempt)
    def post(self,request,format=None):
        serializer=UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email=serializer.data.get('email')
        password=serializer.data.get('password')
        user=authenticate(email=email,password=password)
        if user is not None:
            token=get_tokens_for_user(user)
            data = {"status": True,"token": token, "name":user.name, "email": user.email, "id": user.id}
            return Response(data,status=status.HTTP_200_OK)
        else:
            return Response({"error":"User does not exist"},status=status.HTTP_404_NOT_FOUND)


class MessageListView(ListAPIView):
    authentication_classes=[BasicAuthentication]
    permission_classes=(getpermission,)
    serializer_class=UserSerializer
    
    def get_queryset(self):
        return User.objects.all()


class MessageCreateView(APIView):
    @method_decorator(csrf_exempt)
    def post(self,request,format=None):
        serializer=MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'msg':'message saved Successfully',
            "new_message": request.data.get('message'),
            "sender": request.data.get('sender'),
            "receiver": request.data.get('receiver')
        },status=status.HTTP_201_CREATED)
    
class ConversationView(APIView):
    authentication_classes=[BasicAuthentication]
    permission_classes=(getpermission,)
    serializer_class=MessageSerializer
    
    def get(self,request):
        sender_id=int(request.GET.get('sender'))
        receiver_id=int(request.GET.get('receiver'))
        users = [sender_id,receiver_id]
        chat_object = get_conversation(users)
        return Response({
            "message": chat_object,
            "receiver_name": get_user_by_id(receiver_id).get('name')        
        })
    

    

