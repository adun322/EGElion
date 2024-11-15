import sqlite3
import json
import logging
from utils import json_to_dict_list
from pydantic import BaseModel, EmailStr


class UserRegistration(BaseModel):
    username: str
    email: EmailStr
    telegram: str
    age: int


class TaskManagment():
    def __init__(self):
        pass

    def BaseSetup(self):
        connection = sqlite3.connect("userbase.db", check_same_thread=False)
        cursor = connection.cursor()

        cursor.execute("DROP TABLE IF EXISTS Users")

        cursor.execute('''
        CREATE TABLE Users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        telegram TEST NOT NULL,
        email TEXT NOT NULL,
        age INTEGER,
        task1 INTEGER,
        task2 INTEGER,
        task3 INTEGER,
        task4 INTEGER,
        task5 INTEGER,
        task6 INTEGER,
        task7 INTEGER,
        task8 INTEGER,
        task9 INTEGER,
        task10 INTEGER
        )
        ''')
        connection.commit()
        connection.close()
        return 0

    def NewUser(self, user: UserRegistration):
        connection = sqlite3.connect("userbase.db", check_same_thread=False)
        cursor = connection.cursor()
        cursor.execute('INSERT INTO Users (username, telegram, email, age) VALUES (?, ?, ?, ?)', (user.username, user.telegram, user.email, user.age))
        connection.commit()
        connection.close()
        logging.info("users created")
        return 0

    def UserFromId(self, id: int):
        connection = sqlite3.connect("userbase.db", check_same_thread=False)
        cursor = connection.cursor()
        cursor.execute('''SELECT username, telegram, email, age FROM Users WHERE id = ?''', (id,))
        result = cursor.fetchall()
        connection.commit()
        connection.close()
        logging.info("пользователь найден")
        result = result[0]
        return {"name": result[0], "email": result[2],"telegram": result[1], "age": result[3]}

    def ApproveTask(self, UserId: int, TaskId: int):
        connection = sqlite3.connect("userbase.db", check_same_thread=False)
        cursor = connection.cursor()
        cursor.execute(f"Update Users SET task{TaskId} = 1 WHERE id = ?", (UserId,))
        connection.commit()
        connection.close()
        return 0

    def GetComplete(self, UserId: int, TaskId: int):
        connection = sqlite3.connect("userbase.db", check_same_thread=False)
        cursor = connection.cursor()
        cursor.execute(f"Select username From Users WHERE id = ? And task{TaskId} = 1", (UserId,))
        result = cursor.fetchall()
        connection.commit()
        connection.close()
        return len(result) > 0
