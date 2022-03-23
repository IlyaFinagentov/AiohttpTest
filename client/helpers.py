import psycopg2


def exception_decorator(method):
    def wrap():
        try:
            method()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    return wrap
