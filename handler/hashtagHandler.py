from flask import jsonify
from dao.hashtagDAO import HashtagDAO

class HashtagHandler:

    def mapToDict(self, r):
        result = {}
        result['hid'] = r[0]
        result['hstring'] = [1]
        result['messageid'] = r[2]
        return result

    def getAllHashtags(self):
        dao = HashtagDAO()
        result = dao.getAllHashtags()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Hashtag=mapped_result)

    def getHashtagById(self, hid):
        dao = HashtagDAO()
        result = dao.getUserById(hid)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = self.mapToDict(result)
            return jsonify(Hashtag=mapped)
