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
@app.route('/MessagingApp_DB/messages/<int:mid>/likes/count/')
def getNumberOfLikes(mid):
    return MessagesHandler().getNumberOfLikes(mid)

# Route - List of users who liked a message
@app.route('/MessagingApp_DB/messages/<int:mid>/likes/users/')
def getUsersWhoLikeMessage(mid):
    return MessagesHandler().getUsersWhoLikeMessage(mid)

# Route - Number of dislikes to a message
@app.route('/MessagingApp_DB/messages/<int:mid>/dislikes/count/')
def getNumberOfDislikes(mid):
    return MessagesHandler().getNumberOfDislikes(mid)

# Route - List of users who dislikes a message
@app.route('/MessagingApp_DB/messages/<int:mid>/dislikes/users/')
def getUsersWhoDislikeMessage(mid):
    return MessagesHandler().getUsersWhoDislikeMessage(mid)

# Route - List of users in the contact list of some user X
@app.route('/MessagingApp_DB/users/<int:uid>/contacts/')
def getContactsOfUser(uid):
    return UsersHandler().getContactsOfUser(uid)

# Route - List of messages posted to a chat group
@app.route('/MessagingApp_DB/groupchats/<int:gid>/messages/')
def getMessagesByGroupChatId(gid):
    return GroupChatsHandler().getMessagesByGroupChatId(gid)

# Route - List of users subscribed to a chat group
@app.route('/MessagingApp_DB/groupchats/<int:gid>/users/')
def getUsersInAGroupChat(gid):
    return GroupChatsHandler().getUsersInAGroupChat(gid)

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

# Route - Ability to add new user

# Route - Ability to post a new message

# Route - Ability to join a chat group

# Route - Ability to like a message

# Route - Ability to dislike a message

# Route - List of chat groups to which a user belongs
@app.route('/MessagingApp_DB/users/<int:uid>/groupchats/')
def getGroupChatByUserId(uid):
    return UsersHandler().getGroupChatbyUserId(uid)

# Route - List of messages in a given chat group

# Route - List of messages with a given Hashtag on a chat group

# Route - The ability to post a reply to a message

if __name__ == '__main__':
    app.run()


