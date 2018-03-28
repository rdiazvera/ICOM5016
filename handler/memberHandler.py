from flask import jsonify
from dao.memberDAO import MemberDAO

class MemberHandler:

    def mapToDict(self, r):
        result = {}
        result['userid'] = r[0]
        result['groupchatid'] = r[1]
        result['memberid'] = r[2]
        return result

    def getAllMembers(self):
        dao = MemberDAO()
        result = dao.getAllMembers()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Member=mapped_result)

    def getMemberById(self, mid):
        dao = MemberDAO()
        result = dao.getMemberById(mid)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = self.mapToDict(result)
            return jsonify(Member=mapped)
