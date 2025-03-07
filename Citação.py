pl = input("Primeira Linha.\n")
n = input("Deseja continuar a citação se SIM 's' se NAO 'n'.")
while True:
    if n == "s":
        with open('Citação.txt', 'w') as arquivo:
            arquivo.write (pl + '\n')
            input(pl)