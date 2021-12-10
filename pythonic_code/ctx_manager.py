# Context managers in action

def stop_database():
    print("stop postgres")

def start_database():
    print("start postgres")


class DBHandler:
    def __enter__(self): # this method is executed before running the body of the context manager
        stop_database()
        return self
    def __exit__(self, exc_type, ex_value, ex_traceback): # this method is executed after running the body of the context manager
        start_database()
def db_backup():
    print("pg_dump database")

def main():
    with DBHandler(): # __enter__ method executes here
        db_backup()
    # __exit__ method executes here

main()
