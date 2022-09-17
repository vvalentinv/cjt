from dotenv import dotenv_values
from psycopg_pool import ConnectionPool

config = dotenv_values(".env")

pool = ConnectionPool(
    'postgresql://' +
    config.get('db_user') + ':'
    + config.get('db_password') + '@' +
    config.get('host') + ':' +
    config.get('port') + '/' +
    config.get('db_name')
)
