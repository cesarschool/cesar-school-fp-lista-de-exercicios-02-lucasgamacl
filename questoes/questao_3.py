## QUESTÃO 3 ##
# Implementar um programa que calcula o desconto previdenciário de um funcionário. 
# O programa deve, dado um salário, retornar o valor do desconto proporcional ao mesmo. 
# O cálculo de desconto segue a regra: o desconto deve 11% do valor do salário, entretanto, 
# o valor máximo de desconto é 318,20.
# Sendo assim, ou o programa retorna 11% sobre o salário ou 318,20.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    Cash = int(input('Qual o seu salário?: '))
    DTO = ((Cash/100)*11)
    if DTO>=318.20:
        print('Seu salário com desconto é: ', (Cash - 318.20))
    else:
        print('Seu salário com desconto é: ', (Cash - DTO))


    
if __name__ == '__main__':
    main()
