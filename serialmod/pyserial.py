import serial
import time

# Substitua '/dev/ttyUSB0' pela porta correta do seu Arduino
arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

# Função para enviar o ângulo ao Arduino
def setServoAngle(angle):
    if 0 <= angle <= 180:
        command = str(angle) + '\n'  # Envia o ângulo como uma string seguida por uma nova linha
        arduino.write(command.encode())  # Envia o comando para o Arduino
        time.sleep(0.1)  # Pequena pausa para garantir que o comando seja processado
    else:
        print("Ângulo fora do intervalo. Escolha entre 0 e 180 graus.")

# Teste: Enviar diferentes ângulos
try:
    print("Movendo o servo para 0 graus")
    setServoAngle(0)
    time.sleep(2)

    print("Movendo o servo para 90 graus")
    setServoAngle(90)
    time.sleep(2)

    print("Movendo o servo para 180 graus")
    setServoAngle(180)
    time.sleep(2)

    print("Voltando o servo para 0 graus")
    setServoAngle(0)
    time.sleep(2)

finally:
    arduino.close()  # Fechar a conexão serial ao final
    print("Teste concluído")