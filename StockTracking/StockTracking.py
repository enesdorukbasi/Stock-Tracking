import sys
import Managers.CategoryManager
import Managers.ProductManager
import Managers.SalesManager


MainMenu = """
STOCK TRACKİNG

(1)Category Transactions
(2)Product Transactions
(3)Sales Transactions
(4)Exit
Please Select a Transaction...
"""
CategoryMenu = """
You Selected Category Actions
(1)List
(2)Add
(3)Delete
(4)Update
"""
ProductMenu = """
You Selected Product Transactions
(1)List
(2)Add
(3)Delete
(4)Update
"""
SalesMenu = """
You Selected Sales Transactions
(1)List
(2)Add
(3)Delete
"""

while True:
    print(MainMenu)
    process = int(input(""))
    if process == 1:
        print(CategoryMenu)
        CatProcess = int(input(""))
        if CatProcess == 1:
            Managers.CategoryManager.toList()
        elif CatProcess == 2:
            name = input("Enter the name of the category to be added : ")
            Managers.CategoryManager.Add(name)
        elif CatProcess == 3:
            name = input("Enter the name of the category to be remove : ")
            Managers.CategoryManager.Delete(name)
        elif CatProcess == 4:
            Id = input("Enter the id of the category to be update : ")
            Name = input("Enter the current category name : ")
            Managers.CategoryManager.Update(Id,Name)
    elif process == 2:
        print(ProductMenu)
        ProProcess = int(input(""))
        if ProProcess == 1:
            Managers.ProductManager.toList()
        elif ProProcess == 2:
            name = input("Enter the name of the product to be added:")
            number = int(input("Enter the quantity of the product to be added:"))
            price = float(input("Enter the price of the product to be added:"))
            category = int(input("Enter the category of the product to be added:"))
            Managers.ProductManager.Add(name,number,price,category)
        elif ProProcess == 3:
            name = input("Enter the name of the product you want to delete:")
            Managers.ProductManager.Delete(name)
        elif ProProcess == 4:
            Id = input("Enter the id of the product you want to update:")
            Name = input("Enter the current product name:")
            Number = int(input("Enter the quantity of the current product:"))
            Price = float(input("Enter the price of the current product:"))
            Category = int(input("Enter the category of the current product:"))
            Managers.ProductManager.Update(Id,Name,Number,Price,Category)
    elif process == 3:
        print(SalesMenu)
        SalesProcess = int(input(""))
        if SalesProcess == 1:
            Managers.SalesManager.toList()
        elif SalesProcess == 2:
            productId = int(input("Enter the product to be added:"))
            number = int(input("How many of the product will be added:"))
            price = float(input("Enter the price of the product:"))
            Managers.SalesManager.Add(productId,number,price)
        elif SalesProcess == 3:
            Id = int(input("Enter the id of the sale you want to delete:"))
            Managers.SalesManager.Delete(Id)
    elif process == 4:
        print("Bye Bye...")
        sys.exit()