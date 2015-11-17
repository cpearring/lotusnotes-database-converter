#!/usr/bin/python

import sqlite3

# if database isn't available, it'll make the database
# for now, database is stored locally, want to make server side someday
conn = sqlite3.connect('tech_lotus.db')
print "Connected and opened VTECHZ database";

conn.execute('''CREATE TABLE VTECHZ
	(ID INT PRIMARY KEY		NOT NULL,
	NAME		TEXT	NOT NULL,
	REQDATE		TEXT	NOT NULL,
	NEEDDATE	TEXT	NOT NULL,
	PROBLEM		TEXT	NOT NULL,
	COMPLETEDBY	TEXT	NOT NULL,
	STATUS		INT		NOT NULL,
	PHONE		INT		NOT NULL,
	REVISIONS	INT		NOT NULL,
	CREATEDATE	TEXT	NOT NULL,
	EDITDATE	TEXT	NOT NULL);''')
print "Table created";

conn.close()
