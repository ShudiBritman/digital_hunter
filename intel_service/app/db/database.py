import mysql.connector
import os
import logging




class DataBase:
    def __init__(self):
        self.host = os.getenv("MYSQL_HOST")
        self.port = int(os.getenv("MYSQL_PORT"))
        self.user = os.getenv("MYSQL_USER")
        self.password = os.getenv("MYSQL_PASSWORD")
        self.database = os.getenv("MYSQL_DB")

    def get_connection(self):
        return mysql.connector.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database
        )
    

    def init_db(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        query = '''CREATE TABLE IF NOT EXIST targets(
            entity_id VARCHAR(100) PRIMARY KEY,
            reported_lat FLOAT NOT NULL,
            reported_lon FLOAT NOT NULL,
            priority_level INT NOT NULL,
            status VARCHAR(50) DEFAULT 'active');

            CREATE TABLE IF NOT EXIST signals(
            timestamp DATETIME,
            signal_id INT PRIMARY KEY,
            signal_type VARCHAR(50)
            )
        '''
        cursor.execute(query)


        
