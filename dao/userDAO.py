from config.dbconfig import pg_config
import psycopg2


# Data Access Object (DAO) Class to access the Users and Contacts entities
class UserDAO:

    # Initialization Method (Class Constructor)
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    # === User Getters === #

    # List of users in the system
    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select * from users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserById(self, uid):
        cursor = self.conn.cursor()
        query = "select * from users where uid = %s;"
        cursor.execute(query, (uid,))
        result = cursor.fetchone()
        return result

    #Information on a given user (by id)
    def getUserInformationById(self, uid):
        cursor = self.conn.cursor()
        query = "select * from users where uid = %s;"
        cursor.execute(query, (uid,))
        result = cursor.fetchone()
        return result

    #Information on a given user (by username)
    def getUserInformationByUsername(self, username):
        cursor = self.conn.cursor()
        query = "select * from users where username = %s;"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        return result

    # === Contacts Getters === #

    # List of users in the contact list of some user X
    def getContactsOfUser(self, uid):
        cursor = self.conn.cursor()
        # TODO: Edit
        query = "select user1_uid from contacts where uid = %s;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result