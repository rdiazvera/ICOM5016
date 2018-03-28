class UserDAO:
    def __init__(self):
        U1 = [424, 'Apu', 'Las', 'troij90wf', '787-832-4040', 'apu.las@upr.edu']
        U2 = [987, 'Jil', 'Mas', 'hytrty12', '787-832-4141', 'jil.mas@upr.edu']
        U3 = [343, 'Bob', 'Nas', 'treyte3', '787-832-4242', 'bob.nas@upr.edu']
        U4 = [963, 'Amy', 'Pas', 'tret6654', '787-832-4343', 'amy.pas@upr.edu']
        U5 = [345, 'Ron', 'Qas', 'retree76', '787-832-4545', 'ron.qas@upr.edu']

        self.data = []
        self.data.append(U1)
        self.data.append(U2)
        self.data.append(U3)
        self.data.append(U4)
        self.data.append(U5)

    def getAllUsers(self):
        return self.data

    def getUserById(self, id):
        for r in self.data:
            if id == r[0]:
                return r
        return None

    def getUsersByNameFirst(self, name):
        result = []
        for r in self.data:
            if name == r[1]:
                result.append(r)
        return result

    def getUsersByNameLast(self, name):
        result = []
        for r in self.data:
            if name == r[2]:
                result.append(r)
        return result

    def getUserByPhone(self, phone):
        for r in self.data:
            if phone == r[4]:
                return r
        return None

    def getUserByEmail(self, email):
        for r in self.data:
            if email == r[5]:
                return r
        return None
