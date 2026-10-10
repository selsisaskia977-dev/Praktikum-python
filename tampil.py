from rich.console import Console
from rich.table import Table

console = Console()
table = Table(title="Daftar Alat Praktikum")

table.add_column("No", justify="right")
table.add_column("Alat")
table.add_column("Fungsi")

table.add_row("1", "VS Code", "Menulis dan menjalankan kode")
table.add_row("2", "venv", "Mengisolasi paket proyek")
table.add_row("3", "Git", "Mencatat riwayat perubahan")

console.print(table)