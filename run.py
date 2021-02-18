import os

from app import crud_app

config_name = os.getenv('APP_SETTINGS')
app = crud_app(config_name)

if __name__ == '__main__':
    app.run()