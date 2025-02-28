nome=(input)("Qual seu nome?")
idade=int(input("Qual sua idade?"))
salario=float(input("Quanto você ganha mesalmente?"))
if salario<=1500:
    descont=0
elif salario>=1501 and salario <2500:
    descont=salario * 0.05
elif salario>=2501 and salario <4000:
    descont=salario * 0.10
else:
    descont=salario * 0.15
salario=salario-descont
print(f'Salário a receber é de R${salario}0 ')
print(f'desconto aplicado é de de R${descont}0 ')