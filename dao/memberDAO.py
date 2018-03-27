class memberDAO:
    def __init__(self):
        M1 = [424, 101, 1]
        M2 = [424, 276, 2]
        M3 = [987, 276, 3]
        M4 = [987, 74, 4]
        M5 = [343, 276, 5]
        M6 = [343, 74, 5]
        M7 = [963, 276, 6]
        M8 = [963, 74, 7]
        M9 = [345, 276, 8]

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

    def getAllMembers(self):
        return self.data

    def getMemberById(self, id):
        for r in self.data:
            if id == r[2]:
                return r
        return None

    def getMemberByGroupId(self, gid):
        for r in self.data:
            if gid == r[1]:
                return r
        return None

    def getMemberByUserId(self, uid):
        for r in self.data:
            if uid == r[0]:
                return r
        return None