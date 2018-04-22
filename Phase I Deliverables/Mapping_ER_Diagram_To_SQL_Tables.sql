create table user (
	uid serial primary key, 
	first_name varchar(20), 
	last_name varchar(20), 
	password varchar(25),
	phone varchar(10), 
	email varchar(50)
	)

create table message (
	mid serial primary key, 
	text varchar(250), 
	date_created timestamp, 
	uid integer references user(uid),
	gid integer references groupchat(gid)
	)

create table groupchat (
	gid serial primary key, 
	gname varchar(20), 
	uid integer references user(uid)
	)

create table hashtag (
	hid serial primary key, 
	hstring varchar(30) unique, 
	mid integer references message(mid)
	)

create table ismember (
	uid integer references user(uid),
	gid integer references groupchat(gid),
	primary key (uid, gid)
	)

create table reactions (
	uid integer references user(uid),
	mid integer references message(mid),
	type varchar(10), 
	primary key (uid, mid)
	)

create table replies (
	reply_mid integer references message(mid),
	replied_mid integer references message(mid),
	primary key (reply_mid, replied_mid)
	)
	
create table contacts (
	user1_uid integer references user(uid),
	user2_uid integer references user(uid),
	primary key (user1_uid, user2_uid)
	)
	

