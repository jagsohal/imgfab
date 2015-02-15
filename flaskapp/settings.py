import os

SOCIAL_AUTH_FACEBOOK_KEY = os.getenv("SOCIAL_AUTH_FACEBOOK_KEY")
SOCIAL_AUTH_FACEBOOK_SECRET = os.getenv("SOCIAL_AUTH_FACEBOOK_SECRET")

SOCIAL_AUTH_FACEBOOK_SCOPE = ['public_profile', 'email', 'user_photos']
SOCIAL_AUTH_STORAGE = 'social.apps.flask_app.me.models.FlaskStorage'
SOCIAL_AUTH_USER_MODEL = 'flaskapp.models.User'
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True
SOCIAL_AUTH_AUTHENTICATION_BACKENDS = (
  'social.backends.facebook.FacebookOAuth2',
)

MONGODB_SETTINGS = {
  "host": os.getenv("MONGOLAB_URI"),
  "DB": "imgfab_psa"
}

SESSION_COOKIE_NAME = "imgfab_session"
SECRET_KEY = os.getenv("IMGFAB_SESSION_KEY") or "change-me"
SOCIAL_AUTH_LOGIN_REDIRECT_URL = "/"
SOCIAL_AUTH_LOGIN_ERROR_URL = "/login-error"