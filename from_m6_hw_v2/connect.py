import psycopg2
from contextlib import contextmanager


@contextmanager
def create_connection():
    try:
        """ create a database connection to database """
        conn = psycopg2.connect(host="localhost", database="hw6db", user="postgres", password="567432")  # database="postgres"
        yield conn
        conn.close()
    except psycopg2.OperationalError as err:
        raise RuntimeError(f"Failed to create database connection {err}")
