import unittest
from Password_test.Password_Checker2 import check_password_strength


class TestPasswordStrengthChecker(unittest.TestCase):

    def test_empty_password(self):
        self.assertEqual(check_password_strength(""), "Password cannot be empty!")

    def test_too_short(self):
        self.assertEqual(check_password_strength("123"), "Weak (password id too short)")

    def test_only_lowercase(self):
        result = check_password_strength("abcdef")
        self.assertIn("Weak", result)
        self.assertIn("Your password is missing", result)

    def test_only_uppercase(self):
        result = check_password_strength("ABCDEF")
        self.assertIn("Weak", result)
        self.assertIn("Your password is missing", result)

    def test_only_digits(self):
        result = check_password_strength("1234567890")
        self.assertIn("Weak", result)
        self.assertIn("Your password is missing", result)

    def test_moderate_password(self):
        result = check_password_strength("abcABC123")
        self.assertIn("Moderate", result)

    def test_strong_password(self):
        result = check_password_strength("abcABC123!")
        self.assertIn("Strong", result)

    def test_special_chars_missing(self):
        result = check_password_strength("abcABC123")
        self.assertIn("Your password is missing", result)

    def test_max_strength(self):
        result = check_password_strength("aB1@aB1@aB1@")
        self.assertIn("Strong", result)
        self.assertIn("Score: 100", result)

    def test_just_enough(self):
        result = check_password_strength("aB1@abc")
        self.assertIn("Strong", result)


if __name__ == '__main__':
    unittest.main()