from fastapi import FastAPI
from database import TaskManagment
from database_question import Task
import database_question
from database_question import QuestionTaskManagment
import database
from pydantic import BaseModel
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO, filename="bd_log.log", filemode='w')
logging.info("msg")
logging.debug("mss")

tm = TaskManagment()
qtm = QuestionTaskManagment()


class Answer(BaseModel):
    user_id: int
    answer: int


@app.get("/")
def HomePage():
    return {"message": "pr"}


@app.post("/register")
def register(user: database.UserRegistration):
    return tm.NewUser(user)


@app.get("/user/{id_user}")
def get_user(id_user: int):
    return tm.UserFromId(id_user)


@app.post("/new_task")
def post_task(task: Task):
    qtm.NewTask(task)


@app.get("/tasks/{id_task}")
def get_task(id_task: int):
    return qtm.GetTask(id_task)


@app.get("/tasks/chapter/{chapter,id_user}")
def get_chapter(chapter: str, id_user: int):
    return qtm.GetChapter(chapter, id_user)


@app.post("/tasks/load_answer")
def post_answer(id_task: int, id_user: int, answer: str):
    if qtm.GetCorrect(id_task)[0] == answer:
        tm.ApproveTask(id_user, id_task)
        return 0
    else:
        return 1


@app.get("/tasks/subject/{subject,id_user}")
def get_sub(subject: str, id_user: int):
    return qtm.GetSubject(subject, id_user)


@app.get("/tasks/course/{id_user}")
def get_course(id_user: int):
    return qtm.GetCourse(id_user)
