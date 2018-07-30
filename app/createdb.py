import os

from psycopg2 import connect


def connect_to_db(config=None):
    if config == 'testing':
        db_name = os.getenv('TEST_DB')
    else:
        db_name = os.getenv('DB_NAME')

    host = os.getenv('DB_HOST')
    user = os.getenv('DB_USERNAME')
    password = os.getenv('DB_PASSWORD')

    return connect(
        database=db_name,
        host=host,
        user=user,
        password=password
    )


def create_users_table(cur):
    cur.execute(
        """CREATE TABLE users(
            id serial PRIMARY KEY,
            email VARCHAR NOT NULL UNIQUE,
            password VARCHAR NOT NULL);""")


def create_entries_table(cur):
    cur.execute(
        """CREATE TABLE entries(
            id serial,
            user_id INTEGER NOT NULL,
            title VARCHAR NOT NULL,
            entry VARCHAR NOT NULL,
            tag VARCHAR NOT NULL,
            created_at timestamp NOT NULL,
            last_modified timestamp NOT NULL,
            PRIMARY KEY (user_id , id),
            FOREIGN KEY (user_id) REFERENCES users (id));""")


def main(config=None):
    conn = connect_to_db(config=config)
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    cur.execute("""DROP TABLE IF EXISTS users CASCADE""")
    cur.execute("""DROP TABLE IF EXISTS entries CASCADE""")

    create_users_table(cur)
    create_entries_table(cur)

    cur.close()
    conn.commit()
    conn.close()
    print('Database created successfully')


if __name__ == '__main__':
    main()
