#!/usr/bin/python
# Casey Pearring
# CS 294

# lol test the pushing notifcation for slack

import sqlite3

# if database isn't available, it'll make the database
# for now, database is stored locally, want to make server side someday
conn = sqlite3.connect('tech_lotus.db')
print "Connected and opened VTECHZ database";

# lol if not exists
conn.execute('''CREATE TABLE IF NOT EXISTS VTECHZ
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

# open file, want requisition date, need date, problem, completed by
# status, phone #, revisions, date created, and date edited
f = open('test input for issue 1.txt','r')
for line in f:
	# gonna be a lot of if statements here
	# requisition_date will be the first input that we need, so we can start
	# the table there, and then add stuff until the next requisition_date
	if 'requisition_date' in line:
		print line
	elif 'need_date:' in line:
	elif 'problem:' in line:
	elif 'CompletedBy:' in line:
	elif 'status:' in line:
	elif 'phone:' in line:
	elif '$Revisions:' in line:
	elif 'date_created:' in line:
	elif 'date_edited:' in line:
			
		

conn.close()

