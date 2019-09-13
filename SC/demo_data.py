import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')

curs = conn.cursor()

create_demo_table = '''
CREATE TABLE demo (
    s CHAR(3),
    x INT,
    y INT
);
'''

curs.execute(create_demo_table)

entries = [("'g'", 3, 9), ("'v'", 5, 7), ("'f'", 8, 7)]

# inserting entries to demo table
for entry in entries:
    insert_entry = '''
    INSERT INTO demo
    (s, x, y)
    VALUES (''' + str(entry[0])+','+str(entry[1])+','+str(entry[2]) + ');'
    curs.execute(insert_entry)

curs.close()
conn.commit()

# Counting number of rows in demo
curs = conn.cursor()
curs.execute('SELECT COUNT(*) FROM demo;').fetchall()

# Counting number of rows in demo where x and y are >5
count_greater = '''
SELECT COUNT(*) FROM demo WHERE x >= 5 AND y>=5;
'''
curs.execute(count_greater).fetchall()

# Counting distinct values of y

curs.execute('SELECT COUNT(DISTINCT y) FROM demo').fetchall()
