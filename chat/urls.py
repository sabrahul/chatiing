from django.urls import path
from .views import MessageListView, MessageCreateView, UserLoginView,UserRegisterView,ConversationView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)




urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/register',UserRegisterView.as_view(),name='register'),
    path('api/user/login',UserLoginView.as_view(),name='login'),
    path('get-all-users',MessageListView.as_view(),name='get_all_users'),
    path('get-conversation',ConversationView.as_view(),name="get_conversation"),
    path('save-message',MessageCreateView.as_view(),name='create-message'),

    # path('api/user/',include(router.urls))
]

#http://127.0.0.1:8000/get-conversation/
#request parameters: -  sender=1, reciever=2  
# {
#     "message": [
#         {'id': "1", "name": "rahul", "message": "hey", "date": ""},
#         {'id': "2", "name": "vishal", "message": "hi", "date": ""},

#     ]
# }

#/get-all-users
# {
#     "users": [
#         {"id": 1,"name": "rahul"},
#         {"id": 2, "name": "vishal"}
#     ],
# }

#/save-message
# payload:- 
# {
#     "message": "hey",
#     "sender": 1,
#     "receiver": 2,
# }
# response:-  
# {
#     "status": "message saved successfully",
#     "message": "hey",
#     "sender": 1,
#     "receiver": 2
# }