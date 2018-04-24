from flask import jsonify, request
from dao.messagesDAO import MessagesDAO
from handler import buildDict


# Handler Class to handle the Messages, Replies, Reactions and Hashtags entities
class MessagesHandler:

    # === Messages Getters === #

    # List of all messages in the system
    def getAllMessages(self):
        dao = MessagesDAO()
        result = dao.getAllMessages()
        mapped_result = []
        for r in result:
            mapped_result.append(buildDict.build_messages_dict(r))
        return jsonify(Messages=mapped_result)

    def getMessageById(self, mid):
        dao = MessagesDAO()
        result = dao.getMessageById(mid)
        mapped = []
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped = buildDict.build_messages_dict(r)
            return jsonify(Messages=mapped)


    # === Reactions Getters === #

    def getAllReactions(self):
        dao = MessagesDAO()
        result = dao.getAllReactions()
        mapped_result = []
        for r in result:
            mapped_result.append(buildDict.build_reactions_dict(r))
        return jsonify(Reactions=mapped_result)

    # Number of likes to a message
    def getNumberOfLikes(self, mid):
        dao = MessagesDAO()
        result = dao.getMessageById(mid)
        mapped = []
        for r in result:
            # TODO: Edit
            mapped.append(buildDict.build_reaction_count_dict(r))
        return jsonify(Likes=mapped)

    # List of users who liked a message
    def getUsersWhoLikeMessage(self, mid):
        dao = MessagesDAO()
        result = dao.getMessageByGroupChatId(mid)
        mapped_result = []
        for r in result:
            # TODO: Edit
            mapped_result.append(buildDict.build_users_dict(r))
        return jsonify(Users=mapped_result)

    # Number of dislikes to a message
    def getNumberOfDislikes(self, mid):
        dao = MessagesDAO()
        result = dao.getMessageById(mid)
        mapped = []
        for r in result:

            mapped.append(buildDict.build_reaction_count_dict(r))
        return jsonify(Dislikes=mapped)


    # List of users who dislikes a message
    def getUsersWhoDislikeMessage(self, mid):
        dao = MessagesDAO()
        result = dao.getMessageByGroupChatId(mid)
        mapped_result = []
        for r in result:
            # TODO: Edit
            mapped_result.append(buildDict.build_users_dict(r))
        return jsonify(Users=mapped_result)


    # === Replies Getters === #

    # === Hashtags Getters === #
