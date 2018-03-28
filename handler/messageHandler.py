from flask import jsonify, request
from dao.message import MessagesDAO


class messageHandler:

    def mapToDict(self, row):
        result = {}
        result['mid'] = row[0]
        result['text'] = row[1]
        result['date_created'] = row[2]
        result['num_likes'] = row[3]
        result['num_dislikes'] = row[4]
        result['num_replies'] = row[5]
        result['uid'] = row[6]
        result['gid'] = row[7]
        return result

    def getAllMessages(self):
        dao = MessagesDAO()
        result = dao.getAllMessages()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Part=mapped_result)

    def mapToSupDict(self, row):
        result = {}
        result['sid'] = row[0]
        result['sname'] = row[1]
        return result

    def getPartById(self, id):
        dao = MessagesDAO()
        result = dao.getPartById(id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = self.mapToDict(result)
            return jsonify(Part=mapped)

    def getMessagesByPartId(self, id):
        dao = MessagesDAO()
        result = dao.getMessagesByPartId(id)
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToSupDict(r))
        return jsonify(Messages=mapped_result)

    def getMessageBy(self, args):
        userID = args.get('id')
        dao = MessagesDAO()
        result = dao.getMessagesByUserID(userID)
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Messages=mapped_result)


    def searchParts(self, args):
        color = args.get('color')
        dao = MessagesDAO()
        result = dao.searchByColor(color)
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Part=mapped_result)
