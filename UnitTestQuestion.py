import unittest as ut
from database_question import QuestionTaskManagment, Task

class TestQuestionTaskManagment(ut.TestCase):
  def setUp(self):
    self.qtm = QuestionTaskManagment()
  
  def test_basesetup(self):
    self.assertEqual(self.qtm.BaseSetup(), 0)
  
  def test_newtask(self):
    task = Task()
    self.assertEqual(self.qtm.NewTask(task), 0)
  
  def test_getcorrect(self):
    pass

  def test_gettask(self):
    pass

if __name__ == "__main__":
  ut.main()