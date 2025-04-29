from pyfirmata import Arduino,SERVO
import time

board = Arduino('/dev/ttyUSB0')

pin1 = 10   # polegar
pin2 = 9    # indicador
pin3 = 8    # medio
pin4 = 7    # anelar
pin5 = 6    # mindinho

board.digital[pin1].mode = SERVO
board.digital[pin2].mode = SERVO
board.digital[pin3].mode = SERVO
board.digital[pin4].mode = SERVO
board.digital[pin5].mode = SERVO

def rotateServo(pino,angle):
    board.digital[pino].write(angle)
    time.sleep(0.015)


rotateServo(pin1,0)
rotateServo(pin2,0)
rotateServo(pin3,0)
rotateServo(pin4,0)
rotateServo(pin5,0)
time.sleep(1)

while True:
    rotateServo(pin1,180)
    time.sleep(1)
    rotateServo(pin1,0)
    time.sleep(1)

    rotateServo(pin2,240)
    time.sleep(1)
    rotateServo(pin2,0)
    time.sleep(1)

    rotateServo(pin3,180)
    time.sleep(1)
    rotateServo(pin3,0)
    time.sleep(1)

    rotateServo(pin4,300)
    time.sleep(1)
    rotateServo(pin4,0)
    time.sleep(1)

    rotateServo(pin5,130)
    time.sleep(1)
    rotateServo(pin5,0)
    time.sleep(2)