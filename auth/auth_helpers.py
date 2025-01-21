from flet import Page, LoginEvent
from flet.security import encrypt, decrypt
from config import Config

class AuthManager:
    def __init__(self, page: Page):
        self.page = page

    def on_login(self, e: LoginEvent):
        if e.error:
            raise Exception(e.error)
        
        # Save token in client storage
        token = self.page.auth.token.to_json()
        encrypted_token = encrypt(token, Config.OAUTH_TOKEN_SECRET)
        self.page.client_storage.set(Config.OAUTH_TOKEN_KEY, encrypted_token)
        
        self.page.go('/profile')

    def on_logout(self, e):
        self.page.go('/')

    def handle_login(self, e):
        saved_token = None

        # Retrieve token from client storage
        encrypted_token = self.page.client_storage.get(Config.OAUTH_TOKEN_KEY)

        # Decrypt retrieved token
        if encrypted_token:
            saved_token = decrypt(encrypted_data=encrypted_token, secret_key=Config.OAUTH_TOKEN_SECRET)

        # Log in the user
        if e is not None or saved_token is not None:
            self.page.login(provider=self.page.oauth_provider, saved_token=saved_token, scope=Config.OAUTH_SCOPES.split())

    def handle_logout(self, e):
        self.page.client_storage.remove(Config.OAUTH_TOKEN_KEY)
        self.page.logout()