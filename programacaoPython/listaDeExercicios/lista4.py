#exercicio 1

par = []
impar = []

numeros = [3, 4, 6, 5, 8, 9, 1, 2, 7, 10]
for x in range(len(numeros)):
  if(numeros[x] % 2 == 0):
   par.append(numeros[x]) 
  else:
    impar.append(numeros[x]) 

print(par)
print(impar)

#Exercicio 2

lista = [78,98,54,65,41]

lista.reverse()

print(lista)

#exercicio 3

lista1 = ["B", "di", "pes"]
lista2 = ["om", "a", "soal"]

result = []
convert = []
separator = ' '
for n1, n2 in zip(lista1, lista2):
  result.append(n1 + n2)
  convert = [separator.join(result)]
print(convert)

#exercicio 4
lista = [11, 14, 17, 80, 109, 114, 1, 8, 9, 2]
maior = 0
posição = 0 

for x in range(0, len(lista)):
        if lista[x] > maior:
            maior = lista[x]
            posicaoMaiorValor = x
          
print(f"O maior valor é: {maior}")
print(f"Ele está na posição: {posicaoMaiorValor}")   

