#exercicio1

comprimento = float(input("Digite o comprimento em centimetros: "))

if(comprimento > 1001):
  novoComprimento = comprimento / 10000
  print("o comprimento é de", novoComprimento, "quilometros")
elif (comprimento > 101):
  novoComprimento = comprimento / 100
  print("O comprimento é de", novoComprimento, "metros.")
elif(comprimento > 1):
  print("O comprimento é positivo")
else:
  print("valor invalido")

#exercicio2

ladoA = float(input("Digite o primeiro lado do triangulo: "))
ladoB = float(input("Digite o segundo lado do triangulo: "))
ladoC = float(input("Digite o terceiro lado do triangulo: "))

if (ladoA == ladoB and ladoA == ladoC):
  print("Triangulo equilátero")
  area = (ladoA * ladoB) / 2
  print("A area do trinangulo é", area)

#exercicio3

tempoDeServico = int(input("Digite seu tempo de serviço: "))
salario = float(input("Digite seu salario: "))

if(tempoDeServico > 5):
  bonus = salario * 0.05
  total = bonus + salario 
  print("O valor de bonus é de:", bonus)
  print("Seu novo salario será de:", total)
else:
  print("Tempo de servico insuficiente")

# exercicio4

custo = float(input(" Digite o custo da quantidade comprada: "))

if(custo > 1000):
  desconto = custo * 0.10
  valorComDesconto = custo - desconto
  print(f"O valor do seu desconto é de: {desconto}")
  print(f"O valor com desconto é de: {valorComDesconto}")
else:
  print("Valor para desconto não atingido")

#exercicio 5

frequencia = float(input("Digite sua frênquencia escolar:"))
mediaNota = float(input("Digite a média da sua nota:"))

if(frequencia >= 75 and mediaNota >= 6):
  print("Você poderá realizar a avaliação final")
else:
  print("Você não poderá realizar a avaliação final")

#exercicio 6
  
anoDeFabricacao = int(input("Digite o ano de fabricação: "))
corDoCarro = input("Digite a cor do carro: ")

if(anoDeFabricacao < 2000 or anoDeFabricacao > 2015):
  print("O preço do combustível para seu veiculo será 5.99")
elif(corDoCarro in ["vermelho", "azul", "verde"]):
  print("Você ganhou uma ducha grátis!")
elif(anoDeFabricacao >= 2001 and anoDeFabricacao <= 2014 or corDoCarro == "preto"):
  print("Você ganhou um chaveiro")
else:
  print("Oppps, você não ganhou nada :/")

#exercicio 7

nota = float(input("Digite sua nota: "))

if(nota < 25):
  print("sua nota no sistema é F")
elif(nota >= 25 and nota < 45):
  print("sua nota no sistema é E")
elif(nota >= 45 and nota < 50):
  print("sua nota no sistema é D")
elif(nota >= 50 and nota < 60):
  print("sua nota no sistema é C")
elif(nota >= 60 and nota <= 80):
  print("sua nota no sistema é B")
elif(nota > 80):
  print("sua nota no sistema é A")
else:
  print("Há algo de errado c sua nota!")