import sqlite3
import sys
import pathlib

def register(category,name,password,signal):
    con = sqlite3.connect('C:/Users/Dani/PycharmProjects/Mnemosyne/PassDB.db')
    cur = con.cursor()

    cur.execute(f"INSERT INTO data (category, name, password) VALUES ('{category}','{name}','{password}')")
    signal.emit('Пароль сохранен!')
    con.commit()


    cur.close()
    con.close()

