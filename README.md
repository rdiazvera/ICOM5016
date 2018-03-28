Phase I Database Project: MessagingApp_DB

----------------------------------------------
                   ROUTES
----------------------------------------------

GENERAL PURPOSES:
    /
    /MessagingApp_DB/home/
    /MessagingApp_DB/login/
    /MessagingApp_DB/signup/

STATISTICS PURPOSES:
    /MessagingApp_DB/statistics/
    #TODO

MESSAGE TABLE:
    /MessagingApp_DB/messages
    /MessagingApp_DB/messages/(mid)/
    /MessagingApp_DB/messages/owner/(ownerid)/
    /MessagingApp_DB/messages/groupchat/(groupchatid)/
    /MessagingApp_DB/messages/date/(date)/

USER TABLE:
    /MessagingApp_DB/users/
    /MessagingApp_DB/users/(uid)/

GROUP CHAT TABLE:
    /MessagingApp_DB/groupchats/
    /MessagingApp_DB/groupchats/(gid)/

MEMBER TABLE:
    /MessagingApp_DB/members/
    /MessagingApp_DB/members/(mid)/

REACTION TABLE:
    /MessagingApp_DB/reactions/
    /MessagingApp_DB/reactions/(rid)/

REPLY TABLE:
    /MessagingApp_DB/replies/
    /MessagingApp_DB/replies/(rid)/

HASHTAG TABLE:
    /MessagingApp_DB/hashtags/
    /MessagingApp_DB/hashtags/(hid)/