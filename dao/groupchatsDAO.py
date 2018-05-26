from config.dbconfig import pg_config
import psycopg2


# Data Access Object (DAO) Class to access the GroupChats and Members entities
class GroupChatsDAO:

    # Initialization Method (Class Constructor)
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2.connect(connection_url)

    # === GroupChat Getters === #

    # List of chats group in the system
    def getAllGroupChats(self):
        cursor = self.conn.cursor()
        query = "select gid, gname, uid from groupchats;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getGroupChatById(self, gid):
        cursor = self.conn.cursor()
        query = "select gid, gname, uid from groupchats where gid = %s;"
        cursor.execute(query, (gid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # List of messages posted to a chat group
    def getMessageByGroupChatId(self, gid):
        cursor = self.conn.cursor()
        query = "select username, messages.mid, text, date_created, uid as author, gid, coalesce(likes, 0)" \
                " as likes, coalesce(dislikes,0) as dislikes, first_name, last_name from users natural inner" \
                " join messages left join (select m.mid, count(case when type = 'like' then 1 else null end) " \
                "as likes, count(case when type='dislike' then 1 else null end) as dislikes from messages as m, " \
                "reactions as r where m.mid = r.mid group by m.mid) as reaction on messages.mid = reaction.mid " \
                "where gid = %s group by messages.mid, username, uid, likes, dislikes order by date_created desc;"
        cursor.execute(query, (gid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Owner of a given chat group
    def getOwnerOfGroupChat(self, gid):
        cursor = self.conn.cursor()
        query = "select uid, first_name, last_name, password, phone, email, username " \
                "from groupchats natural inner join users where gid = %s;"
        cursor.execute(query, (gid,))
        result = cursor.fetchone()
        return result

    # === Members Getters === #

    # List of users subscribed to a chat group
    def getUsersInAGroupChat(self, gid):
        cursor = self.conn.cursor()
        query = "select uid, first_name, last_name, password, phone, email, username " \
                "from members natural inner join users where gid = %s;"
        cursor.execute(query, (gid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # == PHASE 3 == #
    def postMessage(self, gid, text, uid):
        cursor = self.conn.cursor()
        query = "INSERT into messages(text, date_created, uid, gid) values (%s, current_timestamp, %s, %s) " \
                "returning mid, date_created;"
        cursor.execute(query, (text, uid, gid,))
        mid = []
        for row in cursor:
            mid.append(row)
        self.conn.commit()
        return mid

    def addUsersToGroupChat(self, gid, uid):
        cursor = self.conn.cursor()
        query = "INSERT into members(gid, uid) values (%s, %s) returning gid;"
        cursor.execute(query, (gid, uid))
        gid = cursor.fetchone()[0]
        self.conn.commit()
        return gid

    def getMessagesByHashTagInGroup(self, gid, hstring):
        cursor = self.conn.cursor()
        query = "select * from groupchats natural inner join messages where mid in (select mid from " \
                "hashtags where hstring = %s) and gid = %s"
        cursor.execute(query, (hstring, gid))
        result = []
        for row in cursor:
            result.append(row)
        return result
