import requests
import json

#import db

headers= {
 "Accept": "*/*",
 "User-Agent": "Test API requests",
 "Content-Type": "application/json" 
}

apis = {
    "create_table" :  {"method" : "POST", "url" : "http://127.0.0.1:8000/api/db/table/create",
                       "data" : {"name" : "test_table11",  "columns": {"id": "integer","name": "text","age": "integer","city": "text"}}},
    "update_table_add":{"method" : "POST", "url" : "http://127.0.0.1:8000/api/db/table/alter_add",
                        "data" : {"name" : "test_table11",  "columns": {"test_column_2": "text"}}},
    "update_table_drop":{"method" : "POST", "url" : "http://127.0.0.1:8000/api/db/table/alter_drop",
                        "data" : {"name" : "test_table11",  "columns": ["test_column_2"]}},
    "insert_data" : {"method" : "POST", "url" : "http://127.0.0.1:8000/api/db/data/insert",
                        "data" : {"name" : "test_table11",  "columns": [1,"test_name",20,"test_city"]}},
    "insert_data_cols":{"method" : "POST", "url" : "http://127.0.0.1:8000/api/db/data/insert_cols",
                        "data" : {"name" : "test_table11",  "cols": ["id","age"], "vals":[12,43]}},
    "update_data":{"method" : "POST", "url" : "http://127.0.0.1:8000/api/db/data/update",
                        "data" : {"name" : "test_table11",  "cols": {"name": "tesf"}, "where":"where id=12"}},
    "select_data":{"method" : "GET", "url" : "http://127.0.0.1:8000/api/db/data/select",
                        "data" : {"name" : "test_table11",  "cols": ["id","age"], "where":"where id=12"}},
    "delete_data":{"method" : "POST", "url" : "http://127.0.0.1:8000/api/db/data/delete",
                        "data" : {"name" : "test_table11", "where":"where id=1"}},
    "show_tables":{"method" : "GET", "url" : "http://127.0.0.1:8000/api/db/table/show_all",
                        "data" : {"name" : "test_table11"}},
    "create_index": {"method" : "POST", "url" : "http://127.0.0.1:8000/api/db/table/create_index",
                        "data" : {"table" : "test_table11",  "index": "id"}},
    "show_index": {"method" : "GET", "url" : "http://127.0.0.1:8000/api/db/table/show_indexes",
                        "data" : {"name" : "test_table11"}},
    "drop_index": {"method" : "POST", "url" : "http://127.0.0.1:8000/api/db/table/drop_index",
                        "data" : {"table" : "test_table11",  "index": "id"}},
    "rename_table": {"method" : "POST", "url" : "http://127.0.0.1:8000/api/db/table/rename",
                        "data": {"old" : "test_table11", "new": "test_table12"}},
    "create_query": {"method" : "GET", "url" : "http://127.0.0.1:8000/api/db/data/create_query",
                        "data": {"name" : "test_table12", "cols": ["id","age"], "where":"where id=12"}},
    "show_columns": {"method" : "GET", "url" : "http://127.0.0.1:8000/api/db/table/show_columns",
                        "data": {"name" : "test_table12"}},
    "create_view": {"method" : "POST", "url" : "http://127.0.0.1:8000/api/db/view/create",
                        "data": {"name" : "test_view", "table": "test_table12", "cols": ["id","age"], "where":"where id=12"}},
    "alter_view": {"method" : "POST", "url" : "http://127.0.0.1:8000/api/db/view/alter",
                        "data": {"name" : "test_view", "table": "test_table12", "cols": ["id","name","city"], "where":"where id=12"}},
    "truncate_table": {"method" : "POST", "url" : "http://127.0.0.1:8000/api/db/table/truncate",
                        "data": {"name" : "test_table12"}},
    "drop_table": {"method" : "POST", "url" : "http://127.0.0.1:8000/api/db/table/drop",
                        "data": {"name" : "test_table12"}},
        
}


for api in apis:
    resp = requests.request(method=apis[api]["method"], url=apis[api]["url"],data=json.dumps(apis[api]["data"]))
    print(resp.text)




#resp = requests.request(method=apis["create_table"]["method"], url=apis["create_table"]["url"],data=json.dumps(apis["create_table"]["data"]))
#resp = requests.request(method=apis["update_table_add"]["method"], url=apis["update_table_add"]["url"],data=json.dumps(apis["update_table_add"]["data"]))
#resp = requests.request(method=apis["update_table_drop"]["method"], url=apis["update_table_drop"]["url"],data=json.dumps(apis["update_table_drop"]["data"]))
#resp = requests.request(method=apis["insert_data"]["method"], url=apis["insert_data"]["url"],data=json.dumps(apis["insert_data"]["data"]))
#resp = requests.request(method=apis["insert_data_cols"]["method"], url=apis["insert_data_cols"]["url"],data=json.dumps(apis["insert_data_cols"]["data"]))
#resp = requests.request(method=apis["update_data"]["method"], url=apis["update_data"]["url"],data=json.dumps(apis["update_data"]["data"]))
#resp = requests.request(method=apis["select_data"]["method"], url=apis["select_data"]["url"],data=json.dumps(apis["select_data"]["data"]))
#resp = requests.request(method=apis["delete_data"]["method"], url=apis["delete_data"]["url"],data=json.dumps(apis["delete_data"]["data"]))
#resp = requests.request(method=apis["show_tables"]["method"], url=apis["show_tables"]["url"])
#resp = requests.request(method=apis["create_index"]["method"], url=apis["create_index"]["url"],data=json.dumps(apis["create_index"]["data"]))
#resp = requests.request(method=apis["show_index"]["method"], url=apis["show_index"]["url"],data=json.dumps(apis["show_index"]["data"]))
#resp =  requests.request(method=apis["drop_index"]["method"], url=apis["drop_index"]["url"],data=json.dumps(apis["drop_index"]["data"]))
#resp =  requests.request(method=apis["rename_table"]["method"], url=apis["rename_table"]["url"],data=json.dumps(apis["rename_table"]["data"]))
#resp = requests.request(method=apis["create_query"]["method"], url=apis["create_query"]["url"],data=json.dumps(apis["create_query"]["data"]))
#resp = requests.request(method=apis["show_columns"]["method"], url=apis["show_columns"]["url"],data=json.dumps(apis["show_columns"]["data"]))
#resp = requests.request(method=apis["create_view"]["method"], url=apis["create_view"]["url"],data=json.dumps(apis["create_view"]["data"]))
#resp = requests.request(method=apis["alter_view"]["method"], url=apis["alter_view"]["url"],data=json.dumps(apis["alter_view"]["data"]))
#resp = requests.request(method=apis["truncate_table"]["method"], url=apis["truncate_table"]["url"],data=json.dumps(apis["truncate_table"]["data"]))
#resp = requests.request(method=apis["drop_table"]["method"], url=apis["drop_table"]["url"],data=json.dumps(apis["drop_table"]["data"]))
#print(resp.text)
