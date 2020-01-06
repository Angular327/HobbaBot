import psycopg2
import datetime

days = ['mon', 'tue', 'wed', 'thur', 'fri', 'sat', 'sun']
week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
def Connect():
    conn = psycopg2.connect(user = "bubdvuhlxohtqm",
                            password = "197e19be6026819279bc05c41961cda4c65910b6aa5f682af79e257c8f5ac422",
                            host = "ec2-174-129-33-181.compute-1.amazonaws.com",
                            port = "5432",
                            dbname = "d984gl6lnk8s7m")
    cur = conn.cursor()  
    return conn, cur    

def update(id, day):
    conn, cur = Connect()
    s = 'UPDATE users SET '
    for x in days:
        s += x + ' = \'' + str(x in day) + '\'' + ', '
        s += 'c' + x + ' = \'t\', '
    if(',' in s):
        s = s[:-2]
    s += ' WHERE id = \'' + str(id) + '\''
    cur.execute(s)
    conn.commit()
    conn.close()

def insert(username, id, day):
    conn, cur = Connect()
    s = 'INSERT INTO users (id, username) Values (\'' + str(id) + '\', \'' + str(username) + '\')'
    cur.execute(s)
    conn.commit()
    conn.close()
    
def Add(id, check, day):
    conn, cur = Connect()
    s = 'UPDATE users SET '
    for x in days:
        if(x in day):
            s += x + ' = \'' + str(check) + '\'' + ', '
    if(',' in s):
        s = s[:-2]
    s += ' WHERE id = \'' + str(id) + '\''
    cur.execute(s)
    conn.commit()
    conn.close()

def Get(id):
    conn, cur = Connect()
    cur.execute('SELECT * from users WHERE id = \'' + str(id) + '\'')
    rows = cur.fetchall()
    conn.close()
    return rows

def setID(username, id, arr):
    print(id)
    if(len(Get(id)) == 0):
        insert(username, id, arr)
    update(id, arr)

def CheckIn(id, check, day):
    conn, cur = Connect()
    s = 'UPDATE users SET '
    for x in days:
        if(x in day):
            s += 'c' + x + ' = \'' + str(not check) + '\'' + ', '
    if(',' in s):
        s = s[:-2]
    s += ' WHERE id = \'' + str(id) + '\''
    cur.execute(s)
    conn.commit()
    conn.close()

def NewDay(day = 'cmon ctue cwed cthur cfri csat csun', t = True):
    conn, cur = Connect()
    s = 'UPDATE users SET '
    for x in days:
        if(x in day):
            s += 'c' + x + ' = \'' + str(t) + '\'' + ', '
    if(',' in s):
        s = s[:-2]
    cur.execute(s)
    conn.commit()
    conn.close()

def printH(row):
    s = "User: " + str(row[1]) + "\n"
    for x in range(7):
        s += week[x] + ': '
        if(row[x+9]):
            if(row[x + 2]):
                if(x <= datetime.datetime.today().weekday()): 
                    s += "Missed"
                else:
                    s += "To Do"
            else:
                s += "Off Day"
        else:
            s += 'Excersised'
        s += "\n"
    s += '\n'
    return s

def printID(id):
    conn, cur = Connect()
    cur.execute('SELECT * FROM users WHERE id = \'' + str(id) + '\'')
    rows = cur.fetchall()
    conn.close()
    if(len(rows) == 0):
        return "No Days Set Yet! \nUse !Set <days> to set days"
    row = rows[0]
    return '```' + printH(row) + '```'


def printall():
    conn, cur = Connect()
    cur.execute('SELECT * FROM users ORDER BY id')
    rows = cur.fetchall()
    conn.close()
    s = ""
    for row in rows:
        s += printH(row)
    return s
        
def DayGetter(id, b = True):
    conn, cur = Connect()
    cur.execute('SELECT * FROM users WHERE id = \'' + id + '\'')
    rows = cur.fetchall()
    conn.close()
    row = rows[0]
    s = ''
    if(b):
        for x in range(len(days)):
            if(row[x + 2]):
                s += week[x] + ' '
    else:
        for x in range(len(days)):
            if(not row[x + 9]):
                s += week[x] + ' '

    return s

def Delete(id):
    conn, cur = Connect()
    s = 'DELETE FROM users WHERE id = \'' + str(id) + '\''
    cur.execute(s)
    conn.commit()
    conn.close()
