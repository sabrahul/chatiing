from django.urls import path
# from rest_framework.routers import DefaultRouter

from .views import MessageListView, MessageCreateView, UserLoginView,UserRegisterView,ConversationView

# router=DefaultRouter()


# router.register('register/',UserRegisterView,basename='register')



urlpatterns = [
    path('api/user/register/',UserRegisterView.as_view(),name='register'),
    path('api/user/login/',UserLoginView.as_view(),name='login'),
    path('get-all-users/',MessageListView.as_view(),name='get_all_users'),
    path('get-conversation/',ConversationView.as_view(),name="get_conversation"),
    path('save-message/',MessageCreateView.as_view(),name='create-message'),

    # path('api/user/',include(router.urls))
]

#/get-conversation
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
#     "current_user": {"id": 1,"name": "rahul"}
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