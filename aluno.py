import csv
with open('alunos.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print (linha)