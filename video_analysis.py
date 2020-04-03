import cv2
import numpy as np

# cap = cv2.VideoCapture(1) # For using the webcam.

cap = cv2.VideoCapture('./elon_musk.mp4')
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('output.avi', fourcc, 60.0, (w, h))

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    try:
        out.write(frame)
        print("DEBUG: WRITING INTO FRAME!!")
    except:
        print("ERROR: Video not writing to file.")


    cv2.imshow('Elon Colored', frame)
    cv2.imshow('Elon Grayscale', gray)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()