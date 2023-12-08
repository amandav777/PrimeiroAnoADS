#funcao um, diagrama na foto 1

valor_Total = (float(input("Valor total da empresa: ")))

sum = (str(input("Nome do primeiro sócio: ")))
pcum = (float(input("Porcentagem do primeiro sócio: ")))

sdois = (str(input("Nome do segundo sócio: ")))
pcdois = (float(input("Porcentagem do segundo sócio: ")))

stres = (str(input("Nome do terceiro sócio: ")))
pctres = (float(input("Porcentagem do terceiro sócio: ")))


a = valor_Total / pcum
b = valor_Total / pcdois 
c = valor_Total / pctres 

socios(sum, pcum, sdois, pcdois, stres, pctres)

def socios(sum, pcum, sdois, pcdois, stres, pctreis):
  print(f"O valor total da empresa é: {valor_Total}. \n Propriedade individual - {sum}: R$ {a}. \n  Propriedade individual - {sdois}: R$ {b} \n Propriedade individual - {stres}: R$ {c}.")