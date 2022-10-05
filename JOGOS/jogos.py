import forca
import adivinhacao

def escolhaJogo():
    print('---------------------------------')
    print('------Escolha o seu jogo---------')
    print('---------------------------------')

    print('[1] Forca | [2] Adivinhação')

    jogo = int(input("Resposta: "))

    if(jogo == 1):
        forca.jogar()

    elif(jogo == 2):
        adivinhacao.jogar()

if(__name__ == '__main__'):
    escolhaJogo()