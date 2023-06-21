#Erro: Eu pedi para o chat gpt programar um cronometro, mas ele programou um timer, pois nós colocamos o tempo desejado no início
# quando em um cronometro se começa do zero para cima.
import time

def cronometro(tempo):
    while tempo:
        minutos, segundos = divmod(tempo, 60)
        timer = '{:02d}:{:02d}'.format(minutos, segundos)
        print(timer, end="\r")
        time.sleep(1)
        tempo -= 1

    print("Tempo esgotado!")

tempo_total = int(input("Digite a quantidade de segundos para o cronômetro: "))
cronometro(tempo_total)
