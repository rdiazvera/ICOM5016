from config.dbconfig import pg_config
import psycopg2

class ReactionDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllReactions(self):
        cursor = self.conn.cursor()
        query = "select * from reactions;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getNumberOfLikes(self, mid):
        cursor = self.conn.cursor()
        query = "select count(*) from reactions where mid = %s and type= \"like\";"
        cursor.execute(query, (mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getNumberOfDislikes(self, mid):
        cursor = self.conn.cursor()
        query = "select count(*) from reactions where mid = %s and type= \"dislike\";"
        cursor.execute(query, (mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result