from flask import jsonify
from dao.usersDAO import UsersDAO
from handler import buildDict


# Handler Class to handle the Users and Contacts entities
class UsersHandler:

    # === User Getters === #

    # List of users in the system
    def getAllUsers(self):
        dao = UsersDAO()
        result = dao.getAllUsers()
        mapped_result = []
        for r in result:
            mapped_result.append(buildDict.build_users_dict(self, r))
        return jsonify(Users=mapped_result)

    def getUserById(self, id):
        dao = UsersDAO()
        result = dao.getUserById(id)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = buildDict.build_users_dict(self, result)
            return jsonify(Users=mapped)

    # Information on a given user (by id)
    def getUserInformationById(self, uid):
        dao = UsersDAO()
        result = dao.getUserInformationById(uid)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            # TODO: Edit
            mapped = buildDict.build_users_dict(self, result)
            return jsonify(Users=mapped)

    # Information on a given user (by username)
    def getUserInformationByUsername(self, username):
        dao = UsersDAO()
        result = dao.getUserInformationByUsername(username)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            # TODO: Edit
            mapped = buildDict.build_users_dict(self, result)
            return jsonify(Users=mapped)

    # === Contacts Getters === #

    # List of users in the contact list of some user X
    def getContactsOfUser(self, uid):
        dao = UsersDAO()
        result = dao.getContactsOfUser(uid)
        mapped_result = []
        for r in result:
            mapped_result.append(buildDict.build_users_dict(self, r))
        return jsonify(Users=mapped_result)
