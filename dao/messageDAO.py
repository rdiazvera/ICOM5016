class MessagesDAO:
    def __init__(self):
        M1 = [1, 'Saludos cordiales #SoyCool #LaBestia #NecesitoAmigos', '2015-06-13 00:39:17', 2, 1, 6, 424, 101]
        M2 = [2, 'No voy a escribir mensajes obscenos', '2018-28-3 11:50:59', 0, 500, 4, 343, 74]
        M3 = [3, 'Porque mi equipo no me dejo #EstoNoEsUnaDemocracia', '2018-28-3 11:59:59', 0, 10000000, 3, 343, 74]
        M4 = [4, 'huqrqhwruhwqr #gibberish #icom5016', '2018-29-3 11:51:59', 8, 4, 3, 343, 74]
        M5 = [5, 'asfaf #icom5016', '2018-23-3 11:11:59', 111110, 2, 3, 987, 276]
        M6 = [6, 'fffffffffffffffffff #EsperoQueNoSaquemosF #icom5016', '2018-23-3 11:45:59', 0, 3, 3, 345, 276]

        self.data = []
        self.data.append(M1)
        self.data.append(M2)
        self.data.append(M3)
        self.data.append(M4)
        self.data.append(M5)
        self.data.append(M6)


    def getAllMessages(self):
        return self.data

    def getMessageByID(self, mid):
        result = []
        for r in self.data:
            if r[0] == int(mid):
                result.append(r)
        return result

    def getMessageByGroupChatID(self, groupchatid):
        result = []
        for r in self.data:
            if r[7] == int(groupchatid):
                result.append(r)
        return result

    def getMessagesByOwnerID(self, ownerid):
        result = []
        for r in self.data:
            if r[6] == int(ownerid):
                result.append(r)
        return result

    def getMessageByDate(self, date):
        result = []
        for r in self.data:
            if r[2].split()[0] == date:
                result.append(r)
        return result

    def getMessageByText(self, text):
        result = []
        for r in self.data:
            if r[1] == text:
                result.append(r)
        return result



