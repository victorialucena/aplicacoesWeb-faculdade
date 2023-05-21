#exercicio 1)	Salvar o reino de Westeros
cidade = "Porto Real"
direcao = "norte"
gravidade = "alta"

print("Alerta! Uma invasão de Caminhantes Brancos está acontecendo agora em",cidade,"," "vindo do", direcao,". A situação é", gravidade,"e todos devem se preparar para a defesa.")


#exercicio 2)	Aventura na floresta

passos_frente = 50
direcao_direita = 30
direcao_esquerda = 40

print("Siga em frente por", passos_frente,"passos." "Depois, vire à direita por", direcao_direita,"passos. Finalmente, vire à esquerda por",direcao_esquerda,"passos.")


#exercicio 3)	O Resgate da Princesa

distancia_ate_fortaleza = int(50/10)
nome_cavaleiro = "Sir Lancelote"


print(nome_cavaleiro,"levará",distancia_ate_fortaleza, "dias para chegar à fortaleza.")


#exercicio 4)	Jogo de corrida

potencia_motor = int(input("Insira a potência do motor (entre 100 e 500): "))
peso_carro = float(input("Insira o peso do carro (entre 1000 e 2000 kg): "))
velocidade_media = (potencia_motor / peso_carro) * 1000
print(f"A velocidade média do carro é {velocidade_media:.2f} km/h")


#exercicio 5) Descontão de Páscoa

valor_original = float(input("Digite o preço original do produto: "))

desconto = 0.3

calculo_desconto = int(valor_original * desconto)

valor_final = (valor_original - calculo_desconto)

print("Valor original do produto: ", valor_original)

print("Valor do desconto aplicado : 30% ")

print("Valor do desconto :", valor_final)


#7)	Automatizado os cálculos da loja

preco = float(input("Digite o preço unitário da peça de roupa: "))
quantidade = int(input("Digite a quantidade de peças compradas: "))
desconto = float(input("Digite o desconto aplicado: "))

preco_total = preco * quantidade

if desconto > 0:
  valor_desconto = preco_total * (desconto / 100)
  preco_total -= valor_desconto

print("O preço final da compra é R$ {:.2f}".format(preco_total))


#LISTA2
#exercicio 1 

salario = float(input("Digite seu salário: "))
gastos = float(input("Digite o valor gasto no mês: "))

if gastos > salario:
  print("seus gastos estão acima do orçamento!!")
else:
  print("seus gastos estão dentro do orçamento :)")


#exercicio 2 

numero = int(input("Digite um número para descobrir se é divisivel por 5: "))

if numero % 5 == 0:
  print("O", numero, "é divisivel por 5")
else:
  print("O", numero, "não é divisivel por 5 :(")


#exercicio 3

numero_impar_ou_par = int(input("Digite um número para descobrir se é impar ou par: "))

if numero_impar_ou_par % 2 == 0:
  print("O", numero_impar_ou_par, "é par")
else:
  print("O", numero_impar_ou_par, "é impar")

#exercicio 4

x = int(input("Digite um número:"))
a = 2
b = 3
c = 4

if x % 2 == 0:
    mediaAritimetica = (a + b + c) / 3
    print(f"A média aritméticaé: {mediaAritimetica:.2f}")
else:
    if x > 10:
        media_ponderada = (2*a + 3*b + 4*c) / (2+3+4)
        print(f"A média ponderada de é: {media_ponderada:.2f}")

#exercicio 5

numero = (10, 5, 8)

ordem_crescente = sorted(numero)

print(ordem_crescente)