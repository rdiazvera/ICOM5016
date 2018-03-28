class GroupChatDAO:
    def __init__(self):
        G1 = [101, 'Los Cool', 424]
        G2 = [74, 'Grupo Fisica Cuantica', 978]
        G3 = [276, 'Proyecto de DB', 345]

        self.data = []
        self.data.append(G1)
        self.data.append(G2)
        self.data.append(G3)

    def getAllGroupChats(self):
        return self.data

    def getGroupChatById(self, id):
        for r in self.data:
            if int(id) == r[0]:
                return r
        return None

    def getGroupChatByName(self, name):
        for r in self.data:
            if name == r[1]:
                return r
        return None

    def getGroupChatByOwnerId(self, id):
        for r in self.data:
            if id == r[2]:
                return r
        return None
