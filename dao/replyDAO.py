class ReplyDAO:
    def __init__(self):
        M1 = [4, 2, 1]
        M2 = [6, 5, 2]

        self.data = []
        self.data.append(M1)
        self.data.append(M2)

    def getAllReplies(self):
        return self.data

    def getReplyById(self, id):
        for r in self.data:
            if int(id) == r[2]:
                return r
        return None

    def getReplyByReplyId(self, reply_id):
        for r in self.data:
            if int(reply_id) == r[0]:
                return r
        return None

    def getReplyByRepliedId(self, replied_id):
        for r in self.data:
            if int(replied_id) == r[1]:
                return r
        return None
