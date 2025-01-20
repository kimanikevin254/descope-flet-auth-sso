import flet as ft

from auth.auth_provider import OAuthProvider
from auth.auth_helpers import AuthManager
from views.main_view import MainView
from views.profile_view import ProfileView

class MyApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.title = "Demo Application"

        self.oauth_provider = OAuthProvider()
        self.auth_manager = AuthManager(oauth_provider=self.oauth_provider, page=page)
        

        self.page.on_route_change = self.route_handler
        self.page.on_view_pop = self.view_pop
        self.page.on_login = self.auth_manager.on_login
        self.page.on_logout = self.auth_manager.on_logout

    def route_handler(self, route):
        self.page.views.clear()

        if self.page.route == '/profile':
            if(self.page.auth is None):
                return self.page.go(route='/')
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