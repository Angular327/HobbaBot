<<<<<<< HEAD
import psycopg2

def Connect():
    conn = psycopg2.connect(user = "vseqpqtvivijet",
                            password = "46c4637fc258f1ec804d0de7e8ee593509c3882122566072fd2bc2ce7016068e",
                            host = "ec2-174-129-33-13.compute-1.amazonaws.com",
                            port = "5432",
                            dbname = "da47qt2td3m9kl")
    cur = conn.cursor()  
    return conn, cur    

def ListW():
    conn, cur = Connect()
    cur.execute('SELECT * FROM workout ORDER BY id')
    rows = cur.fetchall()
    conn.close()
    s = "Workouts \n"
    for row in rows:
        s += '#' + str(row[0]) + ": " + str(row[2]) + "\n"
    return s

def PrintW(id):
    try:
        int(id)
    except ValueError:
        return "Pick a valid number"
    conn, cur = Connect()
    cur.execute('SELECT * from workout WHERE id = \'' + str(id) + '\'')
    row = cur.fetchall()
    conn.close()
    if(len(row) == 0):
        return "Pick a valid number"
    row = row[0]
    s = row[2] + ':\n'
    s += row[3] + "\n by" + row[1]
=======
import psycopg2

def Connect():
    conn = psycopg2.connect(user = "vseqpqtvivijet",
                            password = "46c4637fc258f1ec804d0de7e8ee593509c3882122566072fd2bc2ce7016068e",
                            host = "ec2-174-129-33-13.compute-1.amazonaws.com",
                            port = "5432",
                            dbname = "da47qt2td3m9kl")
    cur = conn.cursor()  
    return conn, cur    

def ListW():
    conn, cur = Connect()
    cur.execute('SELECT * FROM workout ORDER BY id')
    rows = cur.fetchall()
    conn.close()
    s = "Workouts \n"
    for row in rows:
        s += '#' + str(row[0]) + ": " + str(row[2]) + "\n"
    return s

def PrintW(id):
    try:
        int(id)
    except ValueError:
        return "Pick a valid number"
    conn, cur = Connect()
    cur.execute('SELECT * from workout WHERE id = \'' + str(id) + '\'')
    row = cur.fetchall()
    conn.close()
    if(len(row) == 0):
        return "Pick a valid number"
    row = row[0]
    s = row[2] + ':\n'
    s += row[3] + "\n by" + row[1]
>>>>>>> 9a021e80eb8d8dd12a37a0d1e625e01deafe039b
    return s