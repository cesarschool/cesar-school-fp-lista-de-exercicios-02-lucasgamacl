## QUESTÃO 4 ##
# Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. 
# O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos 
# a pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o 
# valor da prestação como sendo o valor da casa a comprar dividido pelo número de 
# meses a pagar.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    house = int(input('Qual o preço da casa?: '))
    pay = int(input('Qual o seu salário?: '))
    months = int(input('Em quantos meses a divida será paga?: '))
    x = (house/months)
    y = ((pay/100)*30)
    if (x>=y):
        print('Você não pode pagar a casa!')
        print('As parcelas custam: ', x)
        print('30% do seu salário é: ', y)
    else:
        print('Você pode comprar a casa!')
        print('As parcelas custam: ', x)
        print('30% do seu salário é: ', y)


    
if __name__ == '__main__':
    main()
