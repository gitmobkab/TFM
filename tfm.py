import typer,faker,os
from rich.console import Console
from rich.table import Table
from typing import Literal
from utils import *

app = typer.Typer()
fake = faker.Faker()

@app.command()
def generate():
    demo_table = Table(title="tfm Table Demo")
    demo_table.add_column("Id", justify="center", style="blue bold")
    demo_table.add_column("full Name", justify="center", style="dark_blue bold")
    demo_table.add_column("Meeting Date", justify="center", style="navy_blue bold")
    demo_table.add_column("Email", justify="center", style="blue link https://github.com/gitmobkab/TFM")
    demo_table.add_column("gay", justify="center", style="red bold")
    
    for i in range(50):
        demo_table.add_row(
            str(i+1), fake.name(), fake.date(), fake.email(domain="saussage.orl"), str(fake.boolean(75)) 
        )
        
    console = Console()
    console.print(demo_table)
    
    
    
    
@app.command()
def cry(text: str):
    for _ in range(20):
        print(text)
        

@app.command()
def parse(file: str, user: str = "", password: str = "", database: str = "", table: str = "", rows: int = DEFAULT_LINES_COUNT):
    
    # because each commands are heavy to run, it's a good practice to try to stop the execution as soon as possible
    if not os.path.isfile(file):
        log("The provided path is not a file or doesn't exit. Exiting...", "error")
        raise typer.Exit(1)
    
    file_ext = get_file_ext(file)
    
    if file_ext != ".csv":
        log(f"Sorry parse command doesn't support {file_ext} files yet.","warning")
        typer.Abort()
    
    file_content = parse_csv(file, rows)
    columns_names = define_csv_columns(file_content[0])
    
    preview_data(columns_names, file_content[1:])
    
    
    
    
                
        
if __name__ == "__main__":
    app()
