import sqlite3





conn = sqlite3.connect("jobs.db")
cur = conn.cursor()

#print("Hello , Den!")

def create():
    cur.execute("""CREATE TABLE IF NOT EXISTS Jobs (vacancy TEXT, link TEXT, company TEXT, money INT)""")


def passive_insert():
    cur.execute("INSERT INTO Jobs (vacancy, link, company, money) VALUES('title', 'href', 'compa', 'mon')")
    
    conn.commit()
    
    
def active_insert(vacancy, link, company, money):
    cur.execute("""INSERT INTO Jobs VALUES('%s', '%s', '%s', '%s')"""%(vacancy, link, company, money))
    conn.commit()
    



create()




def selector():
    cur.execute("SELECT vacancy, link, company, money FROM Jobs ")
    for temp in cur.fetchall():
        print(temp)

#selector()



#save changes


