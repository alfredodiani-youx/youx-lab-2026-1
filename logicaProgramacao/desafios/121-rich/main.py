from rich import print
from rich.panel import Panel
from rich.table import Table
print("Olá [red]Mundo![/red] :earth_americas:")
print("[bold blue on red]Olá :1st_place_medal:[/]")
print(Panel("oi", title="oi", style="#000000"))
tabela = Table(title="teste")
tabela.add_column("nome")
tabela.add_column("idade")
tabela.add_row("1", "2")
print(tabela)
