create table User (
	uid serial primary key, 
	first_name varchar(20), 
	last_name varchar(20), 
	password varchar(20),
	phone varchar(10), 
	email varchar(20)
	)

create table Messages (
	mid serial primary key, 
	text varchar(250), 
	date_created varchar(10), 
	num_likes integer, 
	num_dislikes integer, 
	num_replies integer , 
	ownerid integer references User(uid),
	groupchatid integer references GroupChat(gid)
	)

create table GroupChat (
	gid serial primary key, 
	gname varchar(20), 
	ownerid integer references User(uid)
	)

create table Hashtag (
	hid serial primary key, 
	hstring varchar(20), 
	messageid integer references Messages(mid)
	)

create table isMember (
	userid integer references user(uid),
	groupchatid integer references GroupChat(gid),
	primary key (userid, groupchatid)
	)

create table Reactions (
	userid integer references User(uid),
	messageid integer references Messages(mid),
	type varchar(10), 
	primary key (userid, messageid)
	)

create table repliesTo(
	reply_mid integer references Messages(mid),
	replied_mid integer references Messages(mid),
	primary key (reply_mid, replied_mid)
	)

