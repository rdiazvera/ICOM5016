class ReactionDAO:
    def __init__(self):
        M1 = [987, 4, 'like', 1]
        M2 = [963, 4, 'like', 2]
        M3 = [987, 2, 'dislike', 3]
        M4 = [987, 3, 'like', 4]
        M5 = [424, 5, 'dislike', 5]
        M6 = [343, 5, 'dislike', 6]
        M7 = [963, 5, 'dislike', 7]
        M8 = [424, 6, 'like', 8]
        M9 = [343, 6, 'dislike', 9]
        M10 = [987, 6, 'like', 10]
        M11 = [345, 5, 'dislike', 11]

        self.data = []
        self.data.append(M1)
        self.data.append(M2)
        self.data.append(M3)
        self.data.append(M4)
        self.data.append(M5)
        self.data.append(M6)
        self.data.append(M7)
        self.data.append(M8)
        self.data.append(M9)
        self.data.append(M10)
        self.data.append(M11)

    def getAllReactions(self):
        return self.data

    def getReactionById(self, id):
        for r in self.data:
            if int(id) == r[3]:
                return r
        return None

    def getReactionByMessageId(self, mid):
        for r in self.data:
            if int(mid) == r[1]:
                return r
        return None

    def getReactionByUserId(self, mid):
        for r in self.data:
            if int(mid) == r[2]:
                return r
        return None
