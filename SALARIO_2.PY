nome=(input)("Qual seu nome?")
idade=int(input("Qual sua idade?"))
salario=float(input("Quanto você ganha mesalmente?"))
if salario<=1500:
    desconto=0
elif salario>=1501 and salario <2500:
    desconto=salario * 0.05
elif salario>=2501 and salario <4000:
    desconto=salario * 0.10
else:
    desconto=salario * 0.15
salario=salario-desconto
print(f'Salário a receber é de R${salario}0, ')
print(f'desconto aplicado é de de R${desconto}0, ')