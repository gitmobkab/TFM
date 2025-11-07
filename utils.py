from typing import Literal
from rich import print as rprint

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
        




def parse_csv(path, lines: int = 50) -> list[str]:
    with open(path,"r") as file:
        content = file.readlines()
        # on lit 51 lignes, la première ligne défini les colonnes
        return content[:lines+1]
    
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


    
    
    