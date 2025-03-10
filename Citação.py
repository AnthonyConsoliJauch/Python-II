with open ('citação.txt', 'w') as arquivo:
    l1=input("Digite suas citacoes favoritas: ")
    arquivo.write(l1 + '\n')
fa=input("deseja continuar se sim aperte s se não aperte n: ")
 
while True:
    if fa == 's':
         l2=input("Digite suas citacoes favoritas: ")
         with open ('citação.txt', 'a')as arquivo:
            arquivo.write(l2 + '\n')
         fa=input("deseja continuar se sim aperte s se não aperte n: ")
    else:
        print("Obrigado pela citação")
        break     