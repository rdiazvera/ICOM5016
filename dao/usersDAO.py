from config.dbconfig import pg_config
import psycopg2


# Data Access Object (DAO) Class to access the Users and Contacts entities
class UsersDAO:

    # Initialization Method (Class Constructor)
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2.connect(connection_url)

    # === User Getters === #

    # List of users in the system
    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select uid, first_name, last_name, password, phone, email, username from users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Information on a given user (by id)
    def getUserInformationById(self, uid):
        cursor = self.conn.cursor()
        query = "select uid, first_name, last_name, password, phone, email, username from users where uid = %s;"
        cursor.execute(query, (uid,))
        result = cursor.fetchone()
        return result

    # Information on a given user (by username)
    def getUserInformationByUsername(self, username):
        cursor = self.conn.cursor()
        query = "select uid, first_name, last_name," \
                " password, phone, email, username from users where username = %s;"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        return result

    # List of chat groups to which a user belongs
    def getGroupChatbyUserId(self, uid):
        cursor = self.conn.cursor()
        query = "select * from groupchats where gid in (select gid from members where uid = %s)"
        cursor.execute(query, uid)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # === Contacts Getters === #

    # List of users in the contact list of some user X
    def getContactsOfUser(self, uid):
        cursor = self.conn.cursor()
        query = "select uid, first_name, last_name, password, " \
                "phone, email, username from users natural inner join (select users1_uid as uid from " \
                "contacts where	users2_uid = %s union select users2_uid as uid from " \
                "contacts where users1_uid = %s) as P; "
        cursor.execute(query, (uid, uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # === Phase 3 === #

    # == Login User == #

    def loginUser(self, username, password):
        cursor = self.conn.cursor()
        query = "select * from users where username = '%s' and password = '%s'"
        cursor.execute(query, (username, password,))
        result = cursor.fetchone()
        return result

    # == Register user === #

    def registerUser(self, username, password, first_name, last_name, email, phone):
        cursor = self.conn.cursor()
        query = "insert into users(first_name, last_name, password, phone, email, username) " \
                "values (%s, %s, %s, %s, %s, %s) returning uid;"
        cursor.execute(query, (first_name, last_name, password, phone, email, username))
        uid = cursor.fetchone()[0]
        self.conn.commit()
        return uid