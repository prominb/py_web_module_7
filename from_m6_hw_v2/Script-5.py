import logging

from psycopg2 import DatabaseError

from connect import create_connection


def select_script(conn, sql_expression: str):
    """ Query SELECT script Знайти які курси читає певний викладач.
    :param conn: Connection object
    :param sql_expression:
    :return:
    """
    c = conn.cursor()
    try:
        c.execute(sql_expression)
        result = c.fetchall()
        for r in result:
            print(r)
    except DatabaseError as e:
        logging.error(e)
    finally:
        c.close()


def main():
    try:
        # читаємо файл зі скриптом
        with open('Script-5.sql', 'r', encoding="utf-8") as f:
            sql = f.read()

        # створюємо з'єднання з БД
        with create_connection() as conn:
            if conn is not None:
                select_script(conn, sql)
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)


if __name__ == '__main__':
    main()
