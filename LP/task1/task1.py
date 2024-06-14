"""
Проблема в поточній реалізації класу Library полягає в тому, що він не дотримується принципу
 єдиного обов'язку (Single Responsibility Principle) SOLID. Клас відповідає як за управління
  книгами, так і за управління користувачами та кредитами, що призводить до
  змішання різних аспектів функціональності.

Це може вплинути на майбутню розширюваність та підтримку коду, оскільки будь-які зміни
у логіці книг, користувачів чи кредитів потенційно можуть впливати на інші частини програми,
 які використовують цей клас.

Для поліпшення цієї ситуації можливо розглянути розділення класу Library на окремі класи або модулі,
 що відповідають за управління книгами, користувачами та кредитами. Таким чином, кожен клас буде
  відповідати за один конкретний аспект системи, що спростить його розширення та зміну в майбутньому.
"""


class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.loans = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added book: {book}")

    def add_user(self, user):
        self.users.append(user)
        print(f"Added user: {user}")

    def loan_book(self, book, user):
        self.loans.append((book, user))
        print(f"Loaned book: {book} to user: {user}")

    def show_books(self):
        print(f"Books: {self.books}")

    def show_users(self):
        print(f"Users: {self.users}")

    def show_loans(self):
        print(f"Loans: {self.loans}")


library = Library()
library.add_book("1984 by George Orwell")
library.add_user("John Doe")
library.loan_book("1984 by George Orwell", "John Doe")
library.show_books()
library.show_users()
library.show_loans()
