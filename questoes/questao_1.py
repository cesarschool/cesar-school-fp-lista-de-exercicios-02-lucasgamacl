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
    x = []
for n in range(5):
 numeros = int(input('digite números'))
 x.append(numeros)
print ('maior número da lista é:', max(x),'menor número da lista é:', min (x))
    


if __name__ == '__main__':
    main()
