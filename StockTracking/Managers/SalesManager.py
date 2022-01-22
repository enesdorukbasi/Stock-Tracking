import DB.Database

def toList():
    cur = DB.Database.con.cursor()
    cur.execute("SELECT * FROM tblSales")
    rows = cur.fetchall()
    row = rows[0]
    if row[1] != "":
        for r in rows:
            print(f"id {r[0]}, productId {r[1]}, number {r[2]}, price {r[3]}")
    else:
        print("List is empty.")

def Add(productId,number,price):
    cur = DB.Database.con.cursor()
    cur.execute(
        "INSERT INTO tblSales(ProductId,Number,Price) VALUES ({},{},{});".format(productId, number, price * number))
    DB.Database.con.commit()

def Delete(Id):
    if Id != "":
        cur = DB.Database.con.cursor()
        cur.execute("DELETE FROM tblSales WHERE Id = {};".format(Id))
        DB.Database.con.commit()
    else:
        print("The Id field cannot be empty.")
