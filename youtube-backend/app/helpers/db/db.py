from pathlib import Path

import pandas as pd
import pymysql
import redshift_connector as rc
from flask import Flask


class MySQL:
    def __init__(self, app: Flask):
        self.app = app
        self.db = None

    def connect(self, read_only=True) -> None:
        """
        Opens connection with MySQL DB
        
        :return:
        """
        # ssl = None
        # if self.app.config['FLASK_ENV'] == constants.Env.PROD:
        #     """ SSL is needed for production """
        #     ssl = True


        if read_only:
            read_ssl = None
            if self.app.config['SECRETS']['MS_READ_CA']:
                base_dir = Path(__file__).parents[2]  # project folder
                ca_cert_file_path = str(
                    base_dir / 'config' / self.app.config['SECRETS']['MS_READ_CA'])
                self.app.logger.info(f"ca_cert_file_path: {ca_cert_file_path}")
                read_ssl = {'ca': ca_cert_file_path}
            self.db = pymysql.connect(
                host=self.app.config['SECRETS']['MS_READ_ONLY_HOST'],
                user=self.app.config['SECRETS']['MS_READ_ONLY_USER'],
                password=self.app.config['SECRETS']['MS_READ_ONLY_PASSWORD'],
                database=self.app.config['SECRETS']['MS_READ_ONLY_DB'],
                ssl=read_ssl
            )
        else:
            write_ssl = None
            if self.app.config['SECRETS']['MS_WRITE_CA']:
                base_dir = Path(__file__).parents[2]  # project folder
                ca_cert_file_path = str(
                    base_dir / 'config' / self.app.config['SECRETS']['MS_WRITE_CA'])
                self.app.logger.info(f"ca_cert_file_path: {ca_cert_file_path}")
                write_ssl = {'ca': ca_cert_file_path}

            self.db = pymysql.connect(
                host=self.app.config['SECRETS']['MS_WRITE_HOST'],
                user=self.app.config['SECRETS']['MS_WRITE_USER'],
                password=self.app.config['SECRETS']['MS_WRITE_PASSWORD'],
                database=self.app.config['SECRETS']['MS_WRITE_DB'],
                ssl=write_ssl
            )
        print(f"Opened the MySQL connection: DB - {self.app.config['SECRETS']['MS_WRITE_DB']})")

    def select(self, sql):
        cursor = self.db.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        results = cursor.fetchall()
        cursor.close()
        return results

    def insert(self, sql):
        cursor = self.db.cursor()
        cursor.execute(sql)
        self.db.commit()
        last_id = cursor.lastrowid
        cursor.close()
        return last_id

    def insert_many(self, sql, vals):
        cursor = self.db.cursor()
        response = cursor.executemany(sql, vals)
        self.db.commit()
        cursor.close()
        return response

    def execute_many(self, sql, vals):
        cursor = self.db.cursor()
        response = cursor.executemany(sql, vals)
        self.db.commit()
        cursor.close()
        return response

    def update(self, sql):
        cursor = self.db.cursor()
        response = cursor.execute(sql)
        self.db.commit()
        cursor.close()
        return response

    def delete(self, sql):
        cursor = self.db.cursor()
        response = cursor.execute(sql)
        self.db.commit()
        cursor.close()
        return response

    def close_connection(self):
        print(f"Closed the MySQL connection: DB - {self.app.config['SECRETS']['MS_WRITE_DB']})")
        self.db.close()


class Redshift:
    def __init__(self, app: Flask):
        self.app = app
        self.db = None
        self.type = type
        self.cursor = None
        self.connection = None

    def connect(self, read_only=True):
        """
        :parameter read_only: connection type

        :returns: the redshift connection or cursor
        """

        if read_only:
            self.connection = rc.connect(
                host=self.app.config['SECRETS']['REDSHIFT_HOST'],
                database=self.app.config['SECRETS']['REDSHIFT_DB'],
                user=self.app.config['SECRETS']['REDSHIFT_USER'],
                password=self.app.config['SECRETS']['REDSHIFT_PASSWORD'],
                port=int(self.app.config['SECRETS']['REDSHIFT_PORT']),
                ssl=bool(int(self.app.config['SECRETS']['REDSHIFT_SSL']))
            )
        else:
            self.connection = rc.connect(
                host=self.app.config['SECRETS']['REDSHIFT_WRITE_HOST'],
                database=self.app.config['SECRETS']['REDSHIFT_WRITE_DB'],
                user=self.app.config['SECRETS']['REDSHIFT_WRITE_USER'],
                password=self.app.config['SECRETS']['REDSHIFT_WRITE_PASSWORD'],
                port=int(self.app.config['SECRETS']['REDSHIFT_WRITE_PORT']),
                ssl=bool(int(self.app.config['SECRETS']['REDSHIFT_WRITE_SSL']))
            )

        self.connection.autocommit = True
        cursor: rc.Cursor = self.connection.cursor()
        self.cursor = cursor
        return cursor

    def execute(self, sql, params=None):
        """
        query: "select * from table where col = '%s' and col2 = '%s' "
        params: (x, y)
        """
        try:
            self.cursor.execute(sql, params)
        except Exception as e:
            print(f"e: {e}")
            if not self.connection.autocommit:
                self.cursor.execute("rollback")
            raise Exception(e)

    def get_df(self, sql):
        self.execute(sql, params=None)
        df: pd.DataFrame = self.cursor.fetch_dataframe()
        if isinstance(df, type(None)):
            return pd.DataFrame(
                columns=[desc[0].decode("utf-8") for desc in self.cursor.description])
        else:
            return df

    def close_connection(self):
        """ make sure to close the connection, after all the DB operation are over """
        print("Redshift DB connection closed successfully.")
        self.cursor.close()
