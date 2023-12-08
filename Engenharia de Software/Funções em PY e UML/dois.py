#funcao dois, diagrama na foto 2

aum = (str(input("Nome do primeiro aluno: ")))
num = (float(input("Nota do primeiro aluno: ")))
adois = (str(input("Nome do segundo aluno: ")))
ndois = (float(input("Nota do segundo aluno: ")))
atres = (str(input("Nome do terceiro aluno: ")))
ntres = (float(input("Nota do terceiro aluno: ")))
media = (num + ndois + ntres)/3
minimo = 7

def usuario(aum, num, adois, ndois, atres, ntres):

  print(f"A média da turma é {media:.1f}.")

  if num < minimo:
   print(f"{aum} abaixo da média.")

  if ndois < minimo:
   print(f"{adois} abaixo da média.")

  if ntres < minimo:
    print(f"{atres} abaixo da média.")

usuario(aum, num, adois, ndois, atres, ntres)
