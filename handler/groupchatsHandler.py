from flask import jsonify
from dao.groupchatsDAO import GroupChatsDAO
from handler import buildDict
import datetime

# Handler Class to handle the GroupChats and Members entities
class GroupChatsHandler:

    # List of chats group in the system
    def getAllGroupChats(self):
        dao = GroupChatsDAO()
        result = dao.getAllGroupChats()
        mapped_result = []
        for r in result:
            mapped_result.append(buildDict.build_groupchats_dict(self, r))
        return jsonify(GroupChats=mapped_result)

    def getGroupChatById(self, gid):
        dao = GroupChatsDAO()
        result = dao.getGroupChatById(gid)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = buildDict.build_groupchats_dict(self, result)
            return jsonify(GroupChats=mapped)

    # List of messages posted to a chat group
    def getMessagesByGroupChatId(self, gid):
        dao = GroupChatsDAO()
        result = dao.getMessageByGroupChatId(gid)
        mapped_result = []
        for r in result:
            mapped_result.append(buildDict.build_all_messages_dict(self, r))
        return jsonify(Messages=mapped_result)

    # Owner of a given chat group
    def getOwnerOfGroupChat(self, gid):
        dao = GroupChatsDAO()
        result = dao.getOwnerOfGroupChat(gid)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = buildDict.build_users_dict(self, result)
            return jsonify(Owner=mapped)

    # List of users subscribed to a chat group
    def getUsersInAGroupChat(self, gid):
        dao = GroupChatsDAO()
        result = dao.getUsersInAGroupChat(gid)
        mapped = []
        for r in result:
            mapped.append(buildDict.build_users_dict(self, r))
        return jsonify(Users=mapped)

    # === Phase 3 === #
    def postMessage(self, gid, form):
        if len(form) != 2:
            return jsonify(Error="Malformed Post Request"), 400
        else:
            text = form['text']
            uid = form['uid']
            if text:


                dao = GroupChatsDAO()
                values = dao.postMessage(gid, text, uid)
                print(values[0][0])
                result = buildDict.build_msg_dict_by_att(self, values[0][0], text, datetime.datetime.now(), uid, gid)

                listOfStrings = str(text).split()
                for word in listOfStrings:
                    if word.find('#') != -1:
                        dao.insertHash(values[0][0], word.replace('#', ''))


                return jsonify(Message=result), 201
            else:
                return jsonify(Error="Unexpected attributes in this post request"), 400

    def addUsersToGroupChat(self, gid, form):
        uid = form['uid']
        mid = GroupChatsDAO().addUsersToGroupChat(gid, uid)
        result = buildDict.build_members_dict_by_attr(self, mid, gid)
        return jsonify(Member=result), 201

    def getMessagesByHashTagInGroup(self, gid, hstring):
        mapped_result = []
        result = GroupChatsDAO().getMessagesByHashTagInGroup(gid, hstring)
        for r in result:
            mapped_result.append(buildDict.build_messages_dict(self, r))
        return jsonify(Message=result), 201

    def replyToMessage(self, gid, form):
        uid = form['uid']
        replied_id = form['mid']
        text = form['text']
        values = GroupChatsDAO().replyToMessage(gid, uid, replied_id, text)
        mapped_result = []
        for r in values:
            mapped_result.append(buildDict.build_reply_dict_by_attr(self, r[0], r[1]))
        return jsonify(Reply=mapped_result), 201

    def availableGroupChats(self, uid):
        values = GroupChatsDAO().availableGroupChats(uid)
        mapped_result = []
        for r in values:
            mapped_result.append(buildDict.build_groupchats_dict(self, r))
        return jsonify(GroupChats=mapped_result), 201

