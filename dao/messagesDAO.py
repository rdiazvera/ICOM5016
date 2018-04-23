from config.dbconfig import pg_config
import psycopg2


# Data Access Object (DAO) Class to access the Messages, Replies, Reactions and Hashtags entities
class MessagesDAO:

    # Initialization Method (Class Constructor)
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    # === Messages Getters === #

    # List of all messages in the system
    def getAllMessages(self):
        cursor = self.conn.cursor()
        query = "select * from messages;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessageById(self, mid):
        cursor = self.conn.cursor()
        query = "select * from messages where mid = %s;"
        cursor.execute(query, (mid,))
        result = cursor.fetchone()
        return result

    # === Reactions Getters === #

    def getAllReactions(self):
        cursor = self.conn.cursor()
        query = "select * from reactions;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Number of likes to a message
    def getNumberOfLikes(self, mid):
        cursor = self.conn.cursor()
        query = "select count(*) from reactions where mid = %s and type= \"like\";"
        cursor.execute(query, (mid,))
        result = cursor.fetchone()
        return result

    # List of users who liked a message
    def getUsersWhoLikeMessage(self, mid):
        cursor = self.conn.cursor()
        query = "select uid from reactions natural inner join users where mid = %s and type= \"like\";"
        cursor.execute(query, (mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Number of dislikes to a message
    def getNumberOfDislikes(self, mid):
        cursor = self.conn.cursor()
        query = "select count(*) from reactions where mid = %s and type= \"dislike\";"
        cursor.execute(query, (mid,))
        result = cursor.fetchone()
        return result

    # List of users who dislikes a message
    def getUsersWhoDislikeMessage(self, mid):
        cursor = self.conn.cursor()
        query = "select uid from reactions natural inner join users where mid = %s and type= \"like\";"
        cursor.execute(query, (mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # === Replies Getters === #

    # === Hashtags Getters === #
