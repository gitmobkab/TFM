from typing import Literal
from rich import print as rprint
import os,json,mariadb,sys
from rich.console import Console
from rich.table import Table

DEFAULT_LINES_COUNT = 50

def load_config(config_path):
    if os.path.isfile(config_path) :
        with open(config_path,"r") as file:
            return json.load(file)
    
    empty_config = {
        "user": {
            "name": "",
            "password": "",
            "database": "",
            "table": "",
            "host": "localhost",
            "port": 3306
        },
        
        "generation":{
            "optimized": False,
            "rows": 50
        },
        
        "parse":{
            "rows": 50
        }
            
    }
    return empty_config 

# Will be used for user feedback 
# EX -> :INFO: PARSING CSV FILES...
def preview_data(columns: list[str],data: list[str]):
    
    data_len = len(data[1:])
    if data_len < 15:
        size = data_len
    else:
        size = 15
    
    table = Table(title="preview_table.tfm", caption=f"--- {size} lines ---")
    console = Console()
    
    table.add_column("Line", justify="center", style="blue bold") # set up special column for line number display
    
    for column in columns:
        table.add_column(column,justify="center")  
        
    for i in range(size):
        table.add_row(
            str(i+1), *data[i].split(",")
        )  
    console.print(table)
    

def log(info: str, mode: Literal["info","success","warning","error"]) -> None:
    if mode == "info":
        rprint(f"[blue bold]:INFO:[/blue bold] {info}")
    elif mode == "success":
        rprint(f"[green bold]:SUCCESS:[/green bold] {info}")
    elif mode == "warning":
        rprint(f"[orange bold]:WARNING:[/orange bold] {info}")
    elif mode == "error":
        rprint(f"[red bold]:ERROR:[/red bold] {info}")
        


def get_file_ext(file: str) -> str:
    file_info = os.path.splitext(file)
    return file_info[1]


    
def parse_csv(path, lines: int = DEFAULT_LINES_COUNT) -> list[str]:
    with open(path,"r") as file:
        content = file.readlines()
        # on lit n+1 lignes parce que la première ligne défini les colonnes
        if len(content) >= lines:
            return content[:lines+1]
        else:
            return content
    
def define_csv_columns(line: str) -> list[str] | None:
    if not line:
        return None
    
    words = line.split(",") # get the words separaated by comma
    # filtering whitespace from each words
    clean_words = []
    for word in words:
        clean_word = word.strip()
        if not clean_word:
            clean_word = "UNDEFINED"
        clean_words.append(clean_word)
            
    return clean_words


def gen_query_placeholder(length: int = 1) -> str:
    # use multiplication on the tuple ("?",) <length> times then turn the tuple into a valid string with join

    placeholder = ("?",) * length # multiplication Ex: ("?",) * 3 = ("?", "?", "?")
    
    placeholder_str = ",".join(placeholder)
    
    return placeholder_str

def make_columns_str(columns: list[str]) -> str:
    if not columns:
        return ""
    
    return ",".join(columns)

def mariadb_fill_table(conn_obj: mariadb.Connection , cursor_obj: mariadb.Cursor, table: str, columns : list[str], values: list[tuple[str]]):
    if not columns:
        log("Can't make INSERT INTO query without at least one column","error")
        sys.exit(1)
    
    query_placeholder = gen_query_placeholder(len(columns))
    columns_str = make_columns_str(columns)
    insert_query = f"INSERT INTO {table} ({columns_str}) VALUES ({query_placeholder})"
    
    log("Inserting Data...","info")
    try:
        cursor_obj.executemany(insert_query, values)
        conn_obj.commit()
        log("Inserting Data... Done", "success")
        log(f"Inserted {cursor_obj.rowcount} rows", "success")
        log(f"Last inserted ID: {cursor_obj.lastrowid}", "info")
    except mariadb.IntegrityError as error:
        log(f"Error Inserting Data (might be due to duplicate for a unique type column): {error}", "error")
        conn_obj.rollback()
    except mariadb.Error as error:
        log(f"Error Inserting Data: {error}","error")
        conn_obj.rollback()     
        

def run_db_table_filling(data : list[tuple],**conn_params):
    conn = None
    cursor = None
    
    try:
        log("Connecting to MariaDB/MySQL...", "info")
        conn = mariadb.connect(**conn_params)
        log("Connection successfull !", "success")
        
        cursor = conn.cursor()
        
        # filling operations there
        mariadb_fill_table(conn, cursor, conn_params["table_name"],conn_params["columns"],data)
        
    except Exception as error:
        log(f"The Following error occured: {error}", "error")
        sys.exit(1)
        
    finally:
        if cursor:
            cursor.close()
            log("Cursor closed !", "info")
        
        if conn:
            conn.close()
            log("Connection closed !", "info")
        
        rprint("[bold green] Bye ![/bold green]")
