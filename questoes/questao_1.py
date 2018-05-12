## QUESTÃO 1 ##
# Faça um programa que receba cinco inteiros e diga qual deles é o maior e qual o menor.
##

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
        lista = [0,1,2,3,4]
    for x in range(5):
        lista[x] = int(input('Digite os numeros: '))
    print('O maior número da lista é',max(lista) ,'O menor número da lista é', min(lista))



if __name__ == '__main__':
    main()
