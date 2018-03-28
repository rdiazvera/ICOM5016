from flask import jsonify
from dao.groupchatDAO import GroupChatDAO


class GroupChatHandler:

    def mapToDict(self, r):
        result = {}
        result['gid'] = r[0]
        result['gname'] = r[1]
        result['ownerid'] = r[2]
        return result

    def getAllGroupChats(self):
        dao = GroupChatDAO()
        result = dao.getAllGroupChats()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(GroupChat=mapped_result)

    def getGroupChatById(self, gid):
        dao = GroupChatDAO()
        result = dao.getGroupChatById(gid)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = self.mapToDict(result)
            return jsonify(GroupChat=mapped)

    def getGroupChatByOwnerId(self, owner):
        dao = GroupChatDAO()
        result = dao.getGroupChatByOwnerId(owner)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = self.mapToDict(result)
            return jsonify(GroupChat=mapped)
