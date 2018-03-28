from flask import jsonify, request
from dao.messageDAO import MessagesDAO


class messageHandler:

    def mapToDict(self, row):
        result = {}
        result['mid'] = row[0]
        result['text'] = row[1]
        result['date_created'] = row[2]
        result['num_likes'] = row[3]
        result['num_dislikes'] = row[4]
        result['num_replies'] = row[5]
        result['ownerid'] = row[6]
        result['groupchatid'] = row[7]
        return result

    def getAllMessages(self):
        dao = MessagesDAO()
        result = dao.getAllMessages()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Message=mapped_result)

    def getMessageByID(self, mid):
        dao = MessagesDAO()
        result = dao.getMessageByID(mid)
        mapped = []
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped = self.mapToDict(r)
            return jsonify(Message=mapped)

    def getMessagesByOwnerID(self, ownerid):
        dao = MessagesDAO()
        result = dao.getMessagesByOwnerID(ownerid)
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Message=mapped_result)

    def getMessagesByGroupChatID(self, groupchatid):
        dao = MessagesDAO()
        result = dao.getMessageByGroupChatID(groupchatid)
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Message=mapped_result)

    def getMessageByText(self, text):
        dao = MessagesDAO()
        result = dao.getMessageByText(text)
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Message=mapped_result)

    def getMessageByDate(self, date):
        dao = MessagesDAO()
        result = dao.getMessageByDate(date)
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Message=mapped_result)

    def getMessageBy(self, args):
        ownerID = args.get('id')
        dao = MessagesDAO()
        result = dao.getMessagesByOwnerID(ownerID)
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Message=mapped_result)

