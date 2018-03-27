class HashtagDAO:
    def __init__(self):
        H1 = [212, 'SoyCool', 1]
        H2 = [123, 'LaBestia', 1]
        H3 = [34, 'NecesitoAmigos', 1]
        H4 = [942, 'EstoNoEsUnaDemocracia', 3]
        H5 = [454, 'gibberish', 4]
        H6 = [872, 'EsperoQueNoSaquemosF', 5]

        self.data = []
        self.data.append(H1)
        self.data.append(H2)
        self.data.append(H3)
        self.data.append(H4)
        self.data.append(H5)
        self.data.append(H6)

    def getAllHashtags(self):
        return self.data

    def getHashtagById(self, id):
        for r in self.data:
            if id == r[0]:
                return r
        return None

    def getHashtagByMessageId(self, name):
        for r in self.data:
            if name == r[1]:
                return r
        return None