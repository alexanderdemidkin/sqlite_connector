from db import SQLite_db
import datetime as dt

db1 = SQLite_db("test.sqlite3")

tst_table = f'test_table_{dt.datetime.now().strftime("%Y%m%d%H%M")}'
ren_table = f'test_rename_{dt.datetime.now().strftime("%Y%m%d%H%M")}'
tst_view = f'test_view_{dt.datetime.now().strftime("%Y%m%d%H%M")}'

print(tst_table)
print(tst_view)
print(ren_table)

def main_test():
    print('create table',db1.create_table(tst_table, {"id": "integer", "name": "text", "age": "integer", "city": "text"}))
    print('update table add',db1.update_table_add(tst_table, {"test_column_2": "text"}) )
    print('update table drop',db1.update_table_drop(tst_table, ["test_column_2"]) )
    print('insert data 1',db1.insert_data(tst_table, [1, "test_name", 22, "test_city"]) )
    print('insert data 2',db1.insert_data(tst_table, [2, "test_name_2", 23, "test_city_2"]) )
    print('insert data cols',db1.insert_data_cols(tst_table, ["id","age"], [41, 28]))
    print('update data',db1.update_data(tst_table, {"name": "test_name_234"}, "where id = 1"))
    print('select data',db1.select_data(tst_table, ["id", "name", "age", "city"], "where id = 1") )
    print('delete data',db1.delete_data(tst_table, "where id = 1"))
    print('show tables',db1.show_all_tables())
    print('create index',db1.create_index(tst_table, "id"))
    print('show indexes',db1.show_all_indexes(tst_table))
    print('drop index',db1.drop_index(tst_table, "id"))
    print('rename table',db1.rename_table(tst_table, ren_table))
    print('create query',db1.create_query(ren_table, ["id", "name", "age", "city"], "where id = 2"))
    print('create view', db1.create_view(tst_view, ren_table, ["id", "name", "age"], "where id = 2") )
    print('alter view', db1.alter_view(tst_view, ren_table, ["id", "name", "age", "city"], "where id = 2") )
    print('drop view', db1.drop_view(tst_view) )
    print('truncate table', db1.trunc_table(ren_table) )
    print('drop table', db1.drop_table(ren_table) )



main_test()