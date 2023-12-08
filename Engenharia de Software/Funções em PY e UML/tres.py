#funcao tres, diagrama na foto


i = 1

while i < 4:
  nome = (str(input(f"Digite o nome da pessoa {i}: ")))
  peso = (float(input(f"Digite o peso da pessoa {i}: ")))
  altura = (float(input(f"Digite a altura da pessoa {i}: ")))
  i += 1

def diabo(nome, peso, altura):

  imc = (peso / altura*altura)

acima = []

if imc > 25 or imc > 18.5 :
  imc.append(acima)
print(f"Usuário acima do peso.")

diabo(nome, peso, altura)