# === Python file that contains all the dictionaries builders === #

# GroupChats Dictionary Builder
def build_groupchats_dict(self, r):
    result = {}
    result['gid'] = r[0]
    result['gname'] = r[1]
    result['uid'] = r[2]
    return result

# Members Dictionary Builder
def build_members_dict(self, r):
    result = {}
    result['uid'] = r[0]
    result['gid'] = r[1]
    result['membersid'] = r[2]
    return result

# Messages Dictionary Builder
def build_messages_dict(self, r):
    result = {}
    result['mid'] = r[0]
    result['text'] = r[1]
    result['date_created'] = r[2]
    result['uid'] = r[3]
    result['groupchatid'] = r[4]
    return result

# Replies Dictionary Builder
def build_replies_dict(self, r):
    result = {}
    result['reply_mid'] = r[0]
    result['replied_mid'] = r[1]
    return result

# Reactions Dictionary Builder
def build_reactions_dict(self, r):
    result = {}
    result['uid'] = r[0]
    result['messageid'] = r[1]
    result['type'] = r[2]
    return result

# Hashtags Dictionary Builder
def build_hashtags_dict(self, r):
    result = {}
    result['hid'] = r[0]
    result['hstring'] = r[1]
    result['messageid'] = r[2]
    return result

# Users Dictionary Builder
def build_users_dict(self, r):
    result = {}
    result['uid'] = r[0]
    result['first_name'] = r[1]
    result['last_name'] = r[2]
    result['password'] = r[3]
    result['phone'] = r[4]
    result['email'] = r[5]
    result['username'] = r[6]
    return result

# Contacts Dictionary Builder
def build_contacts_dict(self, r):
    result = {}
    result['user1_uid'] = r[0]
    result['user2_uid'] = r[1]
    return result

# Reaction Count Dictionary Builder
def build_reaction_count_dict(self, r):
    result = {}
    result['count'] = r[0]
    return result