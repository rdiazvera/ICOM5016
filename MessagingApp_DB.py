from flask import Flask, request
from handler.messageHandler import messageHandler
from handler.userHandler import UserHandler
from handler.groupchatHandler import GroupChatHandler
from handler.memberHandler import MemberHandler
from handler.hashtagHandler import HashtagHandler
from handler.reactionHandler import ReactionHandler
from handler.replyHandler import ReplyHandler

app = Flask(__name__)

# Default Route
@app.route('/')
def welcome():
    return 'Welcome to the Social Messaging App - Default Route'

# Home Route
@app.route('/MessagingApp_DB/home/')
def home():
    return 'Home Route'

# Log in Route
@app.route('/MessagingApp_DB/login/')
def log_in():
    return 'Log in Route'

# Sign up Route
@app.route('/MessagingApp_DB/signup/')
def signup():
    return 'Sign Up Route'

# Route to all elements from table 'Messages'
@app.route('/MessagingApp_DB/messages/')
def getAllMessages():
    if request.args:
        return messageHandler().getMessageBy(request.args)
    else:
        return messageHandler().getAllMessages()

# Route to get an element from table 'Messages' searching with an id
@app.route('/MessagingApp_DB/messages/<int:mid>/')
def getMessageById(mid):
    return messageHandler().getMessageByID(mid)

# Route to get an element from table 'Messages' searching with an owner id
@app.route('/MessagingApp_DB/messages/owner/<int:ownerid>/')
def getMessagesByOwnerId(ownerid):
    return messageHandler().getMessagesByOwnerID(ownerid)

# Route to get an element from table 'Messages' searching with a group chat id
@app.route('/MessagingApp_DB/messages/groupchat/<int:gid>/')
def getMessagesByGroupChatId(gid):
    return messageHandler().getMessagesByGroupChatID(gid)

# Route to get an element from table 'Messages' searching with the date created
@app.route('/MessagingApp_DB/messages/date/<string:date>/')
def getMessagesByDate(date):
    return messageHandler().getMessageByDate(date)

# Route to all elements from table 'Users'
@app.route('/MessagingApp_DB/users/')
def getAllUsers():
    return UserHandler().getAllUsers()

# Route to get an element from table 'Users' searching with an id
@app.route('/MessagingApp_DB/users/<int:uid>/')
def getUserById(uid):
    return UserHandler().getUserById(uid)

# Route to get an element from table 'users' searching with an email
@app.route('/MessagingApp_DB/users/email/<string:email>')
def getUserByEmail(email):
    return UserHandler().getUserByEmail(email)

# Route to get an element from table 'users' searching with an phone
@app.route('/MessagingApp_DB/users/phone/<string:phone>')
def getUserByphone(phone):
    return UserHandler().getUserByPhone(phone)

# Route to all elements from table 'GroupChat'
@app.route('/MessagingApp_DB/groupchats/')
def getAllGroupChats():
    return GroupChatHandler().getAllGroupChats()

# Route to get an element from table 'GroupChat' searching with an id
@app.route('/MessagingApp_DB/groupchats/<int:gid>/')
def getGroupChatsById(gid):
    return GroupChatHandler().getGroupChatById(gid)

# Route to get an element from table 'Groupchat' search with an owner id
@app.route('/MessagingApp_DB/groupchats/owner/<int:ownerId>')
def getGroupChatByOwnerId(ownerId):
    return GroupChatHandler().getGroupChatByOwnerId(ownerId)

# Route to all elements from table 'Member'
@app.route('/MessagingApp_DB/members/')
def getAllMembers():
    return MemberHandler().getAllMembers()

# Route to get an element from table 'Member' searching with an id
@app.route('/MessagingApp_DB/members/<int:mid>/')
def getMemberById(mid):
    return MemberHandler().getMemberById(mid)

# Route to all elements from table 'Reaction'
@app.route('/MessagingApp_DB/reactions/')
def getAllReactions():
    return ReactionHandler().getAllReactions()

# Route to get an element from table 'Reaction' searching with an id
@app.route('/MessagingApp_DB/reactions/<int:rid>/')
def getReactionById(rid):
    return ReactionHandler().getReactionById(rid)

# Route to all elements from table 'Reply'
@app.route('/MessagingApp_DB/replies/')
def getAllReplies():
    return ReplyHandler().getAllReplies()

# Route to get an element from table 'Reply' searching with an id
@app.route('/MessagingApp_DB/replies/<int:rid>/')
def getReplyById(rid):
    return ReplyHandler().getReplyById(rid)

# Route to all elements from table 'Hashtag'
@app.route('/MessagingApp_DB/hashtags/')
def getAllHashtags():
    return HashtagHandler().getAllHashtags()

# Route to get an element from table 'Hashtag' searching with an id
@app.route('/MessagingApp_DB/hashtags/<int:hid>/')
def getHashtagById(hid):
    return HashtagHandler().getHashtagById(hid)

# Route to statistics page
@app.route('/MessagingApp_DB/statistics/')
def statistics():
    return 'Statistics Route'

# Route to trending topics page
@app.route('/MessagingApp_DB/statistics/trending/')
def trendingStatistics():
    return 'Statistics Route: Trending topics via #hashtags'

# Route to message statistics page
@app.route('/MessagingApp_DB/statistics/messages/')
def messagesStatistics():
    return 'Statistics Route: Number of message per day'

# Route to replies statistics page
@app.route('/MessagingApp_DB/statistics/replies/')
def repliesStatistics():
    return 'Statistics Route: Number of replies per day'

# Route to likes statistics page
@app.route('/MessagingApp_DB/statistics/likes/')
def likeStatistics():
    return 'Statistics Route: Number of likes'

# Route to dislikes statistics page
@app.route('/MessagingApp_DB/statistics/dislikes/')
def dislikeStatistics():
    return 'Statistics Route: Number of dislikes'

# Route to active users statistics page
@app.route('/MessagingApp_DB/statistics/activeusers/')
def activeUserstatistics():
    return 'Statistics Route: Active users'

if __name__ == '__main__':
    app.run()


