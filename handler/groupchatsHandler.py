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
            mapped_result.append(buildDict.build_groupchats_dict(r))
        return jsonify(GroupChats=mapped_result)

    def getGroupChatById(self, gid):
        dao = GroupChatsDAO()
        result = dao.getGroupChatById(gid)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = buildDict.build_groupchats_dict(result)
            return jsonify(GroupChats=mapped)

    # List of messages posted to a chat group
    def getMessagesByGroupChatId(self, gid):
        dao = GroupChatsDAO()
        result = dao.getMessageByGroupChatId(gid)
        mapped_result = []
        for r in result:
            mapped_result.append(buildDict.build_messages_dict(r))
        return jsonify(Messages=mapped_result)

    # Owner of a given chat group
    def getOwnerOfGroupChat(self, gid):
        dao = GroupChatsDAO()
        result = dao.getGroupChatById(gid)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = buildDict.build_users_dict(result)
            return jsonify(Users=mapped)

    # List of users subscribed to a chat group
    def getUsersInAGroupChat(self, gid):
        dao = GroupChatsDAO()
        result = dao.getGroupChatById(gid)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = buildDict.build_users_dict(result)
            return jsonify(GroupChats=mapped)
