import typer,faker
from rich.console import Console
from rich.table import Table

app = typer.Typer()
fake = faker.Faker()

@app.command()
def generate():
    demo_table = Table(title="tfm Table Demo")
    demo_table.add_column("Id", justify="center", style="blue bold")
    demo_table.add_column("full Name", justify="center", style="dark_blue bold")
    demo_table.add_column("Meeting Date", justify="center", style="navy_blue bold")
    demo_table.add_column("Email", justify="center", style="blue")
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
        
        
if __name__ == "__main__":
    app()
