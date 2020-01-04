import psycopg2
import datetime

days = ['mon', 'tue', 'wed', 'thur', 'fri', 'sat', 'sun']
week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
def Connect():
    conn = psycopg2.connect(user = "postgres",
                            password = "miles1",
                            host = "localhost",
                            port = "5433",
                            dbname = "discord")
    cur = conn.cursor()  
    return conn, cur    

def update(id, day):
    conn, cur = Connect()
    s = 'UPDATE users SET '
    for x in days:
        s += x + ' = \'' + str(x in day) + '\'' + ', '
        s += 'c' + x + ' = \'' + str(not x in day) + '\'' + ', '
    s = s[:-2]
    s += ' WHERE id = \'' + str(id) + '\''
    cur.execute(s)
    conn.commit()
    conn.close()

def insert(id, day):
    conn, cur = Connect()
    s = 'INSERT INTO users Values(id ' + str(id) + ')'
    cur.execute(s)
    conn.commit()
    conn.close()

def get(id):
    conn, cur = Connect()
    cur.execute('SELECT * from users WHERE id = \'' + str(id) + '\'')
    rows = cur.fetchall()
    conn.close()
    return rows

def setID(id, arr):
    if(len(get(id)) == 0):
        insert(id, arr)
    update(id, arr)

def add(id, arr):
    conn, cur = Connect()
    arr = arr.split(' ')
    s = 'UPDATE users SET '
    for x in arr:
        s += x + ' = \'t\'' + ', '
        s += 'c' + x + ' = \'t\'' + ', '
    s = s[:-2]
    s += ' WHERE id = \'' + str(id) + '\''
    cur.execute(s)
    conn.commit()
    conn.close()

def remove(id, arr):
    conn, cur = Connect()
    arr = arr.split(' ')
    s = 'UPDATE users SET '
    for x in arr:
        s += x + ' = \'f\'' + ', '
        s += 'c' + x + ' = \'f\'' + ', '
    s = s[:-2]
    s += ' WHERE id = \'' + str(id) + '\''
    cur.execute(s)
    conn.commit()
    conn.close()

def CheckIn(id, day = days[datetime.datetime.today().weekday()]):
    remove(id, [day])

def printH(row):
    s = "ID = " + str(row[0]) + "\n"
    for x in range(1,8):
        s+= week[x] + ' = ' + str(row[1]) + "\n"
    s += '\n'
    return s

def printID(id):
    if(len(get(id)) == 0):
        return "No Days Set Yet! \nUse !set <days> to set days"
    conn, cur = Connect()
    cur.execute('SELECT * FROM users WHERE id = \'' + id + '\'')
    rows = cur.fetchall()
    conn.close()
    row = rows[0]
    return printH(row)


def printall():
    conn, cur = Connect()
    cur.execute('SELECT * FROM users ORDER BY id')
    rows = cur.fetchall()
    conn.close()
    for row in rows:
        printH(row)
        
def DayGetter(id):
    if(len(get(id)) == 0):
        return "No Days Set Yet! \nUse !Set <days> to set days"
    conn, cur = Connect()
    cur.execute('SELECT * FROM users WHERE id = \'' + id + '\'')
    rows = cur.fetchall()
    conn.close()
    row = rows[0]
    s = ''
    for x in range(len(days)):
        if(row[x + 1]):
            s += week[x] + ' '
    return s

def Delete(id):
    conn, cur = Connect()
    s = 'DELETE FROM users WHERE id = \'' + str(id) + '\''
    cur.execute(s)
    conn.commit()
    conn.close()
