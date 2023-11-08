from django.db import connections, connection

# Define your database settings
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "mydatabase.db",
    }
}


# Function to establish a database connection
def setup_database():
    connection.settings_dict = DATABASES["default"]
    connections.ensure_defaults("default")
    connection.close()
    connection.connect()
