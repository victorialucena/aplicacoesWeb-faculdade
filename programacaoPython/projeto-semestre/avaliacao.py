import re
from bitstring import BitArray

print("Projeto Sistemas de Numeração\n\n"
     "Nome: Isaac Felipe RGM 33517771\n"
     "Nome: Lucas Moreti RGM 34487361\n"
     "Nome: Victoria Lucena RGM 34709223\n")

print("Bem vindo ao menu, aqui você terá 4 opções de escolha. Peço que digite o numero da opção para escolher qual operação você deseja realizar \n" ) 
opcoes = 0
while True:
  opcoes = input("\nOpção 1: Conversão de decimal para as bases binário e octadecimal. \n"
                      "Opção 2: Conversão das bases binário e octadecimal para decimal. \n"
                      "Opção 3: Calculadora aritmética de binários, que contemple as operações de soma e subtração. \n"
                   "Opção 4: Sair do programa. \n\n"
                      "Qual das opções você quer escolher ? \n\n")
  opcoes = int(opcoes)
  
  if opcoes == 1:
      while True:
        print("\nOpcão 1: Você escolheu a conversão de decimal para as bases binário e octadecimal.\n")
        n_decimal = input('Digite o numero em decimal: (Ou voltar para ir ao Menu) \n\n')
        if n_decimal == 'voltar': 
          break
          
        n_decimall = int(n_decimal)
        n_binario = bin(n_decimall)
        n_oct = oct(n_decimall)
        print('O numero %d em binário é: %s' % (n_decimall, n_binario[2:]))
        print('O numero %d em octal é: %s' % (n_decimall, n_oct[2:]))
    
  elif opcoes == 2:
      print("\nOpção 2: Conversão das bases binário e octadecimal para decimal. \n")
      while True:
        entrada = input("Digite o numero em binario: (Ou voltar para ir ao Menu) \n\n")
        if entrada == 'voltar':
          break
        elif not re.match("^[01]+$", entrada):
          print("entrada incorreta ")
        else:
          numero_binario = int(entrada)
          numero_decimal = int(entrada,2)
          numero_octal = oct(numero_decimal)
          octal_sem_prefixo = str(numero_octal).lstrip("0o")
          print("\nO numero binario",entrada,"corresponde ao numero",numero_decimal,"em Decimal")
          print("\nO numero binario",entrada,"corresponde ao numero",octal_sem_prefixo,"em Octal\n\n\n")
    
  elif opcoes == 3:
      print("\nOpção 3: Calculadora aritmética de binários, que contemple as operações de soma e subtração. \n")
      print("Escolha uma das duas opções: " ) 
      while True:
          opcoesAritmeticas = input("\nQual das opções você quer escolher ? (Ou voltar para ir ao Menu) \n\n"
            "Opção 1: Soma os binários \n"
                                    "Opção 2: Subtrair os binários \n\n")
          if opcoesAritmeticas == "voltar":
            break
          opcoesAritmeticass = int(opcoesAritmeticas)
          if opcoesAritmeticass == 1:
            print("\nOpcão 1: Você escolheu somar os binários \n")
            numeroSoma1 = input("Agora você precisa digitar o primeiro número binário a ser somado: ")
            numeroSoma2 = input("Agora você precisa digitar o segundo número binário a ser somado: ")
            def adicaoBinario(numeroSoma1, numeroSoma2):
              bit1 = BitArray(bin=numeroSoma1)
              bit2 = BitArray(bin=numeroSoma2)
              result = bit1.uint + bit2.uint
              return bin(result)[2:]
            print(f"\nA soma dos numeros binários {numeroSoma1} e {numeroSoma2} é:", adicaoBinario(numeroSoma1, numeroSoma2))   
        
          elif opcoesAritmeticass == 2:
            print("\nOpção 2: Você escolheu subtrair os binários \n")
            numeroSubtrair1 = input("Agora você precisa digitar o primeiro número binário a ser subtraido: ")
            numeroSubtrair2 = input("Agora você precisa digitar o segundo número binário a ser subtraido: ")
            def subtracaoBinario(numeroSubtrair1, numeroSubtrair2):
              bit1 = BitArray(bin=numeroSubtrair1)
              bit2 = BitArray(bin=numeroSubtrair2)
              result = bit1.uint - bit2.uint
              return bin(result)[2:]
            print(f"\nA subtração dos numeros binários {numeroSubtrair1} e {numeroSubtrair2} é:", subtracaoBinario(numeroSubtrair1, numeroSubtrair2))
            
  elif opcoes == 4:
      print("\nOpção 4: Sair do programa.")
      print("Encerrando o programa...")
      exit(0)

  else:
    print("Numero inválido \n\n")