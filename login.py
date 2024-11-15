from database_question import QuestionTaskManagment
import database_question
import database
from database import TaskManagment
qtm=QuestionTaskManagment()
qtm.BaseSetup()
a=TaskManagment()
a.BaseSetup()
b=database.UserRegistration
b.username="Ivan"
b.telegram="@babizon14"
b.email="babizon14@pon.ru"
b.age=993
a.NewUser(b)
b=database.UserRegistration
b.username="Biba"
b.telegram="@biba"
b.email="babizon14@pon.ru"
b.age=52
a.NewUser(b)
b=database.UserRegistration
b.username="Boba"
b.telegram="@boba"
b.email="boba@pon.ru"
b.age=69
a.NewUser(b)
b=database_question.Task
b.subject="math"
b.chapter="geometry"
b.question="sin 90 deg"
b.answer="1"
qtm.NewTask(b)
b.subject="math"
b.chapter="geometry"
b.question="cos 90 deg"
b.answer="0"
qtm.NewTask(b)
b.subject="math"
b.chapter="algebra"
b.question="1+1"
b.answer="2"
qtm.NewTask(b)
b.subject="math"
b.chapter="algebra"
b.question="x+2=0; x=?"
b.answer="-2"
qtm.NewTask(b)
b.subject="physics"
b.chapter="mechanics"
b.question="V*t=?"
b.answer="S"
qtm.NewTask(b)
b.subject="physics"
b.chapter="mechanics"
b.question="w*r=?"
b.answer="v"
qtm.NewTask(b)
b.subject="physics"
b.chapter="electricity"
b.question="I*R=?"
b.answer="U"
qtm.NewTask(b)
b.subject="physics"
b.chapter="electricity"
b.question="C*U=?"
b.answer="q"
qtm.NewTask(b)