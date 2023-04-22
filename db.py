import sqlite3


class SQLite_db:

    def __init__(self, db_name: str):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()

    def close(self):
        self.conn.close()

    def create_table(self,table_name: str, table_columns: dict):
        """
        create a table in sqlite database 
        parameters:
            table_name string,

            table_columns dict
            table_columns example:
            {
                "column_name": "data_type",
                "column_name": "data_type",
            }
        return boolean
        """
        cols = ''
        for key,val in table_columns.items():
            cols += f"{key} {val},"
        self.cur.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({cols[:-1]})")
        self.conn.commit()
        return True
    
    def create_index(self,table_name: str, column_name: str):
        """
        create a index in table in sqlite database 
        parameters:
            table_name string,
            column_name string
        return boolean
        """
        self.cur.execute(f"CREATE INDEX IF NOT EXISTS {table_name}_{column_name} ON {table_name}({column_name})")
        self.conn.commit()
        return True
    
    def drop_index(self,table_name: str, index_name: str):
        """
        drop a index in table in sqlite database 
        parameters:
            table_name string,
            index_name string
        return boolean
        """
        self.cur.execute(f"DROP INDEX IF EXISTS {table_name}_{index_name}")
        self.conn.commit()
      
        return True
    
    def drop_table(self,table_name: str):
        """
        drop a table in sqlite database 
        parameters:
            table_name string

        return boolean
        """
        self.cur.execute(f"DROP TABLE IF EXISTS {table_name}")
        self.conn.commit()
      
        return True
    
    def update_table_add(self,table_name: str, table_columns: dict):
        """
        update a table in sqlite database 
        parameters:
            table_name string,
            table_columns dict
            table_columns example:
            {
                "column_name": "data_type",
                "column_name": "data_type",
            }
        return boolean
        """
        cols = ''
        for key,val in table_columns.items():
            cols = f"{key} {val},"
            self.cur.execute(f"ALTER TABLE {table_name} add {cols[:-1]}")
        self.conn.commit()
      
        return True
    
    def update_table_drop(self,table_name: str, table_columns: list):
        for col in table_columns:
            self.cur.execute(f"ALTER TABLE {table_name} drop {col}")
        self.conn.commit()
      
        return True
    
    def rename_table(self,table_name: str, new_name: str):
        self.cur.execute(f"ALTER TABLE {table_name} RENAME TO {new_name}")
        self.conn.commit()
      
        return True
    
    def rename_column(self,table_name: str, old_name: str, new_name: str):
        self.cur.execute(f"ALTER TABLE {table_name} RENAME {old_name} TO {new_name}")
        self.conn.commit()
      
        return True
    
    def show_all_tables(self):
        self.cur.execute("SELECT name FROM sqlite_schema WHERE type ='table' AND name NOT LIKE 'sqlite_%';")
        result = self.cur.fetchall()
      
        return result
    
    def show_all_columns(self,table_name: str):
        self.cur.execute(f"PRAGMA table_info({table_name})")
        result = self.cur.fetchall()
      
        return result
    
    def show_all_indexes(self,table_name: str):
        self.cur.execute(f"PRAGMA index_list({table_name})")
        result = self.cur.fetchall()
      
        return result
    
    def insert_data(self,table_name: str, data: list):
        vals = ''
        for val in data:
            vals += f"'{val}',"
        self.cur.execute(f"INSERT INTO {table_name} VALUES ({vals[:-1]})")
        self.conn.commit()
      
        return True
    
    def insert_data_cols(self, table_name: str, cols: list, values: list):
        col = ''
        vals = ''
        for cl in cols:
            col += f"{cl},"
        for val in values:
            vals += f"{val},"
        self.cur.execute(f"INSERT INTO {table_name} ({col[:-1]}) VALUES ({vals[:-1]})") 
        self.conn.commit()
      
        return True  

    def update_data(self,table_name: str, data: dict, where: str):
        for key,val in data.items():
           self.cur.execute(f"UPDATE {table_name} SET {key}='{val}'  {where}")
        self.conn.commit()
      
        return True    
    
    def delete_data(self,table_name: str, where: str):
        self.cur.execute(f"DELETE FROM {table_name} {where}")
        self.conn.commit()
      
        return True

    def select_data(self,table_name: str, columns: list,where: str):
        cols = ''
        for col in columns:
            cols += f"{col},"
        result = self.cur.execute(f"SELECT {cols[:-1]} FROM {table_name} {where}").fetchall()
      
        return result

    def create_query(self,table_name: str, columns: list,where: str):
        cols = ''
        for col in columns:
            cols += f"{col},"
        result = f"SELECT {cols[:-1]} FROM {table_name} {where}"
      
        return result
    
    def create_view(self,view_name: str,table_name: str,  columns: list,where: str):
        cols = ''
        for col in columns:
            cols += f"{col},"
        self.cur.execute(f"CREATE VIEW {view_name} AS SELECT {cols[:-1]} FROM {table_name} {where}")
        self.conn.commit()
      
        return True
    
    def show_view(self,view_name: str):
        result = self.cur.execute(f"SELECT * FROM {view_name}").fetchall()
      
        return result
    
    def alter_view(self,view_name: str,table_name: str, columns: list,where: str):
        self.cur.execute(f"DROP VIEW IF EXISTS {view_name}")
        self.conn.commit()
        self.create_view( view_name,table_name, columns,where)

        return True
    
    
    def drop_view(self,table_name: str):
        self.cur.execute(f"DROP VIEW IF EXISTS {table_name}")
        self.conn.commit()
      
        return True

    def trunc_table(self, table_name: str):
        self.cur.execute(f"delete from {table_name}")
        self.conn.commit()
      
        return True