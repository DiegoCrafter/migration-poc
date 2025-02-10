from google.cloud.sql.connector import Connector
from app.constants import Constants
from sqlalchemy import text
import io
import polars as pl

class Utils:
    def __init__(self):
        """
        Constructor
        """

    def get_connection(self):
        connector = Connector()
        conn = connector.connect(
            Constants.INSTANCE_CONNECTION_NAME,
            "pg8000",
            user=Constants.DB_USER,
            password=Constants.DB_PASSWORD,
            db=Constants.DB_NAME
        )
        return conn
    
    def get_value_as_list(self, dictionary, key):
        if key in dictionary:
            value = dictionary[key]
            return value if isinstance(value, list) else [value]
        return []
    
    def insert_csv_to_db(self, file, table_name, column_names, engine, batch_size=1000):
        df = pl.read_csv(io.StringIO(file.decode("utf-8")), has_header=False, new_columns=column_names)
        data = df.to_numpy().tolist()
        columns = ", ".join(column_names)
        placeholders = ", ".join([f":{col}" for col in column_names])
        insert_stmt = text(f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})")
        with engine.connect() as db_conn:
            with db_conn.begin():
                for i in range(0, len(data), batch_size):
                    batch = data[i:i + batch_size]
                    db_conn.execute(
                        insert_stmt,
                        [{col: row[idx] for idx, col in enumerate(column_names)} for row in batch]
                    )
        return data