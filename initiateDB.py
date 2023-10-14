import sqlite3
def initiateDB(name):
    conn = sqlite3.connect(name)
    print("Connected to database successfully")

    conn.execute('CREATE TABLE users (username TEXT, adhar TEXT, walletID TEXT, password TEXT)')
    print("Created table successfully!")

    # conn.close() 
initiateDB("userData.db") # to create user database

