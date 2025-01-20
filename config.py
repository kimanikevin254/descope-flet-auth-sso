from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    @staticmethod
    def get_env_var(name, default=None, required=True):
        value = os.getenv(name, default)
        if required and value is None:
            raise ValueError(f"Environment variable '{name}' is required but not set.")
        return value

    OAUTH_CLIENT_ID = get_env_var('OAUTH_CLIENT_ID')
    OAUTH_CLIENT_SECRET = get_env_var('OAUTH_CLIENT_SECRET')
    OAUTH_AUTHORIZATION_ENDPOINT = get_env_var('OAUTH_AUTHORIZATION_ENDPOINT')
    OAUTH_TOKEN_ENDPOINT = get_env_var('OAUTH_TOKEN_ENDPOINT')
    OAUTH_USER_ENDPOINT = get_env_var('OAUTH_USER_ENDPOINT')
    OAUTH_REDIRECT_URI = get_env_var('OAUTH_REDIRECT_URI')
    OAUTH_USER_ID_FIELD = get_env_var('OAUTH_USER_ID_FIELD')
    OAUTH_TOKEN_SECRET = get_env_var('OAUTH_TOKEN_SECRET')
    OAUTH_TOKEN_KEY = get_env_var('OAUTH_TOKEN_KEY')