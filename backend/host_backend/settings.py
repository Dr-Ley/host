from pathlib import Path
from mongoengine import connect  # pyright: ignore[reportMissingImports]
from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# ------------------------------
# ENVIRONMENT VARIABLES
# ------------------------------

# SECRET KEY — MUST NEVER be hardcoded in production
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

# DEBUG — off in production
DEBUG = os.environ.get("DEBUG", "False").lower() == "true"

# Allowed hosts (Render will inject this)
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(",")

# MongoDB URI (stored in Render)
MONGO_URI = os.environ.get("MONGO_URI")

# Connect to MongoDB using mongoengine
connect(
    db="tripnestDB",
    host=MONGO_URI,
)


# ------------------------------
# Django Apps
# ------------------------------

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
    "api",
]


# ------------------------------
# Middleware
# ------------------------------

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware"
]

CORS_ALLOW_ALL_ORIGINS = True


ROOT_URLCONF = "host_backend.urls"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "host_backend.wsgi.application"


# ------------------------------
# Dummy Database (using MongoEngine instead)
# ------------------------------

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.dummy"
    }
}


# ------------------------------
# Static Files
# ------------------------------

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"  # needed for Render deployment


# ------------------------------
# Default Auto Field
# ------------------------------

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
