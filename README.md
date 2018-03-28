# Database Project: MessagingApp_DB

Backend of an application used for messaging in a social context.

## Available Routes
These routes will be use to get data from the database.

### General Purposes Routes
These routes will be used for login/signin information and initial home page.
```
/
/MessagingApp_DB/home/
/MessagingApp_DB/login/
/MessagingApp_DB/signup/
```

### Statistics Purposes Routes
These routes will be used for getting statistics from the application.
```
/MessagingApp_DB/statistics/
```

### Message Table Routes
These routes will be used for getting data from the Messages Table.
```
/MessagingApp_DB/messages
/MessagingApp_DB/messages/(mid)/
/MessagingApp_DB/messages/owner/(ownerid)/
/MessagingApp_DB/messages/groupchat/(groupchatid)/
/MessagingApp_DB/messages/date/(date)/
```

### User Table Routes
These routes will be used for getting data from the Users Table.
```
/MessagingApp_DB/users/
/MessagingApp_DB/users/(uid)/
```

### GroupChats Table Routes
These routes will be used for getting data from the GroupChats Table.
```
/MessagingApp_DB/groupchats/
/MessagingApp_DB/groupchats/(gid)/
```

### Members Table Routes
These routes will be used for getting data from the Members Table.
```
/MessagingApp_DB/members/
/MessagingApp_DB/members/(mid)/
```

### Reactions Table Routes
These routes will be used for getting data from the Reactions Table.
```
/MessagingApp_DB/reactions/
/MessagingApp_DB/reactions/(rid)/
```

### Replies Table Routes
These routes will be used for getting data from the Replies Table.
```
/MessagingApp_DB/replies/
/MessagingApp_DB/replies/(rid)/
```

### Hashtags Table Routes
These routes will be used for getting data from the Hashtags Table.
```
/MessagingApp_DB/hashtags/
/MessagingApp_DB/hashtags/(hid)/
```


