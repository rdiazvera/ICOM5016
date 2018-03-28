from flask import jsonify
from dao.replyDAO import ReplyDAO


class ReplyHandler:

    def mapToDict(self, r):
        result = {}
        result['reply_mid'] = r[0]
        result['replied_mid'] = [1]
        result['rid'] = [3]
        return result

    def getAllReply(self):
        dao = ReplyDAO()
        result = dao.getAllReply()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Reply=mapped_result)

    def getReplyById(self, rid):
        dao = ReplyDAO()
        result = dao.getReplyById(rid)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.mapToDict(result)
            return jsonify(Reply=mapped)
