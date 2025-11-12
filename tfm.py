import typer,faker,os
from rich.console import Console
from rich.table import Table
from utils import *
from pathlib import Path

app = typer.Typer()
fake = faker.Faker()
APP_DIR = typer.get_app_dir("TFM") # change if the app name change (actual: "TFM")
PATH_TO_CONFIG: Path = Path(APP_DIR) / "config.json" # Trust me...

CONFIG = load_config(PATH_TO_CONFIG)

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
def parse(file: str, user: str = CONFIG["user"]["name"] , password: str = CONFIG["user"]["password"], database: str = CONFIG["user"]["database"], table: str = CONFIG["user"]["table"], rows: int = CONFIG["parse"]["rows"]):
    
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
