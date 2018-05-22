from flask import Flask, request
from handler.messagesHandler import MessagesHandler
from handler.usersHandler import UsersHandler
from handler.groupchatsHandler import GroupChatsHandler
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Default Route
@app.route('/')
def welcome():
    return 'Welcome to the Social Messaging App - Default Route'


# -- Phase II Routes -- #


# Route - List of all messages in the system
@app.route('/MessagingApp_DB/messages/')
def getAllMessages():
    return MessagesHandler().getAllMessages()

# Route - Number of likes to a message
@app.route('/MessagingApp_DB/messages/<int:mid>/likes/count/', methods=['GET', 'POST'])
def getNumberOfLikes(mid):
    if request.method == 'GET':
        return MessagesHandler().getNumberOfLikes(mid)
    else:
        return MessagesHandler().addReactions(mid, request.form)

# Route - List of users who liked a message
@app.route('/MessagingApp_DB/messages/<int:mid>/likes/users/')
def getUsersWhoLikeMessage(mid):
    return MessagesHandler().getUsersWhoLikeMessage(mid)

# Route - Number of dislikes to a message
@app.route('/MessagingApp_DB/messages/<int:mid>/dislikes/count/', methods=['GET', 'POST'])
def getNumberOfDislikes(mid):
    if request.method == 'GET':
        return MessagesHandler().getNumberOfDislikes(mid)
    else:
        return MessagesHandler().addReactions(mid, request.form)

# Route - List of users who dislikes a message
@app.route('/MessagingApp_DB/messages/<int:mid>/dislikes/users/')
def getUsersWhoDislikeMessage(mid):
    return MessagesHandler().getUsersWhoDislikeMessage(mid)

# Route - List of users in the contact list of some user X
@app.route('/MessagingApp_DB/users/<int:uid>/contacts/')
def getContactsOfUser(uid):
    return UsersHandler().getContactsOfUser(uid)

# Route - List of messages posted to a chat group
@app.route('/MessagingApp_DB/groupchats/<int:gid>/messages/', methods=['GET', 'POST'])
def getMessagesByGroupChatId(gid):
    if request.method == 'GET':
        if not request.args:
            return GroupChatsHandler().getMessagesByGroupChatId(gid)
        else:
            return GroupChatsHandler().getMessagesByHashTagInGroup(gid, request.args)

    else:
        return GroupChatsHandler().postMessage(gid, request.form)

# Route - List of users subscribed to a chat group
@app.route('/MessagingApp_DB/groupchats/<int:gid>/users/', methods=['GET', 'POST'])
def getUsersInAGroupChat(gid):
    if request.method == 'GET':
        return GroupChatsHandler().getUsersInAGroupChat(gid)
    else:
        return GroupChatsHandler().addUsersToGroupChat(gid, request.form)

# Route - List of users in the system
@app.route('/MessagingApp_DB/users/')
def getAllUsers():
    return UsersHandler().getAllUsers()

# Route - List of chats group in the system
@app.route('/MessagingApp_DB/groupchats/')
def getAllGroupChats():
    return GroupChatsHandler().getAllGroupChats()

# Route - Owner of a given chat group
@app.route('/MessagingApp_DB/groupchats/<int:gid>/owner')
def getOwnerOfGroupChat(gid):
    return GroupChatsHandler().getOwnerOfGroupChat(gid)

# Route - Information on a given user (by id)
@app.route('/MessagingApp_DB/users/<int:uid>/')
def getUserInformationById(uid):
    return UsersHandler().getUserInformationById(uid)

# Route - Information on a given user (by username)
@app.route('/MessagingApp_DB/users/<string:username>/')
def getUserInformationByUsername(username):
    return UsersHandler().getUserInformationByUsername(username)


# -- Phase III Routes -- #


# Route - Ability to login a user

@app.route('/MessagingApp_DB/users/login/')
def loginUser():
    return UsersHandler().loginUser(request.form)

# Route - Ability to add new user

@app.route('/MessagingApp_DB/users/register/')
def registerUser():
    return UsersHandler().registerUser(request.form)

# Route - Ability to post a new message
#
# @app.route('/MessagingApp_DB/groupchats/<int:gid>/users/<int:uid>')
# def postMessageToGroupChat(gid, uid):
#     return GroupChatsHandler().postMessageToGroupChat(gid, uid, request.form)

# Route - Ability to join a chat group



# Route - Ability to like a message

# @app.route('/MessagingApp_DB/messages/<int:mid>/likes/users/<int:uid>')
# def addLikeToMessage(mid, uid):
#     return MessagesHandler().addLikeToMessage(uid, mid)

# Route - Ability to dislike a message

# @app.route('/MessagingApp_DB/messages/<int:mid>/dislikes/users/<int:uid>')
# def addDislikeToMessage(mid, uid):
#     return MessagesHandler().addDislikeToMessage(uid, mid)

# Route - List of chat groups to which a user belongs
@app.route('/MessagingApp_DB/users/<int:uid>/groupchats/')
def getGroupChatByUserId(uid):
    return UsersHandler().getGroupChatbyUserId(uid)

# Route - List of messages in a given chat group

# Route - List of messages with a given Hashtag on a chat group
#
# @app.route('/MessagingApp_DB/groupchats/<int:gid>/messages/')
# def getMessagesByGroupChatIdWithHashtag(gid):
#     return GroupChatsHandler().getMessagesByGroupChatIdWithHashtag(gid, request.form)

# Route - The ability to post a reply to a message
# @app.route('/MessagingApp_DB/groupchats/<int:gid>/messages/<int:mid>/reply')
# def replyToMessageyGroupChatId(gid, mid):
#     return MessagesHandler().replyToMessage(gid, mid, request.form);

if __name__ == '__main__':
    app.run()


