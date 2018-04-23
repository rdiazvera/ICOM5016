from flask import jsonify
from dao.groupchatDAO import GroupChatDAO
from handler import buildDict


# Handler Class to handle the GroupChats and Members entities
class GroupChatHandler:

    # List of chats group in the system
    def getAllGroupChats(self):
        dao = GroupChatDAO()
        result = dao.getAllGroupChats()
        mapped_result = []
        for r in result:
            mapped_result.append(buildDict.build_groupchats_dict(r))
        return jsonify(GroupChats=mapped_result)

    def getGroupChatById(self, gid):
        dao = GroupChatDAO()
        result = dao.getGroupChatById(gid)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = buildDict.build_groupchats_dict(result)
            return jsonify(GroupChats=mapped)

    # Owner of a given chat group
    def getOwnerOfGroupChat(self, gid):
        dao = GroupChatDAO()
        result = dao.getGroupChatById(gid)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            # TODO: Edit
            mapped = buildDict.build_users_dict(result)
            return jsonify(GroupChats=mapped)

    # List of users subscribed to a chat group
    def getUsersInAGroupChat(self, gid):
        dao = GroupChatDAO()
        result = dao.getGroupChatById(gid)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = buildDict.build_users_dict(result)
            return jsonify(GroupChats=mapped)
