class MessagesDAO:
    def __init__(self):
        M1 = [1, 'Saludos cordiales #SoyCool #LaBestia #NecesitoAmigos', '2015-06-13 00:39:17', 2, 1, 6, 424, 101]
        M2 = [2, 'No voy a escribir mensajes obscenos', '2018-28-3 11:59:59', 0, 500, 4, 343, 345]
        M3 = [3, 'Porque mi equipo no me dejo #EstoNoEsUnaDemocracia', '2018-28-3 11:59:59', 0, 10000000, 3, 343, 345]
        M4 = [4, 'huqrqhwruhwqr #gibberish', '2018-29-3 11:59:59', 8, 4, 3, 343, 345]
        M5 = [5, 'asfaf', '2018-23-3 11:59:59', 111110, 2, 3, 987, 978]
        M6 = [6, 'fffffffffffffffffff  #EsperoQueNoSaquemosF', '2018-23-3 11:59:59', 0, 3, 3, 345, 978]

        self.data = []
        self.data.append(M1)
        self.data.append(M2)
        self.data.append(M3)
        self.data.append(M4)
        self.data.append(M5)
        self.data.append(M6)


def getAllMessages(self):
    return self.data


def getMessageById(self, id):
    for r in self.data:
        if id == r[3]:
            return r
    return None


def getMessageByGroupChatId(self, id):
    if id == 3:
        return [['123', 'Home Depot']]
    elif id == 122:
        T = []
        T.append(['123', 'Home Depot'])
        T.append(['456', 'National'])
        return T
    else:
        return []

def getMessagesByUserID(self, user_id):
    result = []
    if user_id == 343:
        for r in self.data:
         if user_id == 343:
            result.append(r)
    elif user_id == 345:
        for r in self.data:
            if user_id == 345:
                result.append(r)
    return result


def getMessageByDate(self, date):
        for r in self.data:
            if date == '2018-28-3 11:59:59':
                return r
            elif date == '2018-23-3 11:59:59':
                return r
            else:
                return []

def getMessageByText(self, text):
    for r in self.data:
        if text == 'asfaf':
            return r
        elif text == 'No voy a escribir mensajes obscenos':
            return r
        else:
            return []

def searchByColor(self, color):
    result = []
    for r in self.data:
        if color == r[3]:
            result.append(r)
    return result