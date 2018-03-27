class replyDAO:
    def __init__(self):
        M1 = [4, 2, 1]
        M1 = [6, 5, 1]

        self.data = []
        self.data.append()

    def getAllReply(self):
        return self.data

    def getReplyById(self, id):
        for r in self.data:
            if id == r[2]:
                return r
        return None

    def getReplyByReplyId(self, reply_id):
        for r in self.data:
            if reply_id == r[0]:
                return r
        return None

    def getReplyByRepliedId(self, replied_id):
        for r in self.data:
            if replied_id == r[1]:
                return r
        return None
