create table User (
	uid serial primary key, 
	first_name varchar(20), 
	last_name varchar(20), 
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
	uid integer references User(uid),
	gid integer references GroupChat(gid)
	)

create table GroupChat (
	gid serial primary key, 
	gname varchar(20), 
	uid integer references User(uid)
	)

create table Hashtag (
	hid serial primary key, 
	hstring varchar(20), 
	mid integer references Messages(mid)
	)

create table isPartOf(
	uid integer references user(uid), 
	gid integer references GroupChat(gid), 
	primary key (uid, gid)
	)

create table Reactions (
	uid integer references User(uid), 
	mid integer references Messages(mid), 
	type varchar(10), 
	primary key (uid, mid)
	)

Create table repliesTo(
	reply_id integer references Messages(mid), 
	replied_id integer references Messages(mid), 
	primary key (mid, mid)
	)

