import sqlite3 as sq
import getpass
import os
import sys
def open_account(name):
  def openn():
    conn = sq.connect(name)
    cur = conn.cursor()
    #cur.execute("DROP TABLE IF EXISTS ACCOUNTS")
    cur.execute('''CREATE TABLE ACCOUNTS
              (ID INTEGER PRIMARY KEY AUTOINCREMENT,
	      FIRST_NAME NOT NULL,
	     LAST_NAME NOT NULL,
             USER TEXT NOT NULL,
	     PASSWORD TEXT NOT NULL);''')

    conn.close()
  def openn2():
    conn = sq.connect(name)
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS ACCOUNTS")
    cur.execute('''CREATE TABLE ACCOUNTS
              (ID INTEGER PRIMARY KEY AUTOINCREMENT,
              FIRST_NAME NOT NULL,
             LAST_NAME NOT NULL,
             USER TEXT NOT NULL,
             PASSWORD TEXT NOT NULL);''')

    conn.close() 
  try:
     openn()
  except:
    print 'Data_base already exists, want to override?'
    command = raw_input('y/n?  :')
    if command == 'y':
        key = getpass.getpass('key:  ')
	if key == '00000':
	    openn2()
        else:
            sys.exit('Key did not match')
    else:
       sys.exit('thank you')

def insert(name):
    print ('----------** Inputs Are Case Sensitive **---------------------------')
    print ('')
    first_name = raw_input('First_name:  ')
    last_name = raw_input('Last_name:  ')
    user = raw_input('user_name:  ')
    password = getpass.getpass('password:  ')
    n_p = getpass.getpass('Retype password:  ')
    assert password == n_p,'Retyped password did not match, please re-run'
    conn = sq.connect(name)
    cur = conn.cursor()
    params = (first_name,last_name,user,password)
    cur.execute("INSERT INTO ACCOUNTS VALUES(NULL,?,?,?,?)",params)
    conn.commit()
    conn.close()

def display(name):
    print ('----------** Inputs Are Case Sensitive **---------------------------')
    print ('')
    key = getpass.getpass('Administrative key:   ')

    if key == '00000':
       pass
    else:
        sys.exit('Key did not match')
    conn = sq.connect(name)
    cur = conn.cursor()
    rows = cur.execute("SELECT ID,FIRST_NAME,LAST_NAME,USER,PASSWORD from ACCOUNTS")
    for row in rows:
       print 'ID: ',row[0]
       print 'FIRST NAME',row[1]
       print 'LAST NAME',row[2]
       print 'USER: ',row[3]
       print 'PASSWORD: ',row[4], '\n'     
def extract(name):
    conn = sq.connect(name)
    cur = conn.cursor()
    rows = cur.execute("SELECT ID,FIRST_NAME,LAST_NAME,USER,PASSWORD from ACCOUNTS")
    pas = []
    lists = []
    for row in rows:
        lists.append((row[0],row[1],row[2],row[3],row[4]))
    #for row in rows:
    #    pas.append(row[4])
    conn.commit()
    conn.close()
    return lists 

def update(name):
   print ('----------** Inputs Are Case Sensitive **---------------------------')
   print ('')
   last_name = raw_input('Last_name:  ')
   lists = extract(name)
   #print lists[1][2]
   mask = []
   for i in range(len(lists)):
       if last_name == lists[i][2]:
           old_pass = raw_input('Old Password: ')
           assert old_pass in lists[i],'Sorry, old password could be located. Please re-run'
           n_user = raw_input('New user_name: ')
           n_pass = getpass.getpass('New password:  ')
           r_pass = getpass.getpass('Retype password:  ')
           assert n_pass == r_pass,'Retyped password did not match, please run again'
           conn = sq.connect(name)
           cur = conn.cursor()
           params = (n_user,n_pass,last_name)
           cur.execute("UPDATE ACCOUNTS set USER = ?, PASSWORD = ? where LAST_NAME = ?",params)
           conn.commit()
           conn.close()
           print 'Update Done !'
	   mask.append(1)
	   break
       else:
           pass
   if len(mask) == 0:
           print 'User could not be located. Please run again'
   else:
           pass
           #print 'User could not be located. Please run again'
	   #sys.exit()
def delete(name):
    print ('----------** Inputs Are Case Sensitive **---------------------------')
    print ('')
    last_name = raw_input('Last_name:  ')
    lists = extract(name)
    mask = []
    for i in range(len(lists)):
        if last_name == lists[i][2]:
	    old_p = raw_input('password:  ')
	    assert old_p == lists[i][4],'Password did not match to the last name'
	    conn = sq.connect(name)
	    cur = conn.cursor()
	    params = (lists[i][2],)
            cur.execute("DELETE from ACCOUNTS where LAST_NAME = ?",params)
	    conn.commit()
	    conn.close()
	    mask.append(1)
	    print ('{} {} user has been removed'.format(lists[i][1],lists[i][2]))
	    break
	else:
	    pass
    if len(mask) != 0:
        pass 
    else:
        print ('Users could not be located')
