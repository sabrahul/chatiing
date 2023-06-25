from .models import User,Message


def get_user_by_id(user_id):
    return User.objects.get(id=user_id)

def get_conversation(users: list):
    Conversation = Message.objects.filter(sender__in=users,receiver__in=users).order_by('created_at')
    chat_object = [{
            "message": chat.message,
            "sender": chat.sender.id,
            "receiver": chat.receiver.id,
            "date": chat.created_at
        } for chat in Conversation]
    return chat_object