
# For reading data and creating a database of English-Turkish words

import sqlite3 as sq
import csv

# initialize dictionary for Turkish - English words
turkEng_dict = {}
# open the csv file unti the 'with' ends
with open('turkish_english_2000.csv',encoding='utf8') as csv_file:
    # read the csv file
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    # go through each row of the csv file
    for row in csv_reader:
        # first line has nothing, skip
        if line_count == 0:
            line_count+=1
            pass
        # use the id to add the words to the dictionary, increment line count
        else:
            turkEng_dict[line_count] = [row[1],row[2],'PRACTICE']
            line_count+=1


# open the sqlite file, create it if it doesn't exist
conn = sq.connect('turk_eng_db.sqlite')
# define the cursor
cursor = conn.cursor()

# creates a table named TURK_ENG with column titles ID, TURKISH, ENGLISH, and CATEGORY
cursor.execute('''CREATE TABLE TURK_ENG
         (ID INT PRIMARY KEY     NOT NULL,
         TURKISH           TEXT    NOT NULL,
         ENGLISH           TEXT     NOT NULL,
         CATEGORY          TEXT     NOT NULL);''')

# for each entry in the Turkish - English dictionary
for entries in range(1,len(turkEng_dict)):
    cur_ID = str(entries)
    cur_eng = str(turkEng_dict[entries][0])
    cur_turk = str(turkEng_dict[entries][1])
    cur_catg = str(turkEng_dict[entries][2])

    # uses values from the variables to input them into the database
    cursor.execute("INSERT INTO TURK_ENG (ID,TURKISH,ENGLISH,CATEGORY) VALUES (?, ?, ?, ?)",
          (cur_ID, cur_eng, cur_turk, cur_catg))
    
# save the changes and close the database
conn.commit()
conn.close()