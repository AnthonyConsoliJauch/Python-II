nome=(input)("Qual seu nome?")
idade=int(input("Qual sua idade?"))
tem_carteira=input("Tem carteira de motorista? Digite s para SIM, e n para NÃO.")
if idade >=18 and tem_carteira == 's':
    print("Pode dirigir")
else:
    print("Não pode dirigir")