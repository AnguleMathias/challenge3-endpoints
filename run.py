from app.app import app
from instance.config import *


app.config.from_object(app_config[os.getenv('APP_SETTINGS')])

app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

if __name__ == '__main__':
    app.run()
