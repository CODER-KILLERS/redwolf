import os 
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col


logo = ('''\033[1;32m
████████\033[1;37m╗ \033[1;32m██████\033[1;37m╗ \033[1;32m██\033[1;37m╗  \033[1;32m██\033[1;37m╗\033[1;32m███████\033[1;37m╗\033[1;32m███\033[1;37m╗   \033[1;32m██\033[1;37m╗
\033[1;37m╚══\033[1;32m██\033[1;37m╔══╝\033[1;32m██\033[1;37m╔═══\033[1;32m██\033[1;37m╗\033[1;32m██\033[1;37m║ \033[1;32m██\033[1;37m╔╝\033[1;32m██\033[1;37m╔════╝\033[1;32m████\033[1;37m╗  \033[1;32m██\033[1;37m║
\033[1;32m   ██\033[1;37m║   \033[1;32m██\033[1;37m║   \033[1;32m██\033[1;37m║\033[1;32m█████\033[1;37m╔╝ \033[1;32m█████\033[1;37m╗  \033[1;32m██\033[1;37m╔\033[1;32m██\033[1;37m╗ \033[1;32m██\033[1;37m║
\033[1;32m   ██\033[1;37m║   \033[1;32m██\033[1;37m║   \033[1;32m██\033[1;37m║\033[1;32m██\033[1;37m╔═\033[1;32m██\033[1;37m╗ \033[1;32m██\033[1;37m╔══╝  \033[1;32m██\033[1;37m║╚\033[1;32m██\033[1;37m╗\033[1;32m██\033[1;37m║
\033[1;32m   ██\033[1;37m║   ╚\033[1;32m██████\033[1;37m╔╝\033[1;32m██\033[1;37m║  \033[1;32m██\033[1;37m╗\033[1;32m███████\033[1;37m╗\033[1;32m██\033[1;37m║ ╚\033[1;32m████\033[1;37m║
\033[1;37m   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝

''')

os.system('clear')
print(logo)
