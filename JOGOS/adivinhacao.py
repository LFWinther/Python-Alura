import random
def jogar():

    print('---------------------------------')
    print('Bem vindo no jogo de ADIVINHAÇÃO!')
    print('---------------------------------')

    numerSecreto = random.randrange(1, 11)
    tentativas = 3
    rodada = 1
    verificacao = True
    pontos = 100

    while verificacao :
        print('Nível de dificuldade:')
        print('[1] Fácil | [2] Médio | [3] Difícil')
        nivel = int(input('Resposta: '))
        if(nivel < 0 or nivel > 3):
            print('Digite uma opção válida')
        else:
            verificacao = False
        if(nivel == 1):
            tentativas = 5
        elif(nivel == 2):
            tentativas = 4
        else:
            tentativas =3

    for rodada in range(1, tentativas + 1):
        print('tentativa {} de {}'.format(rodada, tentativas))
        chute1 = input('Digite o um número de 1 a 10: ')
        chute2 = int(chute1)
        acertou = chute2 == numerSecreto
        maior = chute2 > numerSecreto
        menor = chute2 < numerSecreto

        if(chute2 < 1 or chute2 >= 10):
            print('Digite o um número de 1 a 10')
            continue

        print('voce digitou', chute1)
        if(acertou):
            print('Você acertou!!')
            print('Pontos: ', pontos)
            break
        if(maior):
             print('Errou, seu chute foi maior do que o número secreto!')
        elif(menor):
            print('Errou, seu chute foi menor do que o número secreto!')
        pontosPerdidos = abs(numerSecreto - chute2)
        pontos = pontos - pontosPerdidos
    print('Fim de jogo')
if(__name__ == '__main__'):
    jogar()
