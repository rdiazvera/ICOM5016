from flask import jsonify
from dao.groupchatsDAO import GroupChatsDAO
from handler import buildDict


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
            mapped_result.append(buildDict.build_messages_dict(self, r))
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
        if len(form) != 1:
            return jsonify(Error="Malformed Post Request"), 400
        else:
            text = form['text']
            uid = form['uid']
            if text:
                dao = GroupChatsDAO()
                values = dao.postMessage(gid, text, uid)
                result = buildDict.build_msg_dict_by_att(values[0], text, values[1], gid, uid)
                return jsonify(Message=result), 201
            else:
                return jsonify(Error="Unexpected attributes in this post request"), 400

    def addUsersToGroupChat(self, gid, form):
        uid = form['uid']
        GroupChatsDAO().addUsersToGroupChat(gid, uid)
        result = buildDict.build_members_dict(uid, gid)
        return jsonify(Member=result), 201

    def getMessagesByHashTagInGroup(self, gid, form):
        if len(form) != 1:
            return jsonify(Error="Malformed Post Request"), 400
        else:
            hstring = form['hstring']
            if hstring:
                mapped_result = []
                result = GroupChatsDAO().getMessagesByHashTagInGroup(gid, hstring)
                for r in result:
                    mapped_result.append(buildDict.build_messages_dict(self, r))
                return jsonify(Message=result), 201
            else:
                return jsonify(Error="Unexpected attributes in this post request"), 400
