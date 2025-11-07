DEFAULT_LINES_COUNT = 50

from typing import Literal
from rich import print as rprint
import os

# Will be used for user feedback 
# EX -> :INFO: PARSING CSV FILES...
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


    
    
    