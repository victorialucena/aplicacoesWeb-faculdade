#exercicio 1

frase = "Portable Network Graphics"

palavras = frase.split()

sigla = ""

for palavra in palavras:
    sigla += palavra[0].upper()

print(f"A sigla da frase '{frase}' é {sigla}")

#exercicio 2

cpf = "51372358811"

identificador_estado = cpf[8]

estado = ""

if identificador_estado == "1":
    estado = "Distrito Federal, Goiás, Mato Grosso do Sul ou Tocantins"
elif identificador_estado == "2":
    estado = "Pará, Amazonas, Acre, Amapá, Rondônia ou Roraima"
elif identificador_estado == "3":
    estado = "Ceará, Maranhão ou Piauí"
elif identificador_estado == "4":
    estado = "Pernambuco, Rio Grande do Norte, Paraíba ou Alagoas"
elif identificador_estado == "5":
    estado = "Bahia ou Sergipe"
elif identificador_estado == "6":
    estado = "Minas Gerais"
elif identificador_estado == "7":
    estado = "Rio de Janeiro ou Espírito Santo"
elif identificador_estado == "8":
    estado = "São Paulo"
elif identificador_estado == "9":
    estado = "Paraná ou Santa Catarina"
elif identificador_estado == "0":
    estado = "Rio Grande do Sul"
else:
  print("algo de errado com seu número")

print(f"O CPF pertence a: {estado}")

#exercicio 3

from math import pow

numero = input("Digite um número: ")
total = 0

for digito in numero:
    valor = pow(int(digito), len(numero))
    total += valor

if int(numero) == total:
    print(f"{numero} é um número de Armstrong!")
else:
    print(f"{numero} não é um número de Armstrong!!")
