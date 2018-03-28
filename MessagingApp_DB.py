from flask import Flask, request
from handler.messageHandler import messageHandler


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/MessagingApp_DB/home/')
def home():
    return 'home'


@app.route('/MessagingApp_DB/login/')
def log_in():
    return 'log in'


@app.route('/MessagingApp_DB/signup/')
def signup():
    return '<img src="https://www.cienciapr.org/sites/cienciapr.org/files/styles/article-page-node/public/img_8918.jpg?itok=kUprTzqX"> </img>' \
           '<p> esta pagina es para sign-upiar, del verbo sign up' \



@app.route('/MessagingApp_DB/messages')
def getAllMessages():
    if request.args:
        return messageHandler().getMessageBy(request.args)
    else:
        return messageHandler().getAllMessages()


@app.route('/MessagingApp_DB/messages/<int:mid>')
def getMessageByID(mid):
    return messageHandler().getMessageByID(mid)


@app.route('/MessagingApp_DB/messages/userID/<int:uid>')
def getMessagesByUserID(uid):
    return messageHandler().getMessagesByUserID(uid)


@app.route('/MessagingApp_DB/messages/groupchat/<int:gid>')
def getMessagesByGroupChatID(gid):
    return messageHandler().getMessagesByGroupChatID(gid)


@app.route('/MessagingApp_DB/messages/date/<string:date>')
def getMessagesByDate(date):
    return messageHandler().getMessagesByDate(date)


@app.route('/MessagingApp_DB/statistics/')
def statistics():
    return 'statistics'


if __name__ == '__main__':
    app.run()


