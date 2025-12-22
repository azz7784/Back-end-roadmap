import unittest
from services.user_manager import Usermanager
from errors import ValidationError, BusinessError


class TestUserManager(unittest.TestCase):

    def test_create_user_success(self):
        manager = Usermanager()
        manager.add_user("ali", "ali@example.com")

        self.assertEqual(len(manager.users),1)
        self.assertEqual(manager.users[0].username, "ali")

    def test_create_user_without_username(self):
        manager = Usermanager()

        with self.assertRaises(ValidationError):
            manager.add_user("", "test@example.com")


    def test_duplicate_username(self):
        manager = Usermanager()
        manager.add_user("ali", "other@example.com")

        with self.assertRaises(BusinessError):
            manager.add_user("ali", "other@example.com")