import cv2
import mediapipe as mp
import servo_braco3d as mao

cap = cv2.VideoCapture(0)

cap.set(3,840)
cap.set(4,680)

hands = mp.solutions.hands
Hands = hands.Hands(max_num_hands=1)
mpDwaw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    frameRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = Hands.process(frameRGB)
    handPoints = results.multi_hand_landmarks
    h, w, _ = img.shape
    pontos = []
    if handPoints:
        for points in handPoints:
            mpDwaw.draw_landmarks(img, points,hands.HAND_CONNECTIONS)
            #podemos enumerar esses pontos da seguinte forma
            for id, cord in enumerate(points.landmark):
                cx, cy = int(cord.x * w), int(cord.y * h)
                cv2.circle(img,(cx,cy),4,(255,0,0),-1)
                pontos.append((cx,cy))

            if pontos:
                distPolegar = abs(pontos[17][0] - pontos[4][0])
                distIndicador = pontos[5][1] - pontos[8][1]
                distMedio = pontos[9][1] - pontos[12][1]
                distAnelar = pontos[13][1] - pontos[16][1]
                distMinimo = pontos[17][1] - pontos[20][1]


                if distPolegar <80:

                    mao.abrir_fechar_thread(10,0)
                else:
                    mao.abrir_fechar_thread(10,1)

                if distIndicador >=1:
                    mao.abrir_fechar_thread(9,1)
                else:
                    mao.abrir_fechar_thread(9,0)

                if distMedio >=1:
                    mao.abrir_fechar_thread(8,1)
                else:
                    mao.abrir_fechar_thread(8,0)

                if distAnelar >=1:
                    mao.abrir_fechar_thread(7,1)
                else:
                    mao.abrir_fechar_thread(7,0)

                if distMinimo >=1:
                    mao.abrir_fechar_thread(6,1)
                else:
                    mao.abrir_fechar_thread(6,0)
    
    cv2.imshow('Imagem',img)
    if (cv2.waitKey(1) & 0xFF == 27) or (cv2.getWindowProperty('Imagem', cv2.WND_PROP_VISIBLE) < 1):
        break
  

  
cap.release()
cv2.destroyAllWindows()