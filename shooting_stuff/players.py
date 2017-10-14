import json
from channels import Group
from .models import User

def connect_player(message,user_id):

    #adds new players to the group
    try:
        user = User.object.get(ID = user_id)
    except User.DoesNotExreist:
        message.reply_channel.send({
            #sends error message if object does not eist
            "text":json.dumps({"error":"bad_slug"}),
            "close":True,
        })
        return
    message.reply_channel.send({"accept":True})
    #each client has reply channel. This line adds
    #all the channels to the same reply group
    Group(user.group_name).add(message.reply_channel)

def disconnect_player(message,user_id):
    #disconects players when they leave the socket
    try:
        user = User.object.get(ID = user_id)
    except User.DoesNotExist:
        #Disconnect Message
        return
    Group(user.group_name).discard(message.reply_channel)


