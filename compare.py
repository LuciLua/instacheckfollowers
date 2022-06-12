from numpy import array
import rich
from rich.table import Table
from rich.console import Console

qt_seguidores = 0
qt_seguindo = 0

def formatacoes(lista):
    lista = lista.replace("\n", ',')
    lista = lista.replace('"', '')
    lista = lista.split(',')
    return lista


with open('seguidores.txt', 'r') as arquivo:
    lista = arquivo.read()
    lista = formatacoes(lista)
    
    seguidores = array(lista)
    qt_seguidores = lista.__len__()

with open('seguindo.txt', 'r') as arquivo:
    lista = arquivo.read()
    
    lista = formatacoes(lista)
    seguindo = array(lista)
    
    qt_seguindo = lista.__len__()
    
reciproco = []
nao_reciproco = []
# Quem eu sigo e me segue de volta
for seguindoo in seguindo:
    for seguidoress in seguidores:
        if seguindoo == seguidoress:
            reciproco.append(seguidoress)
            
difference = set(seguindo).difference(set(seguidores))

table = Table(title="Relação seguidores Instagram")

table.add_column("Seguindo", justify="right", style="green")
table.add_column("Seguidores", justify="right", style="green")
table.add_column("Seguindo e Seguidores", justify="right", style="green")
table.add_column("[red]Seguindo e Não-Seguidores", justify="right", style="green")

table.add_row("{}".format(qt_seguindo), "{}".format(qt_seguidores), "{}".format(array(reciproco).__len__()), "[red]{}".format((difference).__len__()))

console = Console()
console.print(table)
rich.print("Relação de [red] Seguindo e Não-Seguidores ({}) [/] gerada em um novo arquivo".format((difference).__len__()))

with open('naoMeSeguemDeVolta.txt', 'w') as arquivo:
    for diff in difference:
        arquivo.write('https://instagram.com/{}\n'.format(diff))