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

    # === PHASE 3 === #

    # List of chat groups to which a user belongs
    def getGroupChatbyUserId(self, uid):
        dao = UsersDAO()
        result = dao.getGroupChatbyUserId(uid)
        mapped_result = []
        for r in result:
            mapped_result.append(buildDict.build_groupchats_dict(self, r))
        return jsonify(GroupChats=mapped_result)

    # === Contacts Getters === #

    # List of users in the contact list of some user X
    def getContactsOfUser(self, uid):
        dao = UsersDAO()
        result = dao.getContactsOfUser(uid)
        mapped_result = []
        for r in result:
            mapped_result.append(buildDict.build_users_dict(self, r))
        return jsonify(Contacts=mapped_result)

    def loginUser(self, form):
        dao = UsersDAO()
        username = form['username']
        password = form['password']
        result = dao.loginUser(username, password)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = buildDict.build_users_dict(self, result)
            return jsonify(Users=mapped)

    def registerUser(self, form):
        if len(form) != 6:
            return jsonify(Error="Malformed Post Request"), 400
        else:
            username = form['username']
            password = form['password']
            first_name = form['first_name']
            last_name = form['last_name']
            email = form['email']
            phone = form['phone']
            if username and password and first_name and last_name and email and phone:
                dao = UsersDAO()
                uid = dao.registerUser(username, password, first_name, last_name, email, phone)
                result = buildDict.build_users_dict_by_att(self, uid, first_name, last_name, password, phone, email, username)
                return jsonify(User=result), 201
            else:
                return jsonify(Error="Unexpected attributes in this post request"), 400




