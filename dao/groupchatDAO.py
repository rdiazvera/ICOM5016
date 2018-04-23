from config.dbconfig import pg_config
import psycopg2


# Data Access Object (DAO) Class to access the GroupChats and Members entities
class GroupChatDAO:

    # Initialization Method (Class Constructor)
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    # === GroupChat Getters === #

    # List of chats group in the system
    def getAllGroupChats(self):
        cursor = self.conn.cursor()
        query = "select * from groupchats;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getGroupChatById(self, gid):
        cursor = self.conn.cursor()
        query = "select * from groupchats where gid = %s;"
        cursor.execute(query, (gid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Owner of a given chat group
    def getOwnerOfGroupChat(self, gid):
        cursor = self.conn.cursor()
        query = "select uid, first_name, last_name, password, phone, email " \
                "from groupchats natural inner join users where gid = %s;"
        cursor.execute(query, (gid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # === Members Getters === #

    # List of users subscribed to a chat group
    def getUsersInAGroupChat(self, gid):
        cursor = self.conn.cursor()
        query = "select uid, first_name, last_name, password, phone, email " \
                "from members natural inner join users where gid = %s;"
        cursor.execute(query, (gid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
