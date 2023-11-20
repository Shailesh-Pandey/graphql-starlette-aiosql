
import sqlite3

conn = sqlite3.connect("Users.db")
cursor = conn.cursor()

# create a table
cursor.execute("""CREATE TABLE Users
                 (id TEXT, name TEXT, email TEXT)
               """)


# save data
conn.commit()


users = [('1', 'Mike','mike@mike.com'
          ),
         ('2','Shailesh','shailesh@shailesh.com'
          ),
         ('3','example', 'example@example.com'
		 )]
cursor.executemany("INSERT INTO Users VALUES (?,?,?)", users)
conn.commit()