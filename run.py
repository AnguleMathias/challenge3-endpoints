import os
from app.app import app
from instance.config import *


app.config.from_object(app_config[os.getenv('APP_SETTINGS')])

if __name__ == '__main__':
    app.run()
