from flask_bcrypt import Bcrypt
import os
from datetime import timedelta
from flask import Flask, jsonify, request
import psycopg2
from flask_jwt_extended import (
    JWTManager, create_access_token)

app = Flask(__name__, instance_relative_config=True)

jwt = JWTManager(app)

bcrypt = Bcrypt(app)


class Database:
    def __init__(self):
        dbname = os.getenv('DB_NAME')
        user = os.getenv('DB_USER')
        password = os.getenv('DB_PASSWORD')
        host = os.getenv('DB_HOST')
        port = os.getenv('DB_PORT')
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            host=host,
            password=password,
            port=port)
        self.cursor = self.conn.cursor()

    def create_table_user(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                                id serial PRIMARY KEY,
                                username VARCHAR NOT NULL,
                                email VARCHAR NOT NULL UNIQUE,
                                password VARCHAR NOT NULL);
                                """)
        self.cursor.close()
        self.conn.commit()
        self.conn.close()

    def create_table_entry(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS entries(
                                id serial,
                                user_id INTEGER NOT NULL,
                                title VARCHAR NOT NULL,
                                entry VARCHAR NOT NULL,
                                created_at timestamp,
                                last_modified timestamp,
                                PRIMARY KEY (user_id , id),
                                FOREIGN KEY (user_id) REFERENCES users (id));
                                """)

        self.cursor.close()
        self.conn.commit()
        self.conn.close()

    def drop_table_entry(self):
        self.cursor.execute("""DROP TABLE IF EXISTS entries""")
        self.cursor.close()
        self.conn.commit()
        self.conn.close()

    def drop_table_user(self):
        self.cursor.execute("""DROP TABLE IF EXISTS users cascade""")
        self.cursor.close()
        self.conn.commit()
        self.conn.close()

    def signup(self, user_data):
        user = request.get_json()
        username = (user['username'])
        self.cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        username_data = self.cursor.fetchall()
        if not username_data:
            self.cursor.execute("""INSERT INTO users (username, password, email)
                                VALUES (%(username)s, %(password)s, %(email)s)""", user_data)
            self.conn.commit()
            return jsonify({'message': 'User created successfully'}), 201
        self.cursor.close()
        self.conn.close()
        return jsonify({'message': 'Username already exists'}), 400

    def login(self, username, password):
        self.cursor.execute("""SELECT password, username FROM users WHERE username = (%s)""",
                            (username,))
        data = self.cursor.fetchone()
        if data:
            if not data[1] == username:
                return jsonify({'message': 'User is invalid'}), 400
            if bcrypt.check_password_hash(data[0], password):
                expiration = timedelta(minutes=30)
                access_token = create_access_token(identity=username, expires_delta=expiration)
                return jsonify({'token': access_token, 'message': 'Login successful'}), 200
            else:
                return jsonify({'message': 'Password is invalid'}), 400
        self.cursor.close()
        self.conn.close()
        return jsonify({'message': 'Username is invalid'}), 400

    def add_entry(self, entry_data):
        self.cursor.execute("""INSERT INTO entries (user_id, title, entry)
                            VALUES (%(user_id)s,%(title)s, %(entry)s)""", entry_data)
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
        return jsonify({'message': 'Entry successfully created'}), 200

    def get_one_entry(self, entry_id):
        self.cursor.execute("""SELECT * FROM entries WHERE entry_id = %s""", (entry_id,))
        data = self.cursor.fetchall()
        if data:
            return jsonify({'Entry': data, 'message': 'Entry successfully found'}), 200
        self.cursor.close()
        self.conn.close()
        return jsonify({'message': 'Entry not found'})

    def get_all_entries(self):
        self.cursor.execute("""SELECT * FROM entries""")
        data = self.cursor.fetchall()
        if data:
            return jsonify({'Entries': data, 'message': 'All entries found successfully'})
        self.cursor.close()
        self.conn.close()
        return jsonify({'message': 'No entries found'})

    def update_entry(self, entry_id, entry_data):
        self.cursor.execute("""SELECT * FROM entries WHERE entry_id = %s""", (entry_id,))
        data = self.cursor.fetchall()
        if data:
            self.cursor.execute("""UPDATE entries set entry_title=%(title)s,
                                entry=%(entry)s """, entry_data)
            self.conn.commit()
            self.cursor.execute("""SELECT * FROM entries WHERE entry_id = %s""", (entry_id,))
            updated_data = self.cursor.fetchall()
            return jsonify({'Entry': updated_data, 'message': 'Entry successfully updated'}), 200
        self.cursor.close()
        self.conn.close()
        return jsonify({'message': 'Entry not found'})

    def delete_entry(self, entry_id):
        self.cursor.execute("""SELECT * FROM entries WHERE entry_id = %s""", (entry_id,))
        data = self.cursor.fetchall()
        if data:
            self.cursor.execute("""DELETE FROM entries WHERE entry_id = %s""", (entry_id,))
            self.conn.commit()
            return jsonify({'message': 'Entry successfully deleted'}), 204
        self.cursor.close()
        self.conn.close()
        return jsonify({'message': 'Entry not found.'}), 400

#
# if __name__ == "__main__":
#     db = Database()
#     db.create_table_entry()
#     db.create_table_user()
