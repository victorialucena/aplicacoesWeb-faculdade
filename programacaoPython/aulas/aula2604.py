# exercicio 1

for y in range(1,5):
  forma = "*" * y
  print(forma)

#exercicio 2

altura = int(input("Digite uma altura:"))
largura = int(input("Digite uma largura:"))

forma = "*" * largura

for y in range(altura):
  print(forma)

# exercicio 3

triangulo = int(input("Digite o valor do triângulo: "))

for x in range(1, triangulo + 1):
    forma = " " * (triangulo - x)
    asteriscos = "*" * (2*x - 1)
    print(forma + asteriscos)



#exercicio 4

valorDaConta = float(input("Digite o valor da conta:"))
gorjeta = 0.1
valorComGorjeta = valorDaConta * gorjeta
valorTotal = valorDaConta + valorComGorjeta

print(f"o valor total da compra é {valorTotal} reais")

#exercicio 5

horasTrabalhadas = int(input("Digite suas horas trabalhadas: "))
valorPorHora = float(input("Digite o valor recebido por hora trabalhada:"))
salarioDiario = horasTrabalhadas * valorPorHora

print(f"Seu salário diario é de: {salarioDiario} reais")

#exercicio6
idade = int(input("insira sua idade: "))
diasvividos = idade * 365
print(f"você viveu aproximadamente {diasvividos} dias")
         
 #exercicio7
idade = int(input("insira sua idade: "))
idadeDezAnos = idade + 10

print(f"em 10 anos você terá {idadeDezAnos} anos")

#exercicio 8 

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

media = (nota1+nota2) / 2

print(f"Sua média foi: {media}")
