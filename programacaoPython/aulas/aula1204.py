# in percorre - web scraping

nome = "cruzeiro"

if("z" in nome):
  print("tem Z!")
else:
  print("nao tem z!")

if(nome[0] == "c"):
  print("Tem C")
else: 
  print("n tem c")


for x in range(1, 11):
  print(x * 5)

qnt = 0
nome = "cruzeiro"

for letra in nome:
  if(letra == "r"):
     qnt = qnt + 1
print(qnt, "letras r")

for x in range(1, 10):
  if(x % 2 == 0):
    print(x)

num = int(input("Digite um numero: "))

while(num > 10):
  num = int(input("digite um numero: "))

num = 0

while(num > 5):
  print(num)
  num = num + 1

qntdd = 0
num =0
noe = "cruzeiro"

while(num < 8):
  if(nome[num] == "r"):
    qntdd = qntdd + 1
  num = num + 1
print(qntdd, "letras 3")

for y in range(1,10):
  palavra = "incomodam" * y
  print(palavra)