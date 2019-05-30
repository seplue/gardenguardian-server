import psycopg2


class Connection(object):

    def __init__(self, database_address, database_user, database_password, database_name):
        self.database_address = database_address
        self.database_user = database_user
        self.database_password = database_password
        self.database_name = database_name


    def open_connection(self):

        conn = psycopg2.connect('host={} user={} password={} dbname={}'
                                .format(self.database_address, self.database_user, self.database_password, self.database_name))
        cursor = conn.cursor()

        query = "INSERT INTO measurements(measurementtime, measurementtype, measurementvalue, bedname, gardenname) " \
                "VALUES (%s, %s, %s, %s, %s)"

        cursor.execute(query, values)
        conn.commit()

    def close_connection(self):

        conn.close()
        cursor.close()
