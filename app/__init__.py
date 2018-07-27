from flask import Flask
from flask_restful import Api

import config
import psycopg2
import psycopg2.extras


def connectToDB():
    connectionString = 'dbname=diary user=postgres password=1 host=localhost'
    print(connectionString)
    try:
        return psycopg2.connect(connectionString)
    except:
        print("Cant connect to database")

    conn = connectToDB()
    cur = conn.cursor()
    try:
        cur.execute("select title, description from entries")
    except:
        print("Error")
        results = cur.fetchall()
        return results


def create_app(config_name):
    app = Flask(__name__)
    api = Api(app)

    app.config.from_object(config.app_config[config_name])
    app.url_map.strict_slashes = False

    from app.resources.user_resource import SignupResource, LoginResource
    from app.resources.entry_resource import EntryResource

    api.add_resource(SignupResource, '/api/v1/user/signup')
    api.add_resource(LoginResource, '/api/v1/user/login')
    api.add_resource(EntryResource, '/api/v1/user/entries', '/api/v1/user/entries/<int:entry_id>')

    return app
