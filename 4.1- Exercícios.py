# Exercício Condicionais

#"input()" trás a função do usuário pressionar algum botão
#"int()" transforma os números em inteiros
numero = int(input("Digite um Número Inteiro: "))

if numero > 0: # se for maior do que 0 = positivo
    if numero % 2 == 0: # se for dívisivel por 2 é par, se não, é impar
        print("o número é positivo e par.")
    else:
        print("o número é positivo e ímpar.")
elif numero < 0: # se for menor do que 0 = negativo e se é divisível por 5 ou não.
    if numero % 5 == 0:
        print("o número é negativo e divisível por 5.")
    else:
        print("o número é negativo e não é divisível por 5.")
else:
    print("o número é zero.") # se não for nenhuma opção anterior, é 0
