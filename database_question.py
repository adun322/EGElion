import sqlite3
import json
import logging
from utils import json_to_dict_list
from database import TaskManagment as tm
from pydantic import BaseModel, EmailStr


class Task(BaseModel):
    subject: str
    chapter: str
    question: str
    answer: str

    def model_post_init(self, *args, **kwargs):
        pass


class QuestionTaskManagment():
    def __init__(self):
        pass

    def BaseSetup(self):
        connection = sqlite3.connect("userbase.db", check_same_thread=False)
        cursor = connection.cursor()
        cursor.execute("DROP TABLE IF EXISTS Tasks")
        connection.commit()
        cursor.execute('''
        CREATE TABLE Tasks (
        id INTEGER PRIMARY KEY,
        subject TEXT NOT NULL,
        chapter TEXT NOT NULL,
        question TEXT NOT NULL,
        answer TEXT NOT NULL
        )
        ''')
        connection.commit()
        connection.close()
        return 0

    def NewTask(self, task: Task):
        connection = sqlite3.connect("userbase.db", check_same_thread=False)
        cursor = connection.cursor()
        cursor.execute('INSERT INTO Tasks (subject, chapter, question,answer) VALUES (?, ?, ?, ?)',
                    (task.subject, task.chapter, task.question, task.answer))
        connection.commit()
        connection.close()
        return 0

    def GetCorrect(self,id_task: int):
        connection = sqlite3.connect("userbase.db", check_same_thread=False)
        cursor = connection.cursor()
        cursor.execute('Select answer from Tasks Where id = ?',
                    (id_task,))
        ans = cursor.fetchall()
        connection.commit()
        connection.close()
        return ans[0]


    def GetTask(self,id_task: int):
        connection = sqlite3.connect("userbase.db", check_same_thread=False)
        cursor = connection.cursor()
        cursor.execute('Select subject, chapter, question, answer from Tasks Where id = ?',
                    (id_task,))
        ans = cursor.fetchall()
        connection.commit()
        connection.close()
        return {"subject": ans[0][0], "chapter": ans[0][1], "question": ans[0][2], "answer": ans[0][3]}

    def GetChapter(self,chapter: str, id_user: int):
        connection = sqlite3.connect("userbase.db", check_same_thread=False)
        cursor = connection.cursor()
        cursor.execute('Select id,subject, chapter, question from Tasks Where chapter = ?',
                       (chapter,))
        ans = cursor.fetchall()
        connection.commit()
        connection.close()
        res = []
        for i in ans:
            a = tm()
            res.append(list(i) + [a.GetComplete(id_user, i[0])])
        return list(map(lambda x: {"id": x[0], "subject": x[1],"chapter":x[2],"question":x[3], "accept": x[4]}, res))

    def GetSubject(self,subject: str, id_user: int):
        connection = sqlite3.connect("userbase.db", check_same_thread=False)
        cursor = connection.cursor()
        cursor.execute('Select chapter from Tasks Where subject = ?',
                       (subject,))
        ans = cursor.fetchall()
        connection.commit()
        connection.close()
        res = []
        d = {}
        d2 = {}
        qtm=QuestionTaskManagment()
        for i in ans:
            res += (qtm.GetChapter(i[0], id_user))
        for i in res:
            if list(d.keys()).count(i["chapter"]) == 0:
                d[i["chapter"]] = 1
                d2[i["chapter"]] = 0
            else:
                d[i["chapter"]] += 1
            if i["accept"]:
                d2[i["chapter"]] += 1
        for i in d.keys():
            d2[i] = d2[i] / d[i]
        return d2

    def GetCourse(self,id_user: int):
        qtm = QuestionTaskManagment()
        connection = sqlite3.connect("userbase.db", check_same_thread=False)
        cursor = connection.cursor()
        cursor.execute('Select subject from Tasks')
        ans = cursor.fetchall()
        connection.commit()
        connection.close()
        res = []
        d3 = {}
        for i in ans:
            res.append(i[0])
        for i in set(res):
            k = qtm.GetSubject(i, id_user)
            sm = 0
            for j in k.keys():
                sm += k[j]
            sm /= len(k.keys())
            d3[i] = sm
        return d3