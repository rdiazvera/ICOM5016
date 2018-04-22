create table users (
	uid serial primary key,
	first_name varchar(20),
	last_name varchar(20),
	password varchar(25),
	phone varchar(10),
	email varchar(50)
	);

create table groupchats (
	gid serial primary key,
	gname varchar(20),
	uid integer references users(uid)
	);

create table messages (
	mid serial primary key,
	text varchar(250),
	date_created timestamp,
	uid integer references users(uid),
	gid integer references groupchats(gid)
	);

create table hashtags (
	hid serial primary key,
	hstring varchar(30) unique,
	hcount integer,
	mid integer references messages(mid)
	);

create table members (
	uid integer references users(uid),
	gid integer references groupchats(gid),
	primary key (uid, gid)
	);

create table reactions (
	uid integer references users(uid),
	mid integer references messages(mid),
	type varchar(10),
	primary key (uid, mid)
	);

create table replies (
	reply_mid integer references messages(mid),
	replied_mid integer references messages(mid),
	primary key (reply_mid, replied_mid)
	);

create table contacts (
	users1_uid integer references users(uid),
	users2_uid integer references users(uid),
	primary key (users1_uid, users2_uid)
	);


