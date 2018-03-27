class reactionDAO:
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
        self.data.append(1)
        self.data.append(2)
        self.data.append(3)
        self.data.append(4)
        self.data.append(5)
        self.data.append(6)
        self.data.append(7)
        self.data.append(8)
        self.data.append(9)
        self.data.append(10)
        self.data.append(11)

    def getAllReaction(self):
        return self.data

    def getReactionById(self, id):
        for r in self.data:
            if id == r[3]:
                return r
        return None

    def getReactionByMessageId(self, mid):
        for r in self.data:
            if mid == r[1]:
                return r
        return None

    def getReactionByUserId(self, mid):
        for r in self.data:
            if mid == r[2]:
                return r
        return None
