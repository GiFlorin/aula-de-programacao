import time
tempo = 0
def cronometro():
    sla = 'a'
    while True:
        if sla == '':
            break
        global tempo
        minutos, segundos = divmod(tempo, 60)
        timer = '{:02d}:{:02d}'.format(minutos, segundos)
        print(timer, end="\r")
        #sla = input('\r')
        time.sleep(1)
        tempo += 1
print("Ele nunca para, então é melhor só fechar o terminal")
cronometro()
