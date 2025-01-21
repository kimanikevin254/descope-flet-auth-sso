from flet import Page

class AuthManager:
    def __init__(self, page: Page):
        self.page = page

    def handle_login(self, e):
        self.page.go('/profile')

    def handle_logout(self, e):
        self.page.go('/')