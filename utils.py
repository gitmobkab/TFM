from typing import Literal
from rich import print as rprint
import os,json,typer
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
            "table": ""
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