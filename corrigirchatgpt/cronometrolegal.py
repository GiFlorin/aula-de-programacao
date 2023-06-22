import time
import keyboard

def verifica_tecla(tecla):
    return keyboard.is_pressed(tecla)

tempo = 0
def cronometro():
    while True:
        if verifica_tecla(' '):
            break
        global tempo
        minutos, segundos = divmod(tempo, 60)
        timer = '{:02d}:{:02d}'.format(minutos, segundos)
        print(timer, end="\r")
        #sla = input('\r')
        time.sleep(1)
        tempo += 1
print("Segure espaço para parar")
cronometro()
