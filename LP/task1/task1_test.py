import unittest

class TestBookManager(unittest.TestCase):
    def test_add_book(self):
        book_manager = BookManager()
        book_manager.add_book("1984 by George Orwell")
        self.assertEqual(book_manager.books, ["1984 by George Orwell"])

    def test_show_books(self):
        book_manager = BookManager()
        book_manager.add_book("1984 by George Orwell")
        self.assertEqual(book_manager.show_books(), ["1984 by George Orwell"])

class TestUserManager(unittest.TestCase):
    def test_add_user(self):
        user_manager = UserManager()
        user_manager.add_user("John Doe")
        self.assertEqual(user_manager.users, ["John Doe"])

    def test_show_users(self):
        user_manager = UserManager()
        user_manager.add_user("John Doe")
        self.assertEqual(user_manager.show_users(), ["John Doe"])

class TestLoanManager(unittest.TestCase):
    def test_loan_book(self):
        loan_manager = LoanManager()
        loan_manager.loan_book("1984 by George Orwell", "John Doe")
        self.assertEqual(loan_manager.loans, [("1984 by George Orwell", "John Doe")])

    def test_show_loans(self):
        loan_manager = LoanManager()
        loan_manager.loan_book("1984 by George Orwell", "John Doe")
        self.assertEqual(loan_manager.show_loans(), [("1984 by George Orwell", "John Doe")])

if __name__ == '__main__':
    unittest.main()
