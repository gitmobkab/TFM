



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


    
    
    