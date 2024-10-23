import serial
import time

polegar = 10
indicador = 9
medio = 8
anelar = 7
midinho = 6
# Configuração da porta serial (substitua '/dev/ttyUSB0' pela porta correta)
arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout=0.5)

# Função para enviar o comando de rotação do servo
def rotateServo(pin, angle):
    command = f"{pin},{angle}\n"  # Formata o comando como 'pino,ângulo'
    arduino.write(command.encode())  # Envia o comando ao Arduino
    time.sleep(0.1)  # Pausa para dar tempo ao Arduino processar o comando

# Função abrir/fechar similar ao código original
def abrir_fechar(pin, on_off):
    if on_off == 1:
        rotateServo(pin, 0)
    elif on_off == 0 and pin != 10 and pin != 9:
        rotateServo(pin, 140)
    elif on_off == 0 and pin == 10:
        rotateServo(pin, 150)
    elif on_off == 0 and pin == 9:
        rotateServo(pin, 180)

# Função para testar todos os servos
def testeTodos():
    rotateServo(10, 0)
    rotateServo(9, 0)
    rotateServo(8, 0)
    rotateServo(7, 0)
    rotateServo(6, 0)
    time.sleep(1)

    rotateServo(10, 150)
    time.sleep(1)
    rotateServo(10, 0)
    time.sleep(1)

    rotateServo(9, 130)
    time.sleep(1)
    rotateServo(9, 0)
    time.sleep(1)

    rotateServo(8, 130)
    time.sleep(1)
    rotateServo(8, 0)
    time.sleep(1)

    rotateServo(7, 130)
    time.sleep(1)
    rotateServo(7, 0)
    time.sleep(1)

    rotateServo(6, 130)
    time.sleep(1)
    rotateServo(6, 0)
    time.sleep(2)

# Teste de execução
try:
    testeTodos()
finally:
    print("muitods prints")
    # arduino.close()  # Fecha a conexão serial ao finalizar
