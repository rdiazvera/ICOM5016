from flask import jsonify
from dao.reactionDAO import ReactionDAO


class ReactionHandler:

    def mapToDict(self, r):
        result = {}
        result['userid'] = r[0]
        result['messageid'] = r[1]
        result['type'] = r[2]
        result['reactionid'] = r[3]
        return result

    def getAllReactions(self):
        dao = ReactionDAO()
        result = dao.getAllReactions()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Reaction=mapped_result)

    def getReactionById(self, rid):
        dao = ReactionDAO()
        result = dao.getReactionById(rid)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = self.mapToDict(result)
            return jsonify(Reaction=mapped)
