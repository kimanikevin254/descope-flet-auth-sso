import flet as ft

from auth.auth_helpers import AuthManager
from views.main_view import MainView
from views.profile_view import ProfileView

class MyApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.title = "Demo Application"

        self.auth_manager = AuthManager(page=self.page)

        self.page.on_route_change = self.route_handler
        self.page.on_view_pop = self.view_pop

    def route_handler(self, route):
        self.page.views.clear()

        if self.page.route == '/profile':
            view = ProfileView(self.page, self.auth_manager.handle_logout)
            self.page.views.append(view.get_view())
        else:
            view = MainView(self.auth_manager.handle_login)
            self.page.views.append(view.get_view())

        self.page.update()

    def view_pop(self):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)

    def run(self):
        self.page.go("/")

def main(page: ft.Page):
    app = MyApp(page)
    app.run()

ft.app(target=main)