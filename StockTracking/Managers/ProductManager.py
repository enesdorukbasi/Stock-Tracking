import DB.Database

def toList():
    cur = DB.Database.con.cursor()
    cur.execute("SELECT * FROM tblProduct")
    rows = cur.fetchall()
    row = rows[0]
    if row[1] != "":
        for r in rows:
            print(f"id {r[0]}, name {r[1]}, number {r[2]}, price {r[3]}, category {r[4]}")
    else:
        print("List is empty.")

def Add(name,number,price,category):
    cur = DB.Database.con.cursor()
    cur.execute("INSERT INTO tblProduct(Name,Number,Price,CategoryId) VALUES ('{}',{},{},{});".format(name, number, price,category))
    DB.Database.con.commit()

def Delete(name):
    cur = DB.Database.con.cursor()
    cur.execute("DELETE FROM tblProduct WHERE Name = '{}';".format(name))
    DB.Database.con.commit()

def Update(Id,Name,Number,Price,CategoryId):
    if Id != "":
        cur = DB.Database.con.cursor()
        cur.execute("UPDATE tblProduct SET Name = '{}',Number = '{}',Price = '{}',CategoryId = '{}' WHERE Id = {};".format(Name,Number,Price,CategoryId,Id))
        DB.Database.con.commit()
    else:
        print("The Id field cannot be empty.")