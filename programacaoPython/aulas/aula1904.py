#exercicio 1

idade = int(input("Digite sua idade e descobra sua idade nos outros planetas: "))


anosMercurio = int(0.2408467 * idade)
anosVenus =  int(0.61519726 * idade)
anosMarte =  int(1.8808158 * idade)
anosJupiter =  int(11.862615 * idade)
anosSaturno =  int(29.447498 * idade)
anosUrano = int(84.016846 * idade)
anosNetuno = int(164.79132 * idade)

print(f"Em mercurio vc terá {anosMercurio} anos, em Venus {anosVenus} anos, em Marte {anosMarte} anos, em Jupiter {anosJupiter} anos, em Saturno {anosSaturno} anos, em Urano {anosUrano} anos e em Netuno {anosNetuno} anos")

#exercicio 2

numero = int(input("Digite um numero:"))
limite = int(input("Digite um limite:"))

contador = 0
for x in range(1, limite):
   if(x % numero == 0):
      contador = x + contador
print(contador)

# exercicio 3

from num2words import num2words

num = int(input("digite um numero:"))
num_extenso = num2words(num, lang='pt_BR')

if(num >= 0 and num <= 999.999):
    print(f" numero: {num_extenso}")
else:
  print("Digite um numero de 0 a 999.999!!!!")
