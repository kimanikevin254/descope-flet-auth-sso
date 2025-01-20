from flet.auth import OAuthProvider as BaseOAuthProvider
from config import Config

class OAuthProvider(BaseOAuthProvider):
    def __init__(self):
        super().__init__(
            client_id=Config.OAUTH_CLIENT_ID,
            client_secret=Config.OAUTH_CLIENT_SECRET,
            authorization_endpoint=Config.OAUTH_AUTHORIZATION_ENDPOINT,
            token_endpoint=Config.OAUTH_TOKEN_ENDPOINT,
            user_endpoint=Config.OAUTH_USER_ENDPOINT,
            redirect_url=Config.OAUTH_REDIRECT_URI,
            user_id_fn=lambda u: u[Config.OAUTH_USER_ID_FIELD],
        )