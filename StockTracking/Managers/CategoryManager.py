import DB.Database

def toList():
    cur = DB.Database.con.cursor()
    cur.execute("SELECT * FROM tblCategory")
    rows = cur.fetchall()
    for r in rows:
        print(f"id {r[0]} name {r[1]}")

def Add(name):
    cur = DB.Database.con.cursor()
    cur.execute("INSERT INTO tblCategory(Name) VALUES ('{}');".format(name))
    DB.Database.con.commit()

def Delete(name):
    cur = DB.Database.con.cursor()
    cur.execute("DELETE FROM tblCategory WHERE Name = '{}';".format(name))
    DB.Database.con.commit()

def Update(Id,Name):
    if Id != "":
        cur = DB.Database.con.cursor()
        cur.execute("UPDATE tblCategory SET Name = '{}' WHERE Id = {};".format(Name, Id))
        DB.Database.con.commit()
    else:
        print("The Id field cannot be empty.")