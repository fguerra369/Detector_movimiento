import cv2
import numpy as np

# Captura de video
cap = cv2.VideoCapture(0)

# Tomar el primer frame como referencia
ret, frame1 = cap.read()
gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
gray1 = cv2.GaussianBlur(gray1, (21, 21), 0)

while True:
    ret, frame2 = cap.read()
    if not ret:
        break

    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.GaussianBlur(gray2, (21, 21), 0)

    # Detectar movimiento
    delta_frame = cv2.absdiff(gray1, gray2)
    thresh = cv2.threshold(delta_frame, 25, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)

    # Buscar contornos grandes
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    rects = [cv2.boundingRect(c) for c in contours if cv2.contourArea(c) > 2000]

    if rects:
        # Combinar todos los rectángulos en uno solo
        x_min = min([r[0] for r in rects])
        y_min = min([r[1] for r in rects])
        x_max = max([r[0]+r[2] for r in rects])
        y_max = max([r[1]+r[3] for r in rects])
        cv2.rectangle(frame2, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

    cv2.imshow("Detección de Movimiento", frame2)
    gray1 = gray2.copy()  # Actualizar frame base

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


