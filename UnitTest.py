import unittest as ut
from database import TaskManagment


class TestTaskManagment(ut.TestCase):
    def setUp(self):
        self.tm = TaskManagment()

    def test_basesetup(self):
        self.assertEqual(self.tm.BaseSetup(), 0)

    def test_approvetask(self):
        self.assertEqual(self.tm.ApproveTask(0, 0), 0)
    
    def test_newuser(self):
        self.assertEqual(self.tm.NewUser(name="ваня", email="pon@pon.pon", age=993), 0)
    
    def test_userfromid(self):
        self.tm.BaseSetup()
        self.tm.NewUser(name="ваня", email="pon@pon.pon", age=993)
        self.assertEqual(self.tm.UserFromId(1), ("ваня", "pon@pon.pon", 993))
    
    def test_getcomplete_false(self):
        self.tm.BaseSetup()
        self.assertEqual(self.tm.GetComplete(0, 0), False)
    
    def test_getcomplete_true(self):
        self.tm.NewUser(name="ваня", email="pon@pon.pon", age=993)
        self.assertEqual(self.tm.GetComplete(0, 0), True)


if __name__ == "__main__":
    ut.main()
