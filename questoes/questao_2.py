## QUESTÃO 2 ##
# Uma forma de avaliar se uma pessoa está acima do peso é através do calculo do índice IMC. 
# Se o valor do IMC estiver acima de 25, significa que a pessoa está acima do peso. 
# A fórmula é: IMC = Peso(Kg) / (Altura(m)*Altura(m)). Com base na altura e peso fornecido no 
# console exiba uma mensagem determinando se uma pessoa está acima do peso.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
        peso = int(input('Quantos Kilos voce pesa?: '))
        altura = float(input('Qual sua altura?: '))
        IMC = (peso/(altura*altura))
    if (IMC>25):
        print ('Você está acima do peso!')
        print (IMC)
    else:
        print ('Você está abaixo do peso!')
        print (IMC)



if __name__ == '__main__':
    main()
