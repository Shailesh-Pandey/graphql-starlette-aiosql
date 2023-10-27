
import sqlite3

conn = sqlite3.connect("User.db")
cursor = conn.cursor()

# create a table
#cursor.execute("""CREATE TABLE User
#                 (id TEXT, name TEXT, email TEXT)
#               """)


# save data
conn.commit()


users = [('1', 'Mike','mike@mike.com'
          ),
         ('2','Shailesh','shailesh@shailesh.com'
          ),
         ('3','example', 'example@example.com'
		 )]
cursor.executemany("INSERT INTO User VALUES (?,?,?)", users)
conn.commit()