import random

sorteio = random.randint(0, 10)

numeroEscolhido = int(input("Digite um numero de 0 a 10 e descubra se é um numero sorteado: "))

if numeroEscolhido == sorteio:
    print("Uhuul! vc acertou")
else:
    print("Nao foi dessa vez, o numero sorteado foi", sorteio)
