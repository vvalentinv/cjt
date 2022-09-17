import psycopg
import bcrypt
from dotenv import dotenv_values
from util.db_connection import pool
from util.helpers import hash_registering_password

from model.user import User


class UserDao:

    def get_user(self, email):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM users WHERE email = %s", (email,))

                user_row = cur.fetchone()
                if user_row:
                    user_id = user_row[0]
                    first_name = user_row[1]
                    last_name = user_row[2]
                    email = user_row[3]
                    passd = user_row[4]
                    phone = user_row[5]
                    role_name = user_row[6]
                    description = user_row[7]
                    photo_url = user_row[8]
                    return User(user_id, first_name, last_name, email, passd, phone, role_name, description, photo_url)
                else:
                    return None

    def add_user(self, user):
        bytes_p = user.password.encode('utf-8')
        h_pass = hash_registering_password(bytes_p)
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO users (first_name, last_name, email, pass, phone, role_name) "
                            "VALUES (%s, %s, %s, %s, %s, %s) RETURNING *", (user.first_name, user.last_name,
                                                                            user.email, h_pass, user.phone,
                                                                            user.role_name))
                inserted_user = cur.fetchone()
                if inserted_user:
                    return User(inserted_user[0], inserted_user[1], inserted_user[2], inserted_user[3],
                                inserted_user[4].decode(),
                                inserted_user[5], inserted_user[6], inserted_user[7], inserted_user[8])
                return None

    def update_user(self, user, email, first_name, last_name, password, phone):
        if email:
            email_db = email
        else:
            email_db = user.email
        if first_name:
            first_name_db = first_name
        else:
            first_name_db = user.first_name
        if last_name:
            last_name_db = last_name
        else:
            last_name_db = user.last_name
        if password:
            password_db = password
        else:
            password_db = user.password
        if phone:
            phone_db = phone
        else:
            phone_db = user.phone

        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("UPDATE users SET first_name = %s, last_name = %s, pass = %s, phone = %s, email = %s "
                            "WHERE id = %s RETURNING *", (first_name_db, last_name_db, password_db, phone_db,
                                                          email_db, user.user_id))
                user_row = cur.fetchone()
                if user_row is None:
                    return None
                else:
                    return User(user_row[0], user_row[1], user_row[2], user_row[3], user_row[4].decode(), user_row[5],
                                user_row[6], user_row[7], user_row[8])

    def get_user_by_id(self, user_id):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))

                user_row = cur.fetchone()
                if user_row:
                    user_id = user_row[0]
                    first_name = user_row[1]
                    last_name = user_row[2]
                    email = user_row[3]
                    passd = user_row[4].decode()
                    phone = user_row[5]
                    role_name = user_row[6]
                    description = user_row[7]
                    photo_url = user_row[8]

                    return User(user_id, first_name, last_name, email, passd, phone, role_name, description, photo_url)
                else:
                    return None
