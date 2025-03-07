with open('poema.txt', 'r') as arquivo:
    conteudo=arquivo.read()
    print(conteudo)
with open('poem.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha.strip())