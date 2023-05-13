from main import app
import logging
from db import SQLite_db
from models import Table_dict, Table_name, Table_list, Table_new_name, Table_index, Table_cols
from models import Table_upd, Table_select, Table_del, View_mod


db = SQLite_db('api.db')

############################# table ################################f
@app.post("/api/db/table/create")
async def api_create_table(tbl: Table_dict):
    """
    api to create table in SQLite database
    param: 
        table_name: string,
        table_columns: dictionary  {column_name: column_type}
    result: response json
    """
    try:
        print(tbl.name, tbl.columns)
        db.create_table(tbl.name, tbl.columns)
        return {"api": "create table", "name": tbl.name, "columns": tbl.columns, "status": "success"}
    except Exception as e:
        logging.error(e)
        return {"api": "create table","name": tbl.name, "columns": tbl.columns, "status": "error", "error": e}
    
@app.post("/api/db/table/drop")
async def api_drop_table(tbl: Table_name):
    """
    api to drop table in SQLite database
    param: 
        table_name: string,
    result: response json
    """
    try:
        db.drop_table(tbl.name)
        return {"api": "drop table", "name": tbl.name, "status": "success"}
    except Exception as e:
        logging.error(e)
        return {"api": "drop table", "name": tbl.name, "status": "error", "error": e}
    
@app.post("/api/db/table/rename")
async def api_rename(tbl: Table_new_name):
    """
    api to rename table in SQLite database
    param: 
        table_name: string,
    result: response json
    """
    try:
        db.rename_table(tbl.old, tbl.new)
        return {"api": "rename table", "old": tbl.old, "new": tbl.new, "status": "success"}
    except Exception as e:
        logging.error(e)
        return {"api": "rename table", "old": tbl.old, "new": tbl.new, "status": "error", "error": e}
    

@app.get('/api/db/table/show_all')
async def api_show_all():
    try:
        return {"api": "show all tables", "tables": db.show_all_tables()}
    except Exception as e:
        logging.error(e)
        return {"api": "show all tables", "status": "error", "error": e}



##################### columns #########################


@app.post("/api/db/table/alter_add")
async def api_alter_add(tbl: Table_dict ):
    """
    api to add column in SQLite database
    param: 
        table_name: string,
        table_columns: dictionary  {column_name: column_type}
    result: response json
    """
    
    try:
        db.update_table_add(tbl.name, tbl.columns)
        return {"api": "alter add", "name": tbl.name, "columns": tbl.columns, "status": "success"}
    except Exception as e:
        logging.error(e)
        return {"api": "alter add", "name": tbl.name, "columns": tbl.columns, "status": "error", "error": e}
    
    
@app.post("/api/db/table/alter_drop")
async def api_alter_drop(tbl: Table_list):
    """
    api to drop column in SQLite database
    param: 
        table_name: string,
        table_columns: list  [column_name]
    result: response json
    """
    
    try:
        db.update_table_drop(tbl.name, tbl.columns)
        return {"api": "alter drop", "name": tbl.name, "columns": tbl.columns, "status": "success"}
    except Exception as e:
        logging.error(e)
        return {"api": "alter drop", "name": tbl.name, "columns": tbl.columns, "status": "error", "error": e}
    

@app.get('/api/db/table/show_columns')
async def api_show_columns(tbl: Table_name):
    """
    api to show columns on table in SQLite database
    param: 
        table_name: string
    
    result: response json (table data)
    """
    try:
        return {"api": "show columns", "name": tbl.name, "columns": db.show_all_columns(tbl.name)}
    except Exception as e:
        logging.error(e)
        return {"api": "show columns", "name": tbl.name, "status": "error", "error": e}
    

##################### indexes #########################

    
@app.get('/api/db/table/show_indexes')
async def api_show_indexes(tbl: Table_name):
    """
    api to show indexes on table in SQLite database
    param: 
        table_name: string
    
    result: response json (index data)
    """
    try:
        return {"api": "show indexes", "name": tbl.name, "indexes": db.show_all_indexes(tbl.name)}
    except Exception as e:
        logging.error(e)
        return {"api": "show indexes", "name": tbl.name, "status": "error", "error": e}
    

@app.post('/api/db/table/create_index')
async  def api_create_index(tbl: Table_index):
    """
    api to create index on table in SQLite database
    param: 
        table_name: string,
        column: string
    
    result: response json (index data)
    """
    try:
        db.create_index(tbl.table, tbl.index)
        return {"api": "create index", "table_name": tbl.table, "column_name": tbl.index, "status": "success"}
    except Exception as e:
        logging.error(e)
        return {"api": "create index", "table_name": tbl.table, "column_name": tbl.index, "status": "error", "error": e}


@app.post('/api/db/table/drop_index')
async def api_drop_index(tbl: Table_index):
    """
    api to drop index on table in SQLite database
    param: 
        table_name: string,
        index_name: string
    
    result: response json (index data)
    """
    try:
        db.drop_index(tbl.table, tbl.index)
        return {"api": "drop index", "table_name": tbl.table, "index_name": tbl.index, "status": "success"}
    except Exception as e:
        logging.error(e)
        return {"api": "drop index", "table_name": tbl.table, "index_name": tbl.index, "status": "error", "error": e}

@app.post("/api/db/data/insert")
async def api_insert_data(tbl: Table_list ):
    """
    api to insert data on table in SQLite database
    param: 
        name: string,
        columns:list  [column_name]
    result: response json (table data)
    """
    try:
        db.insert_data(tbl.name,tbl.columns)
        return {"api": "insert data", "table_name": tbl.name, "columns": tbl.columns, "status": "success"}
    except Exception as e:
        logging.error(e)
        return {"api": "insert data", "table_name": tbl.name, "columns": tbl.columns, "status": "error", "error": e}

@app.post("/api/db/data/insert_cols")
async def insert_cols(tbl: Table_cols):
    """
    api to insert data on table in SQLite database
    param: 
        name: string,
        cols: list  [column_name],
        vals: list  [column_value]
    
    result: response json (table data)
    """
    try:
        db.insert_data_cols(tbl.name, tbl.cols, tbl.vals)
        return {"api": "insert cols", "table_name": tbl.name, "columns": tbl.cols, "values": tbl.vals, "status": "success"}
    except Exception as e:
        logging.error(e)
        return {"api": "insert cols", "table_name": tbl.name, "columns": tbl.cols, "values": tbl.vals, "status": "error", "error": e}

@app.post("/api/db/data/update")
async def api_update_data(tbl: Table_upd):
    """
    api to update data on table in SQLite database
    param: 
        name: string,
        columns:dict  {column_name:column_value}
        where:string
    result: response json (table data)
    """
    try:
        db.update_data(tbl.name,tbl.cols,tbl.where)
        return {"api": "update data", "table_name": tbl.name, "columns": tbl.cols, "where": tbl.where, "status": "success"}
    except Exception as e:
        logging.error(e)
        return {"api": "update data", "table_name": tbl.name, "columns": tbl.cols, "where": tbl.where, "status": "error", "error": e}
    
    
@app.post("/api/db/data/delete")
async def api_delete_data(tbl: Table_del ):
    """
    api to delete data on table in SQLite database
    param: 
        name: string,
        where:string
    result: response json (table data)
    """
    try:
        db.delete_data(tbl.name,tbl.where)
        return {"api": "delete data", "table_name": tbl.name, "where": tbl.where, "status": "success"}
    except Exception as e:
        logging.error(e)
        return {"api": "delete data", "table_name": tbl.name, "where": tbl.where, "status": "error", "error": e}
    
    
    
@app.get("/api/db/data/select")
async def api_select_data(tbl: Table_select ):
    """
    api to select data on table in SQLite database
    param: 
        name: string,
        cols:list  [column_name]
        where:dict  {column_name:column_value}
    result: response json (table data)
    """
    
    try:
        result = db.select_data(tbl.name, tbl.cols, tbl.where)
        return {"api": "select data", "table_name": tbl.name, "columns": tbl.cols, "where": tbl.where, "status": "success","data": result}
    except Exception as e:
        logging.error(e)
        return {"api": "select data", "table_name": tbl.name, "columns": tbl.cols, "where": tbl.where, "status": "error", "error": e}
    


@app.post("/api/db/view/create")
async def api_create_view(tbl: View_mod):
    """
    api to create view from table in SQLite database
    param: 
        name: string,
        table:string,
        cols:list  [column_name]
        where:string
    result: response json (table data)
    """
    
    try:
        db.create_view(tbl.name,tbl.table,tbl.cols,tbl.where)
        return {"api": "create view", "view_name": tbl.name, "table": tbl.table, "columns": tbl.cols, "where": tbl.where, "status": "success"}
    except Exception as e:
        logging.error(e)
        return {"api": "create view", "view_name": tbl.name, "table": tbl.table, "columns": tbl.cols, "where": tbl.where, "status": "error", "error": e}

    
@app.post("/api/db/view/alter")
async def api_alter_view(tbl: View_mod):
    """
    api to alter view from table in SQLite database
    param: 
        name: string,
        table:string,
        cols:list  [column_name]
        where:string
    result: response json (table data)
    """
    try:
        db.alter_view(tbl.name,tbl.table,tbl.cols,tbl.where)
        return {"api": "alter view", "view_name": tbl.name, "table": tbl.table, "columns": tbl.cols, "where": tbl.where, "status": "success"}
    except Exception as e:
        logging.error(e)
        return {"api": "alter view", "view_name": tbl.name, "table": tbl.table, "columns": tbl.cols, "where": tbl.where, "status": "error", "error": e}
    
    
@app.post("/api/db/view/drop")
async def api_drop_view(tbl: Table_name):
    """
    api to drop view from table in SQLite database
    param: 
        name: string,
    result: response json (table data)
    """
    
    try:
        db.drop_view(tbl.name)
        return {"api": "drop view", "view_name": tbl.name, "status": "success"}
    except Exception as e:
        logging.error(e)
        return {"api": "drop view", "view_name": tbl.name, "status": "error", "error": e}

    
@app.get("/api/db/data/create_query")
async def api_create_query(tbl: Table_select ):
    """
    api to create query from table in SQLite database
    param: 
        name: string,
        cols:list  [column_name]
        where:dict  {column_name:column_value}
    result: response json (table data)
    """
    try:
        return {"api": "create query", "table_name": tbl.name, "columns": tbl.cols, "where": tbl.where, "status": "success", "query": db.create_query(tbl.name, tbl.cols, tbl.where)}
    except Exception as e:
        logging.error(e)
        return {"api": "create query", "table_name": tbl.name, "columns": tbl.cols, "where": tbl.where, "status": "error", "error": e}
    
    
@app.post( '/api/db/table/truncate')
async def api_truncate(tbl: Table_name):
    """
    api to truncate table in SQLite database
    param: 
        name: string,
    result: response json (table data)
    """
    try:
        db.trunc_table(tbl.name)
        return {"api": "truncate table", "table_name": tbl.name, "status": "success"}
    except Exception as e:
        logging.error(e)
        return {"api": "truncate table", "table_name": tbl.name, "status": "error", "error": e}