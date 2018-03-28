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
        result['ownerid'] = row[6]
        result['groupchatid'] = row[7]
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

    def getMessageByID(self, mid):
        dao = MessagesDAO()
        result = dao.getMessageByID(mid)
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToSupDict(r))
        return jsonify(Messages=mapped_result)


      #  dao = MessagesDAO()
      #  result = dao.getMessageByID(id)
      #  if result is None:
      #      return jsonify(Error="NOT FOUND"), 404
      #  else:
      #      mapped = self.mapToDict(result)
      #      return jsonify(Messages=mapped)

    def getMessagesByUserID(self, uid):
        dao = MessagesDAO()
        result = dao.getMessagesByUserID(uid)
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToSupDict(r))
        return jsonify(Messages=mapped_result)

    def getMessagesByGroupChatID(self, gid):
        dao = MessagesDAO()
        result = dao.getMessageByGroupChatID(gid)
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToSupDict(r))
        return jsonify(Messages=mapped_result)

    def getMessageByText(self, text):
        dao = MessagesDAO()
        result = dao.getMessageByText(text)
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToSupDict(r))
        return jsonify(Messages=mapped_result)

    def getMessageByDate(self, date):
        dao = MessagesDAO()
        result = dao.getMessageByDate(date)
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

