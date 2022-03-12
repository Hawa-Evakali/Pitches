import unittest
from app.models import User
from app import db

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(username="paul", email="robbin.githimbo@student.moringaschool.com", password = 'Shizzle27!')

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)
        
    def test_no_access_password(self):
            with self.assertRaises(AttributeError):
                self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('Shizzle27!'))
        
    def save_account(self):
        db.session.add(self.new_user)
        db.session.commit()
        self.asserTrue(len(user.id) > 0)

