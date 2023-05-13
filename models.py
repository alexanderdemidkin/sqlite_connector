from pydantic import BaseModel

class Table_dict(BaseModel):
    name : str
    columns : dict

class Table_name(BaseModel):
    name : str

class Table_list(BaseModel):
    name: str
    columns: list

class Table_new_name(BaseModel):
    old : str
    new : str


class Table_index(BaseModel):
    table : str
    index : str

class Table_cols(BaseModel):
    name: str
    cols: list
    vals: list

class Table_upd(BaseModel):
    name: str
    cols: dict
    where:str

class Table_select(BaseModel):
    name: str
    cols: list
    where:str

class Table_del(BaseModel):
    name: str
    where:str

class View_mod(BaseModel):
    name: str
    table: str
    cols: list
    where:str