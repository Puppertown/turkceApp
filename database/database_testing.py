# database testing 

import sqlite3 as sq

# open the sqlite file
conn = sq.connect(r'C:\Users\CrunchyTiger\Desktop\kivy\Türkçe_Tavşanı\turkceApp\database\turk_eng_db.sqlite')

# define the cursor
cursor = conn.cursor()

# define some variable
test_int = 1

# select the value
cursor.execute("SELECT ENGLISH FROM TURK_ENG WHERE ID = ?",(test_int,))

# assign the found value 
for column in cursor:
    selection = column[0]

print(selection)





