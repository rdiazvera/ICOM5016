from flask import jsonify
from dao.userDAO import UserDAO


class UserHandler:

    def mapToDict(self, r):
        result = {}
        result['uid'] = r[0]
        result['first_name'] = r[1]
        result['last_name'] = r[2]
        result['password'] = r[3]
        result['phone'] = r[4]
        result['email'] = r[5]
        return result

    def getAllUsers(self):
        dao = UserDAO()
        result = dao.getAllUsers()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(User=mapped_result)

    def getUserById(self, id):
        dao = UserDAO()
        result = dao.getUserById(id)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = self.mapToDict(result)
            return jsonify(User=mapped)
