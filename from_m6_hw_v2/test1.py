import logging

from psycopg2 import DatabaseError

from connect import create_connection

""" create a database connection to database """
# conn = psycopg2.connect(host="localhost", database="mytest", user="postgres", password="567432")
if __name__ == '__main__':
    sql_expression_01 = """
        SELECT * FROM test_table;
        """
    
    sql_expression_02 = """
        SELECT * FROM test_table;
        """


    try:
        with create_connection() as conn:
            if conn is not None:
                c = conn.cursor()
                try:
                    c.execute(sql_expression_01)
                    print(c.fetchone())
                    c.execute(sql_expression_02)
                    result = c.fetchall()
                    # result = c.fetchone()
                    print(result)
                    # print(result)
                except DatabaseError as e:
                    logging.error(e)
                finally:
                    c.close()
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)
