import sqlite3
import pandas as pd


class SqliteDB:

    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            return self
        except Exception as e:
            raise RuntimeError(f"Failed to open database {self.db_name}") from e

    def __exit__(self, exc_type, exc_value, traceback):
        
        try:
            self.conn.close()
        except Exception as close_err:
            print(f"Error: failed to close database connection: {close_err}")
        
        return False

    def write_single_record(self, table, record): #record: {'department_id': 7, 'department_name': 'TEST'}
        # INSERT INTO department (department_id, department_name) VALUES (?,?)
        columns = ", ".join(record.keys())
        placeholders = ", ".join(['?' for _ in record])
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        with self.conn:
            self.conn.execute(query, tuple(record.values()))

    def write_multiple_records(self, table, df):
        if df.empty:
            return
        df.to_sql(table, self.conn, if_exists="append", index=False)

    def select_records(self, query): #fetchone(), fetchall()
        df = pd.read_sql_query(query, self.conn)
        return df
    
    def delete_records(self, table, where_clause):
        query = f"DELETE FROM {table} WHERE {where_clause}"
        with self.conn:
            self.conn.execute(query)

    def update_records(self, table, updates, where_clause):
        # {"department_name": "Updated record"}
        update_clause = ", ".join([f"{k} = ?" for k in updates.keys()])
        query = f"UPDATE {table} SET {update_clause} WHERE {where_clause}"
        values = tuple(updates.values())

        with self.conn:
            self.conn.execute(query, values)


with SqliteDB("lessons/lesson_15/department-db") as db:
    #db.write_single_record('department', {'department_id': 8, 'department_name': 'TEST'})

    #df = pd.DataFrame([{'department_id': 9, 'department_name': 'TEST9'},
    #                   {'department_id': 10, 'department_name': 'TEST10'}])
    
    #db.write_multiple_records("department", df)

    result_df = db.select_records("SELECT * FROM department")
    print(result_df)

    #db.delete_records("department", "department_id=10")
    db.update_records("department", {"department_name": "Updated_record"}, "department_id=9")
    
